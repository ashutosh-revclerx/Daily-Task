import os
import re
import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://playwright.dev"
SCREENSHOT_DIR = "screenshots"


# =========================================================
# FIXTURE: Chrome browser + screenshots after each test
# =========================================================
@pytest.fixture(scope="function")
def page(request):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=True   # set False to see browser
        )

        context = browser.new_context()
        page = context.new_page()

        # Increase default timeout for stability
        page.set_default_timeout(60000)

        yield page

        # Screenshot after every test
        page.screenshot(
            path=f"{SCREENSHOT_DIR}/{request.node.name}.png",
            full_page=True
        )

        browser.close()


# ===============================
# SCENARIO 1: Homepage loads
# ===============================
def test_homepage_loads(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page).to_have_title(re.compile("Playwright"))


# ==================================
# SCENARIO 2: Get Started visible
# ==================================
def test_get_started_button_visible(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page.get_by_role("link", name="Get started")).to_be_visible()


# ==================================
# SCENARIO 3: Navigate to Docs
# ==================================
def test_navigation_to_docs(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url(re.compile(".*/docs.*"))


# =========================================
# SCENARIO 4: Switch docs language to Python
# =========================================
def test_switch_to_python_docs(page):
    page.goto(f"{BASE_URL}/docs/intro", wait_until="domcontentloaded")
    page.get_by_role("tab", name="Python").click()
    expect(page.locator("h1")).to_contain_text("Installation")


# ==========================================
# SCENARIO 5: Use search feature
# ==========================================
def test_search_feature(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Search").click()
    page.get_by_placeholder("Search docs").fill("browser")
    page.keyboard.press("Enter")
    expect(page.locator("body")).to_contain_text("browser")
