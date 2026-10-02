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
  page.on('pageerror', error => errors.push(String(error)));
  try {
    const base = `http://127.0.0.1:${port}`;
    await page.goto(`${base}/catalog/`, {waitUntil: 'domcontentloaded'});
    await pause(1200);
    await page.evaluate(() => {
      const link = document.querySelector('nav a[href*="/catalog/grassmannians/"]');
      if (!link) throw new Error('Grassmannians navigation link not found');
      link.click();
    });
    await page.waitForFunction(() => location.pathname.endsWith('/catalog/grassmannians/'));
    await pause(2200);
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
    // Force a navigation while a preceding typeset is still pending.
    // Slow fonts/network make this possible in normal browsing as well.
    await page.evaluate(() => {
      const original = MathJax.typesetPromise.bind(MathJax);
      window.pendingTypeset = false;
      MathJax.typesetPromise = async elements => {
        window.pendingTypeset = true;
        await new Promise(resolve => setTimeout(resolve, 600));
        return original(elements);
      };
      document.querySelector('nav a[href*="flag_varieties/"]').click();
    });
    await page.waitForFunction(() => window.pendingTypeset);
    await page.evaluate(() => {
      document.querySelector('nav a[href*="projective/"]').click();
    });
    await page.waitForFunction(() => location.pathname.endsWith('/catalog/projective/'));
    await page.waitForFunction(() => {
      const formulas = [...document.querySelectorAll('.arithmatex')];
      return formulas.length > 0 && formulas.every(node => node.querySelector('mjx-container'));
    }, {timeout: 20000});
    const duplicates = await page.evaluate(() => [...document.querySelectorAll('.arithmatex')]
      .some(node => node.querySelectorAll('mjx-container').length !== 1));
    if (duplicates || errors.length) throw new Error(JSON.stringify({duplicates, errors}));
    console.log(`Catalog navigation passed: ${pageState.formulas} formulas rendered; #gr26 opened; rapid navigation rendered without refresh`);
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
