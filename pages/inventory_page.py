from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    # Locators
    FIRST_ITEM_NAME = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_first_item_name(self):
        return self.get_text(self.FIRST_ITEM_NAME)

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.SHOPPING_CART_ICON)
        self.wait_for_url("cart")
        from pages.cart_page import CartPage
        return CartPage(self.driver)