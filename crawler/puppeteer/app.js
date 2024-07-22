const puppeteer = require('puppeteer');

(async () => {
  // Launch a new browser instance in headless mode
  const browser = await puppeteer.launch({
    headless: true, // Set this to false to see the browser window
    slowMo: 250, // Slow down the script by 250ms for better visibility
    devtools: true // Open the Chrome DevTools for debugging
  });

  // Create a new page
  const page = await browser.newPage();

  // Navigate to a website
  await page.goto('https://www.google.com');

  // Wait for the page to load
  await page.waitForNavigation();

  // Find an element on the page and click it
  await page.click('#my-button');

  // Wait for the page to update
  await page.waitForNavigation();

  // Take a screenshot of the page
  await page.screenshot({ path: 'example.png' });

  // Close the browser
  await browser.close();
})();
