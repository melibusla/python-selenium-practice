#pytest -m smoke //tagging
#pytest -n 10 // pytest-xdist plugin to run parallel tests
import json
from pathlib import Path

import pytest
from e2ePractice.pageObjects.login import LoginPage

test_data_path = Path(__file__).parent / "data" / "test_e2eTestFramework.json"
with test_data_path.open() as f:
    test_data = json.load(f)
    test_list = test_data["data"]

#parametrize the test with the data from the JSON file, it expects a list of dictionaries, each dictionary representing a set of test data
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    login_page.getTitle()
    print(f"Title of the page: {login_page.getTitle()}")
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(f"Title of the page after login: {shop_page.getTitle()}")
    checkout_confirmation = shop_page.goToCart()
    print(f"Title of the page after going to cart: {checkout_confirmation.getTitle()}")
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

@pytest.mark.parametrize("test_list_item", [test_list[0]])
def test_carousel_image_is_placeholder_not_broken(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    login_page.getTitle()
    print(f"Title of the page: {login_page.getTitle()}")
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    print(f"Title of the page after login: {shop_page.getTitle()}")
    assert not shop_page.is_carousel_image_broken(), "La imagen del carrusel está rota."
    assert shop_page.is_carousel_image_placeholder(), "Se esperaba un placeholder, pero parece una imagen real"

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", [test_list[0]])
def test_product_images_are_not_broken(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    login_page.getTitle()
    print(f"Title of the page: {login_page.getTitle()}")
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    print(f"Title of the page after login: {shop_page.getTitle()}")
    imagenes = shop_page.get_product_images()
    assert len(imagenes) > 0, "No se encontraron imágenes de productos"

    for imagen in imagenes:
        src = imagen.get_attribute("src")
        assert not shop_page.is_image_broken(imagen), f"Imagen rota: {src}"