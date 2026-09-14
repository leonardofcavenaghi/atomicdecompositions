const puppeteer = require('puppeteer');
const http = require('http');
const handler = require('serve-handler');
const server = http.createServer((req, res) => handler(req, res, {public: '../site'}));
server.listen(3000, async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 800 });
  await page.goto('http://localhost:3000/catalog/grassmannians/#gr26', {waitUntil: 'networkidle0'});
  await new Promise(r => setTimeout(r, 2000));
  await page.evaluate(() => {
    document.querySelectorAll('details').forEach(d => d.setAttribute('open', 'true'));
  });
  await new Promise(r => setTimeout(r, 1000));
  const element = await page.$('#gr26 + details');
  if (element) {
    await element.screenshot({path: '../screenshot11.png'});
  } else {
    await page.screenshot({path: '../screenshot11.png'});
  }
  await browser.close();
  server.close();
});
