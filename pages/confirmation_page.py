from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):
    HEADER = (By.CLASS_NAME, "complete-header")

    def get_confirmation_header(self) -> str:
        return self.get_text(self.HEADER)

    def is_order_complete(self) -> bool:
        return self.is_visible(self.HEADER)