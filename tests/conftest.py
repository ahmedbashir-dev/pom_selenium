import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    # Common options
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")

    # Headless mode for CI (GitHub Actions)
    if os.getenv("CI") or os.getenv("GITHUB_ACTIONS"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()

    # maximize only when not headless
    if not (os.getenv("CI") or os.getenv("GITHUB_ACTIONS")):
        driver.maximize_window()

    yield driver
    driver.quit()