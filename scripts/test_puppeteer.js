const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', defaultViewport: { width: 1280, height: 800 } });
  const page = await browser.newPage();
  await page.goto('https://ahuchala.com/hodge/', { waitUntil: 'networkidle2' });
  
  await page.evaluate(() => {
    // Find the button containing 'Gr(k, n)'
    const buttons = document.querySelectorAll('button');
    for (const btn of buttons) {
      if (btn.innerText.includes('Gr(k, n)')) {
        btn.click();
      }
    }
  });

  await new Promise(r => setTimeout(r, 1000));

  await page.evaluate(() => {
    document.getElementById('k-value-grassmannian').value = 2;
    document.getElementById('k-value-grassmannian').dispatchEvent(new Event('input', { bubbles: true }));
    document.getElementById('n-value-grassmannian').value = 5;
    document.getElementById('n-value-grassmannian').dispatchEvent(new Event('input', { bubbles: true }));
    document.getElementById('r-value-grassmannian').value = 1;
    document.getElementById('r-value-grassmannian').dispatchEvent(new Event('input', { bubbles: true }));
    document.getElementById('dims-input').value = '2';
    document.getElementById('dims-input').dispatchEvent(new Event('input', { bubbles: true }));
  });

  await new Promise(r => setTimeout(r, 2000));
  
  await page.screenshot({ path: 'screenshot.png', fullPage: true });

  const diamond = await page.evaluate(() => {
    const d = document.getElementById('hodge-diamond');
    if (!d) return "no #hodge-diamond found";
    const rows = d.querySelectorAll('.diamond-row');
    if (rows.length === 0) return "no rows found in #hodge-diamond";
    return Array.from(rows).map(row => row.innerText.trim());
  });
  
  console.log("Diamond HTML:\n" + diamond);
  
  await browser.close();
})();
