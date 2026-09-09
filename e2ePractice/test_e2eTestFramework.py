from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # Go to shop
    # Use regular expressions to tag the name if there is no other option
    # Xpath //a[contains(@href, 'shop')]
    # CSS a[href*='shop']
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    # Scan all the products and iterate
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for product in products:
        # chaining elements
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            # chaining again and click add to cart
            product.find_element(By.XPATH, "div/button").click()
    # Go to cart
    # button is hidden in smaller resolutions
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # Click Checkout
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    # Input delivery location
    driver.find_element(By.ID, "country").send_keys("Ind")
    # Insert a wait for the results to load
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))
    # Click the result
    driver.find_element(By.LINK_TEXT, "India").click()
    # Check the checkbox
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # Click Purchase button
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # Verify the success toast message
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in successText
    print(successText)

    driver.quit()