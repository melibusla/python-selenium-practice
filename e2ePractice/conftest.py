import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browserInstance():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(4)
    yield driver