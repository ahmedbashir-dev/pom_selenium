from pages.login_page import LoginPage


def test_checkout_workflow(driver):
    login_page = LoginPage(driver).open(LoginPage.URL)
    inventory_page = login_page.login("standard_user", "secret_sauce")
    first_item_name = inventory_page.get_first_item_name()
    inventory_page.add_item_to_cart()
    cart_page = inventory_page.go_to_cart()
    assert inventory_page.get_cart_count() == "1"
    assert first_item_name in cart_page.get_cart_item_name_by_index(0)
    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.fill_details("Abhi", "Sarma", "78541").continue_to_summary()
    confirmation_page = checkout_page.finish_order()
    assert confirmation_page.get_confirmation_header() == "Thank you for your order!"
