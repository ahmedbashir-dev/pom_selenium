import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    web_driver = webdriver.Chrome(options=chrome_options)
    web_driver.delete_all_cookies()
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
