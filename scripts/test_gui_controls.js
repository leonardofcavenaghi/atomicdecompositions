#!/usr/bin/env node
/**
 * Browser regression for the local GUI's copy-input and download-result tools.
 * Run `npm ci` in this directory before invoking this script.
 */
const fs = require('node:fs');
const http = require('node:http');
const os = require('node:os');
const path = require('node:path');
const {spawn} = require('node:child_process');
const puppeteer = require('puppeteer');

function freePort() {
  return new Promise((resolve, reject) => {
    const server = http.createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const port = server.address().port;
      server.close(() => resolve(port));
    });
  });
}

function waitForHttp(url, child, timeout = 15000) {
  const start = Date.now();
  return new Promise((resolve, reject) => {
    const check = () => {
      if (Date.now() - start > timeout) {
        reject(new Error(`GUI did not start at ${url}`));
        return;
      }
      if (child.exitCode !== null) {
        reject(new Error(`GUI exited with code ${child.exitCode}`));
        return;
      }
      const request = http.get(url, response => {
        response.resume();
        if (response.statusCode === 200) {
          resolve();
        } else {
          setTimeout(check, 100);
        }
      });
      request.on('error', () => setTimeout(check, 100));
    };
    check();
  });
}

async function main() {
  const root = path.resolve(__dirname, '..');
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const python = process.env.PYTHON || 'python3';
  const child = spawn(python, ['-m', 'gwflags.gui', '--port', String(port), '--no-browser'], {
    cwd: root,
    stdio: ['ignore', 'pipe', 'pipe']
  });
  let stderr = '';
  child.stderr.on('data', chunk => { stderr += chunk.toString(); });
  let browser;
  const downloadPath = fs.mkdtempSync(path.join(os.tmpdir(), 'gwflags-gui-download-'));
  try {
    await waitForHttp(base, child);
    browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
    const context = browser.defaultBrowserContext();
    if (context && context.overridePermissions) {
      await context.overridePermissions(base, ['clipboard-read', 'clipboard-write']);
    }
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(String(error)));
    const client = await page.createCDPSession();
    await client.send('Browser.setDownloadBehavior', {behavior: 'allow', downloadPath});
    await page.goto(base, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(() => document.querySelectorAll('#preset option').length > 1);

    const initial = await page.evaluate(() => ({
      copy: !!document.querySelector('#copy-input'),
      download: !!document.querySelector('#download-output'),
      disabled: document.querySelector('#download-output').disabled
    }));
    if (!initial.copy || !initial.download || !initial.disabled) {
      throw new Error(`result-tool controls missing or incorrectly enabled: ${JSON.stringify(initial)}`);
    }

    await page.click('#copy-input');
    await page.waitForFunction(() => document.querySelector('#copy-status').textContent === 'Input copied.');
    const copied = await page.evaluate(async () => {
      if (!navigator.clipboard || !navigator.clipboard.readText) return '';
      try { return await navigator.clipboard.readText(); } catch (_) { return ''; }
    });
    if (copied && !copied.includes('"algebra"') ) {
      throw new Error(`clipboard did not contain input JSON: ${copied}`);
    }

    await page.click('#binfo');
    await page.waitForFunction(() => {
      const button = document.querySelector('#download-output');
      return button && !button.disabled && document.querySelector('#out .badge');
    }, {timeout: 20000});
    await page.click('#download-output');
    const start = Date.now();
    let files = [];
    while (!(files = fs.readdirSync(downloadPath)).length && Date.now() - start < 10000) {
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    if (!files.length) throw new Error('download-result button did not create a file');
    const downloaded = JSON.parse(fs.readFileSync(path.join(downloadPath, files[0]), 'utf8'));
    if (downloaded.input.action !== 'info' || downloaded.result.dim !== 2) {
      throw new Error(`downloaded result has unexpected content: ${JSON.stringify(downloaded)}`);
    }
    if (errors.length) throw new Error(`browser page errors: ${errors.join('; ')}`);
    console.log(`GUI controls passed: copied input and downloaded ${files[0]}`);
  } finally {
    if (browser) await browser.close();
    child.kill('SIGTERM');
    fs.rmSync(downloadPath, {recursive: true, force: true});
    if (stderr.trim()) process.stderr.write(stderr);
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
