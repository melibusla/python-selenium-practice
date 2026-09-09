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
def test_product_images_are_not_broken(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login()

    imagenes = shop_page.get_product_images()
    assert len(imagenes) > 0, "No se encontraron imágenes de productos"

    for imagen in imagenes:
        src = imagen.get_attribute("src")
        assert not shop_page.is_image_broken(imagen), f"Imagen rota: {src}"