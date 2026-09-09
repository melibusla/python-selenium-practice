# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

#Run with
# cd /home/melina/selenium_project/e2ePractice
# python3 -m pytest test_e2eTestFramework.py --browser_name firefox

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="Chrome", help="browser selection")

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = "/home/melina/.local/firefox/firefox"
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(
            options=firefox_options,
            service=Service(executable_path="/home/melina/.local/bin/geckodriver")
        )

    driver.implicitly_wait(4)
    yield driver