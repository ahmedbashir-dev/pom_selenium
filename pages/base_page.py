from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Tuple, Optional

class BasePage:
    """
    Parent class for all page objects.
    Provides shared browser interaction helpers so individual
    page objects can focus purely on page-specific behavior.
    """

    DEFAULT_TIMEOUT = 10  # more realistic for most applications

    def __init__(self, driver: WebDriver, timeout: int = None):
        self.driver = driver
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.wait = WebDriverWait(driver, self.timeout)

    def open(self, url: str) -> "BasePage":
        self.driver.get(url)
        return self

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """Wait until the element is visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Wait until at least one element is visible, then return all matches."""
        self.wait.until(EC.visibility_of_any_elements_located(locator))
        return self.driver.find_elements(*locator)

    def is_visible(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> bool:
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self, locator: Tuple[str, str]) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        # Optional but recommended for flaky UIs:
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def type_text(self, locator: Tuple[str, str], text: str, clear: bool = True) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        return self.find(locator).text.strip()

    def get_attribute(self, locator: Tuple[str, str], attr: str) -> Optional[str]:
        return self.find(locator).get_attribute(attr)

    def wait_for_url(self, partial_url: str, timeout: Optional[int] = None) -> None:
        WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.url_contains(partial_url)
        )

    def wait_for_title(self, partial_title: str, timeout: Optional[int] = None) -> None:
        WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.title_contains(partial_title)
        )