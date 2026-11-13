const puppeteer = require('puppeteer');
const http = require('http');
const handler = require('serve-handler');
const server = http.createServer((req, res) => handler(req, res, {public: '../site'}));
server.listen(3000, async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 800 });
  await page.goto('http://localhost:3000/catalog/grassmannians/', {waitUntil: 'networkidle0'});
  await new Promise(r => setTimeout(r, 2000));
  await page.evaluate(() => {
    document.querySelectorAll('details').forEach(d => d.setAttribute('open', 'true'));
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({path: '../screenshot8.png', fullPage: true});
  await browser.close();
  server.close();
});
