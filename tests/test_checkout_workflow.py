from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_checkout(driver):
    wait = WebDriverWait(driver, 15)

    # --- Login ---
    driver.get("https://www.saucedemo.com/")
    
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # --- Inventory ---
    wait.until(EC.url_contains("inventory"))

    first_product_name = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text

    # Add to cart
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']"))
    ).click()

    # Verify badge
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1"

    # Go to cart (important wait)
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # --- Cart Page ---
    wait.until(EC.url_contains("cart"))

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1
    assert first_product_name in cart_items[0].text

    # Proceed to checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # --- Checkout Step One ---
    wait.until(EC.url_contains("checkout-step-one"))

    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("78541")
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # --- Checkout Step Two ---
    wait.until(EC.url_contains("checkout-step-two"))

    summary_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert first_product_name in summary_items[0].text

    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # --- Confirmation ---
    wait.until(EC.url_contains("checkout-complete"))
    confirm_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert confirm_header.text == "Thank you for your order!"
