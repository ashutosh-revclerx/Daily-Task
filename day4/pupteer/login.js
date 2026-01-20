const puppeteer = require("puppeteer");
const assert = require("assert");
const fs = require("fs");
const path = require("path");

// ---------- CONFIG ----------
const BASE_URL = "https://www.saucedemo.com/";
const USERNAME = process.env.TEST_USER || "standard_user";
const PASSWORD = process.env.TEST_PASS || "secret_sauce";
const SCREENSHOT_DIR = path.join(__dirname, "screenshots");

// Create screenshots directory if not exists
if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR);
}

(async () => {
  const browser = await puppeteer.launch({
    headless: true,          // set false to see browser
    slowMo: 50,
    defaultViewport: null,
    args: ["--start-maximized"]
  });

  const page = await browser.newPage();
  page.setDefaultTimeout(30000);

  try {
    // ==========================
    // SCENARIO 1: Open Website
    // ==========================
    await page.goto(BASE_URL, { waitUntil: "domcontentloaded" });
    await page.screenshot({ path: `${SCREENSHOT_DIR}/01_home.png` });

    // ==========================
    // SCENARIO 2: Login
    // ==========================
    await page.type("#user-name", USERNAME);
    await page.type("#password", PASSWORD);

    await Promise.all([
      page.click("#login-button"),
      page.waitForNavigation({ waitUntil: "domcontentloaded" })
    ]);

    assert(page.url().includes("inventory"));
    await page.screenshot({ path: `${SCREENSHOT_DIR}/02_login_success.png` });

    // ==========================
    // SCENARIO 3: Add Item (Create)
    // ==========================
    await page.click("#add-to-cart-sauce-labs-backpack");
    await page.screenshot({ path: `${SCREENSHOT_DIR}/03_item_added.png` });

    // ==========================
    // SCENARIO 4: Verify Item in Cart (Read)
    // ==========================
    await page.click(".shopping_cart_link");
    await page.waitForSelector(".cart_item");

    const itemName = await page.$eval(
      ".inventory_item_name",
      el => el.textContent
    );

    assert.strictEqual(itemName, "Sauce Labs Backpack");
    await page.screenshot({ path: `${SCREENSHOT_DIR}/04_item_verified.png` });

    // ==========================
    // SCENARIO 5: Logout
    // ==========================
    await page.click("#react-burger-menu-btn");
    await page.waitForSelector("#logout_sidebar_link");
    await page.click("#logout_sidebar_link");

    await page.waitForSelector("#login-button");
    assert(page.url().includes("saucedemo"));
    await page.screenshot({ path: `${SCREENSHOT_DIR}/05_logout.png` });

    console.log("✅ Puppeteer login & data operation tests passed");

  } catch (error) {
    console.error("❌ Test failed:", error.message);
    await page.screenshot({ path: `${SCREENSHOT_DIR}/error.png` });
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
