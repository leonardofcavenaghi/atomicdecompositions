const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  // Set a standard desktop viewport
  await page.setViewport({ width: 1280, height: 1080 });
  
  // Load the built HTML file directly
  const filePath = 'file://' + process.cwd() + '/../site/catalog/grassmannians/index.html';
  await page.goto(filePath, { waitUntil: 'networkidle0' });
  
  // Open all details tags
  await page.evaluate(() => {
    document.querySelectorAll('details').forEach(d => d.setAttribute('open', 'true'));
  });
  
  // Wait for MathJax to render
  await page.waitForFunction(() => {
    return document.querySelectorAll('mjx-container').length > 0;
  }, { timeout: 10000 }).catch(() => console.log('MathJax timeout'));
  
  // Add a small delay for layout to settle
  await new Promise(r => setTimeout(r, 2000));
  
  // Take screenshot
  await page.screenshot({ path: 'screenshot8.png', fullPage: true });
  
  await browser.close();
})();
