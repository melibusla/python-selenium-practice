from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.shop import ShopPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Guardamos los elementos del formulario una vez para que la clase sea simple de reutilizar.
        self.username_input = driver.find_element(By.ID, "username")
        self.password_input = driver.find_element(By.ID, "password")
        self.sign_in_button = driver.find_element(By.ID, "signInBtn")

    def login(self, username="rahulshettyacademy", password="Learning@830$3mK2"):
        # Antes de cada login limpiamos los inputs para evitar valores viejos o estados inconsistentes.
        self.username_input.clear()
        self.password_input.clear()

        self.username_input.send_keys(username)
        self.password_input.send_keys(password)

        # En este sitio el click nativo puede quedar bloqueado por overlays o popups del navegador.
        # Hacemos click vía JavaScript para que la automatización sea más estable.
        self.driver.execute_script("arguments[0].click();", self.sign_in_button)

        wait = WebDriverWait(self.driver, 15)
        wait.until(
            lambda driver: "shop" in driver.current_url or driver.find_elements(By.CSS_SELECTOR, "a[href*='shop']")
        )

        shop_page = ShopPage(self.driver)
        return shop_page
