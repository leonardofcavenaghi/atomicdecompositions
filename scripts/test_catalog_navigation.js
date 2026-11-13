#!/usr/bin/env node
/**
 * Browser regression for catalog instant navigation and MathJax rendering.
 * Run `mkdocs build` first and install scripts/package.json dependencies.
 */
const path = require('node:path');
const http = require('node:http');
const fs = require('node:fs');
const puppeteer = require('puppeteer');
const handler = require('serve-handler');

const pause = ms => new Promise(resolve => setTimeout(resolve, ms));

async function measureMath(page, label, started) {
  await page.waitForFunction(() => {
    const nodes = [...document.querySelectorAll('.arithmatex')];
    return nodes.length > 0 && nodes.every(node =>
      node.querySelectorAll('mjx-container').length === 1);
  }, {timeout: 20000, polling: 50});
  const formulas = await page.$$eval('.arithmatex', nodes => nodes.length);
  const unwrapped = await page.evaluate(() => {
    const article = document.querySelector('article');
    if (!article) return [];
    const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT);
    const bad = [];
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (node.parentElement.closest('pre,code,script,style,.arithmatex,mjx-container')) continue;
      if (/\\(?:frac|begin|mathbb|langle|rangle|sum|operatorname)\b|\\[()[\]]/.test(node.textContent)) bad.push(node.textContent.trim().slice(0,180));
    }
    return bad;
  });
  if (unwrapped.length) throw new Error(label + ': raw TeX outside math blocks: ' + JSON.stringify(unwrapped.slice(0,5)));
  const errors = await page.$$eval('mjx-merror,[data-mml-node="merror"]', nodes => nodes.length);
  if (errors) throw new Error(label + ': MathJax reported ' + errors + ' formula errors');
  return {page: label, navigation_to_rendered_ms: Date.now() - started, formulas};
}

async function checkFirstOpen(browser, base, mode) {
  const cold = await browser.newPage();
  const pageErrors = []; const sources = [];
  let intercepted = false; let documents = 0;
  cold.on('pageerror', error => pageErrors.push(String(error)));
  await cold.setCacheEnabled(false);
  await cold.setRequestInterception(true);
  cold.on('request', async request => {
    if (request.isNavigationRequest() && request.frame() === cold.mainFrame()) documents++;
    if (request.url().includes('mathjax') && request.url().includes('tex-mml-chtml.js')) {
      sources.push(request.url());
      if (!intercepted) {
        intercepted=true;
        if (mode==='failed-primary') { await request.abort(); return; }
        await pause(4000);
      }
    }
    await request.continue();
  });
  try {
    const start=Date.now();
    await cold.goto(base+'/catalog/records/qc5-001/',{waitUntil:'domcontentloaded'});
    const first=await measureMath(cold,'pre-rendered uncached first open',start);
    if (sources.length) throw new Error('Static equations requested a browser math runtime');
    await cold.waitForFunction(() => typeof document$!=='undefined');
    await cold.evaluate(() => new Promise(resolve => document$.subscribe(resolve)));
    await cold.evaluate(() => document.querySelector('nav a[href*="projective/"]').click());
    await cold.waitForFunction(() => location.pathname.endsWith('/catalog/projective/'));
    await measureMath(cold,'pre-rendered instant navigation',Date.now());
    if (sources.length || documents!==1) throw new Error('Static navigation depended on runtime/reload');
    await cold.evaluate(() => {
      const node=document.createElement('span');node.className='arithmatex';node.id='late-math-probe';
      node.textContent=String.raw`\(1+1=2\)`;
      document.querySelector('[data-md-component="content"]').appendChild(node);
    });
    await cold.waitForFunction(() => document.querySelector('#late-math-probe mjx-container'),{timeout:20000});
    if (!intercepted || pageErrors.length) throw new Error(JSON.stringify({mode,intercepted,pageErrors}));
    if (mode==='failed-primary' && !sources.some(url=>url.includes('cdnjs'))) throw new Error('Dynamic alternate runtime was not used');
    console.log('First-open static math and dynamic recovery passed: '+JSON.stringify({...first,mode,documents,sources}));
  } finally { await cold.close(); }
}

async function checkWithoutBrowserRenderer(browser, base) {
  const page=await browser.newPage();let mathRequests=0;
  await page.setCacheEnabled(false);
  await page.setJavaScriptEnabled(false);
  page.on('request',request=>{if (/https:\/\/.*(?:jsdelivr|cdnjs).*mathjax/.test(request.url())) mathRequests++;});
  try {
    await page.goto(base+'/methodology/',{waitUntil:'domcontentloaded'});
    const session=await page.createCDPSession();
    const {root}=await session.send('DOM.getDocument',{depth:0});
    const all=await session.send('DOM.querySelectorAll',{nodeId:root.nodeId,selector:'.arithmatex'});
    const rendered=await session.send('DOM.querySelectorAll',{nodeId:root.nodeId,selector:'.arithmatex mjx-container[jax="SVG"]'});
    const accessible=await session.send('DOM.querySelectorAll',{nodeId:root.nodeId,selector:'.geoatoms-mathml math'});
    if (!all.nodeIds.length || all.nodeIds.length!==rendered.nodeIds.length || all.nodeIds.length!==accessible.nodeIds.length || mathRequests) throw new Error('Math is not complete without JavaScript');
    console.log('JavaScript-disabled first open passed: '+rendered.nodeIds.length+' rendered equations and accessible MathML, no CDN math request.');
    await session.detach();
  } finally { await page.close(); }
  const blocked=await browser.newPage();await blocked.setCacheEnabled(false);await blocked.setRequestInterception(true);
  blocked.on('request',request => /https:\/\/.*(?:jsdelivr|cdnjs).*mathjax/.test(request.url()) ? request.abort() : request.continue());
  try {
    await blocked.goto(base+'/catalog/records/qc5-001/',{waitUntil:'domcontentloaded'});
    await measureMath(blocked,'first open with every math CDN blocked',Date.now());
    console.log('CDN-blocked first open passed without a refresh.');
  } finally { await blocked.close(); }
}

async function main() {
  const site = process.env.SITE_DIR || path.resolve(__dirname, '..', 'site');
  const server = http.createServer((request, response) => {
    const pathname = new URL(request.url, 'http://localhost').pathname;
    const file = path.join(site, pathname.endsWith('/') ? `${pathname}index.html` : pathname);
    if ((file.endsWith('.html') || file.endsWith('.xml')) && fs.existsSync(file)) {
      // Production absolute links and sitemap entries must stay on this build.
      const body = fs.readFileSync(file, 'utf8').replaceAll(
        'https://leonardofcavenaghi.github.io/atomicdecompositions/',
        `http://127.0.0.1:${server.address().port}/`);
      response.setHeader('Content-Type', file.endsWith('.xml') ? 'application/xml' : 'text/html');
      response.end(body);
    } else {
      return handler(request, response, {public: site});
    }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const { port } = server.address();
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  const errors = [];
  const renderingTimings = [];
  page.on('pageerror', error => errors.push(String(error)));
  try {
    const base = `http://127.0.0.1:${port}`;
    await page.goto(`${base}/`, {waitUntil: 'domcontentloaded'});
    await page.evaluate(() => {
      [...document.querySelectorAll('nav a[href]')].find(link =>
        new URL(link.href).pathname.endsWith('/catalog/')).click();
    });
    await page.waitForFunction(() => location.pathname.endsWith('/catalog/') &&
      window.jQuery && jQuery.fn.dataTable && jQuery.fn.dataTable.isDataTable('table'));
    await pause(1200);
    const grassmannianStarted = Date.now();
    await page.evaluate(() => {
      const link = document.querySelector('nav a[href*="/catalog/grassmannians/"]');
      if (!link) throw new Error('Grassmannians navigation link not found');
      link.click();
    });
    await page.waitForFunction(() => location.pathname.endsWith('/catalog/grassmannians/'));
    renderingTimings.push(await measureMath(page, 'grassmannians: instant navigation', grassmannianStarted));
    const pageState = await page.evaluate(() => ({
      math: Array.from(document.querySelectorAll('.arithmatex'))
        .every(node => node.querySelector('mjx-container')),
      formulas: document.querySelectorAll('mjx-container').length
    }));
    await page.evaluate(() => {
      const link = document.querySelector('table a[href*="#gr26"]');
      if (!link) throw new Error('Gr(2,6) catalog link not found');
      link.click();
    });
    await pause(500);
    const cardState = await page.evaluate(() => {
      const anchor = document.getElementById('gr26');
      const card = anchor && anchor.parentElement.nextElementSibling;
      return {
        hash: location.hash,
        open: !!card && card.matches('details') && card.open,
        math: Array.from(document.querySelectorAll('.arithmatex'))
          .every(node => node.querySelector('mjx-container'))
      };
    });
    if (!pageState.math || pageState.formulas === 0 || !cardState.open || !cardState.math || errors.length) {
      throw new Error(JSON.stringify({pageState, cardState, errors}));
    }
    if (new URL(page.url()).origin !== base) throw new Error('Test left the local build');
    // Published equations survive rapid navigation without a runtime startup.
    const rapidStarted = Date.now();
    await page.evaluate(() => document.querySelector('nav a[href*="additional/"]').click());
    await page.waitForFunction(() => location.pathname.endsWith('/catalog/additional/'));
    await page.evaluate(() => document.querySelector('nav a[href*="projective/"]').click());
    await page.waitForFunction(() => location.pathname.endsWith('/catalog/projective/'));
    renderingTimings.push(await measureMath(page,'pre-rendered rapid navigation',rapidStarted));
    const duplicates = await page.evaluate(() => [...document.querySelectorAll('.arithmatex')]
      .some(node => node.querySelectorAll('mjx-container').length !== 1));
    if (duplicates || errors.length) throw new Error(JSON.stringify({duplicates, errors}));
    console.log(`Catalog navigation passed: ${pageState.formulas} formulas rendered; #gr26 opened; rapid navigation rendered without refresh`);
    await page.goto(`${base}/catalog/additional/#fl125o01o02o10gm20`, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(() => {
      const card = document.getElementById('fl125o01o02o10gm20').parentElement.nextElementSibling;
      return card.open && card.querySelector('mjx-container');
    });
    await page.waitForFunction(() => [...document.querySelectorAll('.arithmatex')]
      .every(node => node.querySelectorAll('mjx-container').length === 1));
    const computed = await page.evaluate(async () => {
      const response = await fetch('../../data/localization-results.json');
      if (!response.ok) throw new Error('Exact dataset is not downloadable');
      const data = await response.json();
      const gm = data.examples.find(row => row.id === 'e1322438fd01');
      return {records: data.examples.length, cards: document.querySelectorAll('details.example').length,
        gmRank: gm.matrix_at_one.length, corner: gm.matrix_at_one[0][8]};
    });
    if (computed.records !== 131 || computed.cards !== 15 || computed.gmRank !== 9 || computed.corner !== '880') {
      throw new Error(JSON.stringify(computed));
    }
    if (process.env.CATALOG_SCREENSHOT) await page.screenshot({path: process.env.CATALOG_SCREENSHOT, fullPage: false});
    await page.goto(`${base}/catalog/`, {waitUntil: 'networkidle0'});
    await page.waitForFunction(() => window.jQuery && jQuery.fn.dataTable && jQuery.fn.dataTable.isDataTable('table'));
    await page.evaluate(() => jQuery('table').DataTable().search('P4 / O(3)', false, false).draw());
    const cubicIndex = await page.$eval('tbody tr', row => row.cells[3].textContent.trim());
    if (cubicIndex !== '2' || errors.length) throw new Error(JSON.stringify({cubicIndex, errors}));
    console.log('Computed catalog passed: 15 new cards, 131 downloadable results, full GM-20 matrix, correct master-table ambient index.');

    const catalogue = await page.evaluate(async base => fetch(base + '/data/catalog-records.json').then(r => r.json()), base);
    for (const [collection, dimension] of [['fourfolds',4],['fivefolds',5]]) {
      const expected = catalogue.records.filter(r => r.dimension === dimension).length;
      await page.goto(`${base}/catalog/${collection}/`, {waitUntil:'domcontentloaded'});
      await page.waitForFunction(() => window.jQuery && jQuery.fn.dataTable && jQuery.fn.dataTable.isDataTable('table'));
      const count=await page.evaluate(() => jQuery('table').DataTable().rows().count());
      if (count!==expected) throw new Error('Wrong dimension collection count: '+collection+' '+count);
    }
    const recordIds = await page.evaluate(async base => {
      const data = await fetch(base + '/data/catalog-records.json').then(r => r.json());
      return data.records.filter(r => r.link.startsWith('records/')).map(r => r.link.split('/').pop().replace('.md',''));
    }, base);
    for (const id of recordIds) {
      const started = Date.now();
      await page.goto(`${base}/catalog/records/${id}/`, {waitUntil:'domcontentloaded'});
      renderingTimings.push(await measureMath(page, id + ': full-page navigation with cached shared assets', started));
      if (id === 'qc5-001') {
        const multiset = await page.evaluate(async base => {
          const data = await fetch(base + '/data/connection-exponents.json').then(r => r.json());
          const factor = data.records.find(r => r.id === 'QC5-001').factors.find(f => f.number === 1);
          const table = document.querySelector('article table');
          return {classes: factor.classes, rows: table.tBodies[0].rows.length,
            displayedHalves: table.tBodies[0].rows[0].cells[2].querySelectorAll('mjx-mfrac,[data-mml-node="mfrac"]').length};
        }, base);
        if (JSON.stringify(multiset.classes) !== JSON.stringify(['0','1/2','1/2']) ||
            multiset.rows !== 3 || multiset.displayedHalves !== 2) {
          throw new Error('Repeated exponent classes were lost: ' + JSON.stringify(multiset));
        }
      }

      const state=await page.evaluate(() => ({
        mathErrors:document.querySelectorAll('mjx-merror').length,
        inputs:document.querySelectorAll('pre code').length,
        matrices:[...document.querySelectorAll('table')].some(t => t.textContent.includes('M')),
        emptyLinks:[...document.querySelectorAll('article a')].some(a => !a.getAttribute('href'))
      }));
      if (state.mathErrors || state.inputs<2 || !state.matrices || state.emptyLinks) throw new Error(id+': '+JSON.stringify(state));
    }
    for (const route of ['methodology/', 'toric/mathematics/', 'catalog/atomic-invariants/',
      ...['points-curves','surfaces','threefolds','fourfolds','fivefolds','higher-dimensional'].map(s => 'catalog/invariants-' + s + '/')]) {
      const started = Date.now();
      await page.goto(base + '/' + route, {waitUntil: 'domcontentloaded'});
      renderingTimings.push(await measureMath(page, route + ': mathematical rendering', started));
    }
    await page.goto(base + '/catalog/atomic-invariants/', {waitUntil:'domcontentloaded'});
    await page.waitForFunction(() => window.jQuery && jQuery.fn.dataTable &&
      jQuery.fn.dataTable.isDataTable('.atomic-index table'));
    const atomicCounts = await page.evaluate(() => {
      const table = jQuery('.atomic-index table').DataTable();
      const total = table.rows().count();
      table.search('Full atomic invariants').draw(); const full = table.rows({search:'applied'}).count();
      table.search('Ambient matrix incomplete').draw(); const incomplete = table.rows({search:'applied'}).count();
      table.search('').draw(); return {total,full,incomplete};
    });
    const atomicData = await page.evaluate(async base => fetch(base + '/data/atomic-invariants.json').then(r => r.json()), base);
    if (atomicCounts.total !== catalogue.records.length || atomicCounts.full !== atomicData.counts.full_coarse_factors ||
        atomicCounts.incomplete !== atomicData.counts.ambient_sector_incomplete)
      throw new Error('Atomic audit table mismatch: ' + JSON.stringify(atomicCounts));
    await page.goto(`${base}/`, {waitUntil:'domcontentloaded'});
    if (await page.$$eval('.geometry-card', cards=>cards.length)!==2) throw new Error('Geometry division missing');
    const search = await page.evaluate(async () => {
      const [index,records] = await Promise.all([
        fetch('search/search_index.json').then(r=>r.json()),
        fetch('data/catalog-records.json').then(r=>r.json())
      ]);
      const missing=records.records.filter(r => r.link.startsWith('records/')).filter(r =>
        !index.docs.some(d => d.location === 'catalog/'+r.link.replace('.md','/') && r.keywords.every(keyword => d.text.includes(keyword))));
      return {missing:missing.map(r=>r.id),count:index.docs.length};
    });
    if (search.missing.length) throw new Error('Unindexed catalogue records: '+search.missing.join(', '));
    await page.setViewport({width:390,height:844});
    if (await page.evaluate(() => document.documentElement.scrollWidth>window.innerWidth+2)) throw new Error('Home page overflows mobile viewport');
    for (const route of ['catalog/records/qc5-001/', 'catalog/records/lg3-1-2/', 'catalog/invariants-fourfolds/']) {
      await page.goto(base + '/' + route, {waitUntil:'domcontentloaded'});
      await measureMath(page, route + ': mobile mathematical layout', Date.now());
      if (await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 2))
        throw new Error('Mobile overflow: ' + route);
    }
    if (errors.length) throw new Error(errors.join('; '));
    await checkWithoutBrowserRenderer(browser, base);
    await checkFirstOpen(browser, base, 'failed-primary');
    await checkFirstOpen(browser, base, 'delayed-startup');
    console.log('MathJax render timings: ' + JSON.stringify(renderingTimings));
    console.log('Universal catalogue and search passed: ' + catalogue.records.length + ' records, exact matrix tables and rendered mathematics; mobile home layout.');

  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });

