from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
        Parent class for all page objects.

        Provides shared browser interaction helpers so individual
        page objects can focus purely on page-specific behavior
    """

    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def find(self, locator):
        """Wait and return the single matching element"""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_all(self, locator):
        """Wait and return all matching elements"""
        self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text.strip()

    def get_attribute(self, locator, attr):
        return self.find(locator).get_attribute(attr)

    def wait_for_url(self, partial_url, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )
