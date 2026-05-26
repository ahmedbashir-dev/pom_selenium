from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_count(self):
        return len(self.find_all(self.CART_ITEMS))

    def get_cart_item_name_by_index(self, idx):
        items = self.find_all(self.CART_ITEMS)
        return items[idx].text

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_for_url("checkout-step-1")
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)