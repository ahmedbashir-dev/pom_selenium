from pages.login_page import LoginPage


def test_success_login(driver):
    login_page = LoginPage(driver)
    login_page.open(LoginPage.URL)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.get_url()