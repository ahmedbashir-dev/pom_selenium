from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_count(self) -> int:
        return len(self.find_all(self.CART_ITEMS))

    def get_cart_item_name_by_index(self, idx: int) -> str:
        names = self.find_all(self.ITEM_NAMES)
        return names[idx].text

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_for_url("checkout-step-one")   # note: correct URL fragment
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)