#!/usr/bin/env node
/** Render every compiled equation before publishing, retaining accessible MathML. */
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');
const puppeteer = require('puppeteer');
const site = process.env.SITE_DIR || path.resolve(__dirname, '..', 'site');
function files(directory) {
  return fs.readdirSync(directory, {withFileTypes:true}).flatMap(entry => {
    const file = path.join(directory, entry.name);
    return entry.isDirectory() ? files(file) : file.endsWith('.html') ? [file] : [];
  });
}
async function main() {
  const browser = await puppeteer.launch({args:['--no-sandbox','--disable-setuid-sandbox']});
  let page;
  let runtimeBytes;
  try {
    for (const base of ['https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/',
      'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/']) {
      if (page) await page.close();
      page = await browser.newPage();
      await page.setContent('<!doctype html><html><head></head><body></body></html>');
      await page.evaluate(() => { window.MathJax = {startup:{typeset:false}, svg:{fontCache:'local'}}; });
      try {
        const runtimeResponse = page.waitForResponse(response =>
          response.url() === base+'tex-mml-svg.js' && response.status() === 200,
          {timeout:15000}).catch(() => null);
        await Promise.race([
          page.addScriptTag({url:base+'tex-mml-svg.js'}),
          new Promise((_,reject) => setTimeout(() => reject(new Error('Math renderer download timed out')),15000))
        ]);
        await page.waitForFunction(() => window.MathJax && typeof MathJax.tex2mmlPromise==='function', {timeout:15000});
        await page.evaluate(() => MathJax.startup.promise);
        if (await page.evaluate(() => MathJax.version) !== '3.2.2') throw new Error('Unexpected MathJax version');
        const response = await runtimeResponse;
        if (!response) throw new Error('Math renderer response was not captured');
        runtimeBytes = await response.buffer();
        break;
      } catch (error) {
        if (base.includes('cdnjs')) throw error;
      }
    }
    // Late-inserted source equations use the same pinned SVG runtime locally.
    // Published formulas remain fully rendered and need no browser runtime.
    const runtimeDirectory = path.join(site, 'assets/mathjax');
    fs.mkdirSync(runtimeDirectory, {recursive:true});
    if (!runtimeBytes || runtimeBytes.length < 100000) throw new Error('Incomplete MathJax runtime');
    fs.writeFileSync(path.join(runtimeDirectory, 'tex-mml-svg.js'), runtimeBytes);
    fs.copyFileSync(path.join(site, 'assets/mathjax-LICENSE.txt'), path.join(runtimeDirectory, 'LICENSE.txt'));
    // Preserve old published URLs without maintaining divergent source files.
    for (const name of ['mathjax-loader-v2.js', 'mathjax.js']) {
      fs.copyFileSync(path.join(site, 'javascripts/mathjax-loader.js'), path.join(site, 'javascripts', name));
    }
    const htmlFiles = files(site);
    let total = 0;
    const coverageErrors=[];
    for (const file of htmlFiles) {
      const result = await page.evaluate(async html => {
        const doc = new DOMParser().parseFromString(html,'text/html');
        const article = doc.querySelector('article');
        const bad = [];
        const labels = [];
        if (article) {
          const text = article.textContent;
          const opaque = text.match(/\b(?=[a-f0-9]{12}\b)(?=[a-f0-9]*[a-f])[a-f0-9]{12}\b/g) || [];
          const synthetic = text.match(/\b(?:QD5|QC5|PB5|PROD5|PCI5)-[A-Z0-9-]+\b|GM-20/g) || [];
          labels.push(...opaque,...synthetic);
        }
        if (labels.length) throw new Error('Non-geometric visible labels: '+[...new Set(labels)].join(', '));
        if (article) {
          const walker = doc.createTreeWalker(article,NodeFilter.SHOW_TEXT);
          while (walker.nextNode()) {
            const node=walker.currentNode;
            if (node.parentElement.closest('pre,code,script,style,.arithmatex,mjx-container')) continue;
            if (/\\[A-Za-z()[\]{}]|\$[^$\n]+\$|\$\$/.test(node.textContent)) bad.push(node.textContent.trim().slice(0,200));
          }
        }
        if (bad.length) return {bad:bad.slice(0,5)};
        MathJax.texReset();
        let count=0;
        for (const node of doc.querySelectorAll('.arithmatex')) {
          if (node.querySelector('mjx-container')) continue;
          const source=node.textContent.trim();
          const display=source.startsWith('\\[')&&source.endsWith('\\]');
          if (!display && !(source.startsWith('\\(')&&source.endsWith('\\)'))) throw new Error('Unknown math delimiters: '+source.slice(0,80));
          const tex=source.slice(2,-2);
          const mathml=await MathJax.tex2mmlPromise(tex,{display});
          if (/<merror\b/.test(mathml)) throw new Error('Invalid TeX: '+tex.slice(0,200));
          const rendered=await MathJax.mathml2svgPromise(mathml,{display});
          if (rendered.querySelector('[data-mml-node="merror"]')) throw new Error('Invalid SVG math: '+tex.slice(0,200));
          rendered.setAttribute('aria-hidden','true');
          node.replaceChildren(doc.importNode(rendered,true));
          const accessible=doc.createElement('span');
          accessible.className='geoatoms-mathml';
          accessible.innerHTML=mathml;
          node.appendChild(accessible);
          node.setAttribute('data-tex',tex);
          node.setAttribute('data-math-rendered','svg');
          count++;
        }
        return {html:'<!doctype html>\n'+doc.documentElement.outerHTML+'\n',count};
      }, fs.readFileSync(file,'utf8')).catch(error => {throw new Error(path.relative(site,file)+': '+error.message);});
      if (result.bad) { coverageErrors.push({page:path.relative(site,file),source:result.bad}); continue; }
      fs.writeFileSync(file,result.html);
      total+=result.count;
    }
    if (coverageErrors.length) throw new Error('Unwrapped source across compiled pages: '+JSON.stringify(coverageErrors));
    const stylesheet=await page.evaluate(() => MathJax.svgStylesheet().outerHTML);
    const accessibleStyle='<style>.arithmatex{position:relative}.geoatoms-mathml{position:absolute!important;left:0;top:0;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}</style>';
    for (const file of htmlFiles) {
      const html=fs.readFileSync(file,'utf8');
      const versioned=html.replace(/(<(?:script|link)\b[^>]*?\b(?:src|href)=)(["'])([^"']+)\2/g,
        (match,prefix,quote,url) => {
          if (/^(?:https?:|data:|\/\/|#)/.test(url)) return match;
          const relative=url.split(/[?#]/)[0];
          if (!/\.(?:css|js)$/.test(relative)) return match;
          const asset=path.resolve(path.dirname(file),decodeURIComponent(relative));
          if (!asset.startsWith(path.resolve(site)+path.sep)||!fs.existsSync(asset)) return match;
          const digest=crypto.createHash('sha256').update(fs.readFileSync(asset)).digest('hex').slice(0,16);
          const current=url.replace(/([?&])v=[^&]*/,'$1').replace(/[?&]$/,'');
          return prefix+quote+current+(current.includes('?')?'&':'?')+'v='+digest+quote;
        });
      fs.writeFileSync(file,versioned.replace('</head>',stylesheet+accessibleStyle+'</head>'));
    }
    console.log(JSON.stringify({static_math_pages:htmlFiles.length,rendered_formulas:total,renderer:'MathJax 3.2.2 SVG; accessible MathML; no client runtime required'}));
  } finally { await browser.close(); }
}
main().catch(error => {console.error(error);process.exitCode=1;});
