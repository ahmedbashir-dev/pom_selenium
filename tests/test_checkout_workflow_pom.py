from pages.login_page import LoginPage


def test_checkout_workflow(driver):
    # Login
    inventory_page = (
        LoginPage(driver)
        .open()
        .login("standard_user", "secret_sauce")
    )

    # Capture item name before adding
    first_item_name = inventory_page.get_first_item_name()

    # Add to cart and verify badge
    inventory_page.add_item_to_cart()
    assert inventory_page.get_cart_count() == "1"

    # Go to cart
    cart_page = inventory_page.go_to_cart()
    assert cart_page.get_cart_items_count() == 1
    assert first_item_name in cart_page.get_cart_item_name_by_index(0)

    # Checkout
    checkout_page = cart_page.proceed_to_checkout()
    confirmation_page = (
        checkout_page
        .fill_details("Abhi", "Sarma", "78541")
        .continue_to_summary()
        .finish_order()
    )

    assert confirmation_page.get_confirmation_header() == "Thank you for your order!"
