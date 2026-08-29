from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    # More stable locators
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_first_item_name(self) -> str:
        return self.get_text(self.ITEM_NAME)   # gets the first one

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)
        return self

    def get_cart_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.SHOPPING_CART_ICON)
        self.wait_for_url("cart")
        from pages.cart_page import CartPage
        return CartPage(self.driver)