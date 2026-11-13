const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1080 });
  const filePath = 'file://' + process.cwd() + '/../site/catalog/grassmannians/index.html';
  await page.goto(filePath, { waitUntil: 'networkidle0' });
  const metrics = await page.evaluate(() => {
    const parent = document.querySelector('.md-main__inner');
    if (!parent) return 'No md-main__inner';
    const children = Array.from(parent.children).map(el => {
      const r = el.getBoundingClientRect();
      return { tag: el.tagName, className: el.className, width: r.width, x: r.x };
    });
    return children;
  });
  console.log(JSON.stringify(metrics, null, 2));
  await browser.close();
})();
