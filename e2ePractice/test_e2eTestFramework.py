import pytest
from pageObjects.login import LoginPage


def test_e2e(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login()

    shop_page.add_product_to_cart("Blackberry")
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
