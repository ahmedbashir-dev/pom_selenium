from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_checkout(driver):
    wait = WebDriverWait(driver, 10)

    # --- Page 1: Login ---
    driver.get("https://saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # --- Page 2: Inventory Page ---
    wait.until(EC.url_contains("inventory"))
    # Pick the first product name, so that we can verify it later in the cart
    first_product_name = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").text

    # Click add to cart for the first item
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert badge.text == "1"

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() # go to cart

    # --- Page 3: Cart Page ---
    wait.until(EC.url_contains("cart"))

    # Verify that item is in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1
    assert first_product_name in cart_items[0].text

    # Proceed to checkout
    driver.find_element(By.ID, "checkout").click()

    # --- Page 4: Checkout Form step -1 ---
    wait.until(EC.url_contains("checkout-step-one"))
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("78541")
    driver.find_element(By.ID, "continue").click()

    # --- Page 4(b): Order Summary
    wait.until(EC.url_contains("checkout-step-two"))
    summary_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert first_product_name in summary_items[0].text
    driver.find_element(By.ID, "finish").click()

    # --- Page 5: Confirmation Page ---
    wait.until(EC.url_contains("checkout-complete"))
    confirm_header = driver.find_element(By.CLASS_NAME, "complete-header")
    assert confirm_header.text == "Thank you for your order!"

