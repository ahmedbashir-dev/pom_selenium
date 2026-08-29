from pages.login_page import LoginPage


def test_success_login(driver):
    inventory_page = (
        LoginPage(driver)
        .open()                          # or .open(LoginPage.URL) if you keep the parameter
        .login("standard_user", "secret_sauce")
    )

    assert "inventory" in inventory_page.get_url()
    assert inventory_page.get_first_item_name() == "Sauce Labs Backpack"