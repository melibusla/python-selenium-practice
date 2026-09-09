import pytest
from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage


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
def test_carousel_image_is_placeholder_not_broken(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login()

    assert not shop_page.is_carousel_image_broken(), "La imagen del carrusel está rota."
    assert shop_page.is_carousel_image_placeholder(), "Se esperaba un placeholder, pero parece una imagen real"