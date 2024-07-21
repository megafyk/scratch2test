const puppeteer = require('puppeteer');
const fs = require('fs');
const { parse } = require('csv-parse/sync');
require('dotenv').config();

// Login credentials
const baseUrl = process.env.BASE_URL;
const loginUrl = baseUrl + "/#/signin";
const paymentUrl = baseUrl + "/api/paymentTransaction";
const username = process.env.USERNAME;
const password = process.env.PASSWORD;


(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  // Navigate to the login page
  await page.goto(loginUrl);

  // Fill in the login form and submit
  await page.type('#username', username);
  await page.type('#password', password);
  await Promise.all([
    page.click('button[type="submit"].ant-btn.ant-btn-primary'),
    page.waitForNavigation(),
  ]);

  // Read the CSV file with transaction IDs
  let csvData = fs.readFileSync('file.csv', 'utf8');
  let transactionIds = parse(csvData, {
    columns: true,
    skip_empty_lines: true
  }).map(row => row.transactionId);

  // Fetch the transaction details
  for (let transactionId of transactionIds) {
    let queryParams = {
      page: 282,
      api: 'find',
      queryInput: {
        transactionId: {
          contains: transactionId
        }
      },
      limit: 10,
      skip: 0,
      sort: [
        {
          id: 'desc'
        }
      ]
    };

    let queryUrl = new URLSearchParams(queryParams).toString();
    let url = `${paymentUrl}?${queryUrl}`;

    // Use Puppeteer to fetch the JSON response
    let response = await page.goto(url);
    let transactionData = await response.json();
    console.log(`Transaction ID: ${transactionId}`);
    console.log(transactionData);
  }

  // Close the browser
  await browser.close();
})();
