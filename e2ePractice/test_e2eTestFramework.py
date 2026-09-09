import json

import pytest
from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
test_data_path = "data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

#parametrize the test with the data from the JSON file, it expects a list of dictionaries, each dictionary representing a set of test data
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])

    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

@pytest.mark.parametrize("test_list_item", [test_list[0]])
def test_carousel_image_is_placeholder_not_broken(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])

    assert not shop_page.is_carousel_image_broken(), "La imagen del carrusel está rota."
    assert shop_page.is_carousel_image_placeholder(), "Se esperaba un placeholder, pero parece una imagen real"

@pytest.mark.parametrize("test_list_item", [test_list[0]])
def test_product_images_are_not_broken(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])

    imagenes = shop_page.get_product_images()
    assert len(imagenes) > 0, "No se encontraron imágenes de productos"

    for imagen in imagenes:
        src = imagen.get_attribute("src")
        assert not shop_page.is_image_broken(imagen), f"Imagen rota: {src}"