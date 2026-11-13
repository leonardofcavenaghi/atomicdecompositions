const puppeteer = require('puppeteer');
const http = require('http');
const handler = require('serve-handler');

const server = http.createServer((request, response) => {
  return handler(request, response, {
    public: '../site'
  });
});

server.listen(3000, async () => {
  console.log('Server running at http://localhost:3000');
  
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 1000 });
  
  await page.goto('http://localhost:3000/catalog/grassmannians/#gr26', {waitUntil: 'networkidle0'});
  
  // Wait 5 seconds for MathJax
  await new Promise(r => setTimeout(r, 5000));
  
  // Open the flashcards
  await page.evaluate(() => {
    const details = document.querySelectorAll('details');
    details.forEach(d => d.setAttribute('open', 'true'));
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  await page.screenshot({path: '../screenshot3.png', fullPage: true});
  
  await browser.close();
  server.close();
});
