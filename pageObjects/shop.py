from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.checkout_confirmation import CheckoutConfirmationPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Esperamos a que la navegación principal esté lista antes de interactuar con la UI.
        self.shop_link = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='shop']"))
        )

        # La lista de productos se re-evalúa cada vez para evitar referencias stale tras la navegación.
        self.products_cards = self._get_products()

        # El botón del carrito también se espera visible/clickable porque puede tardar en renderizar.
        self.cart_link = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[class*='btn-primary']"))
        )

    def _get_products(self):
        return self.wait.until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'card h-100')]"))
        )

    def add_product_to_cart(self, product_name):
        self.shop_link.click()

        while True:
            products = self._get_products()
            for product in products:
                try:
                    product_title = product.find_element(By.XPATH, ".//h4/a").text
                except StaleElementReferenceException:
                    break

                if product_title.strip() == product_name:
                    product.find_element(By.XPATH, ".//button").click()
                    return
            else:
                return

    def goToCart(self):
        cart_link = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[class*='btn-primary']"))
        )

        try:
            cart_link.click()
        except ElementClickInterceptedException:
            # Fallback de compatibilidad con la UI actual del sitio.
            self.driver.execute_script("arguments[0].click();", cart_link)

        checkout_confirmation = CheckoutConfirmationPage(self.driver)
        return checkout_confirmation
