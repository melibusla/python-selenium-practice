from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from e2ePractice.utils.browserUtils import BrowserUtils


class CheckoutConfirmationPage(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
        self.wait = WebDriverWait(driver, 15)

        # En el flujo actual del sitio, el checkout es un botón/enlace con estructura diferente a la del curso.
        self.checkout_button = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//a[contains(., 'Checkout')] | //button[contains(., 'Checkout')]")
            )
        )

    def checkout(self):
        try:
            self.checkout_button.click()  # click normal, como en el curso
        except ElementClickInterceptedException:
            # Fallback de compatibilidad con la UI actual del sitio.
            self.driver.execute_script("arguments[0].click();", self.checkout_button)

        self.wait.until(
            lambda driver: driver.find_elements(By.ID, "country")
            or driver.find_elements(By.XPATH, "//button[contains(., 'Purchase')]")
        )

    def enter_delivery_address(self, country_name):
        # Flujo anterior del curso: country + India + checkbox + submit.
        if self.driver.find_elements(By.ID, "country"):
            country_input = self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "country")))
            country_input.send_keys(country_name)
            self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))
            self.driver.find_element(By.LINK_TEXT, "India").click()
            checkbox = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='checkbox checkbox-primary'] | //input[@type='checkbox']")))
            checkbox.click()
            submit_button = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']")))
            submit_button.click()
            return

        # Flujo actual del sitio: checkbox + Purchase.
        checkbox = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[@type='checkbox' or @name='terms' or contains(@id, 'terms')]")
            )
        )
        checkbox.click()
        purchase_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(., 'Purchase')]"))
        )
        purchase_button.click()

    def validate_order(self):
        success = self.wait.until(
            lambda driver: driver.find_elements(By.CSS_SELECTOR, "div[class*='alert-success']")
            or "Success! Thank you!" in driver.find_element(By.TAG_NAME, "body").text
            or "Thank you" in driver.find_element(By.TAG_NAME, "body").text,
            message="No se encontró el mensaje final de confirmación del pedido."
        )

        if isinstance(success, list):
            success_text = success[0].text
        else:
            success_text = self.driver.find_element(By.TAG_NAME, "body").text

        assert "Success! Thank you!" in success_text or "Thank you" in success_text
