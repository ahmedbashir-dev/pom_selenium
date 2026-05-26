from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        self.wait_for_url("inventory")
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def login(self, username, password):
        return (
            self.enter_username(username)
            .enter_password(password)
            .click_login()
        )
