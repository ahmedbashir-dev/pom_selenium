from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):
    HEADER = (By.CLASS_NAME, "complete-header")

    def get_confirmation_header(self):
        return self.get_text(self.HEADER)