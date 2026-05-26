from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BUTTON = (By.ID, "finish")

    def fill_details(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def continue_to_summary(self):
        self.click(self.CONTINUE_BUTTON)
        self.wait_for_url("checkout-step-two")
        return self

    def get_cart_item_name_by_index(self, idx):
        items = self.find_all(self.ITEM_NAMES)
        return items[idx].text

    def finish_order(self):
        self.click(self.FINISH_BUTTON)
        self.wait_for_url("checkout-complete")
        from pages.confirmation_page import ConfirmationPage
        return ConfirmationPage(self.driver)