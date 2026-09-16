#!/usr/bin/env node
/**
 * Browser regression for catalog instant navigation and MathJax rendering.
 * Run `mkdocs build` first and install scripts/package.json dependencies.
 */
const path = require('node:path');
const http = require('node:http');
const puppeteer = require('puppeteer');
const handler = require('serve-handler');

const pause = ms => new Promise(resolve => setTimeout(resolve, ms));

async function main() {
  const server = http.createServer((request, response) => handler(request, response, {
    public: path.resolve(__dirname, '..', 'site')
  }));
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
    console.log(`Catalog navigation passed: ${pageState.formulas} formulas rendered; #gr26 opened`);
  } finally {
    await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
