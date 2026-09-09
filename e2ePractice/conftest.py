from pathlib import Path
import sys
import tempfile

try:
    project_root = Path(__file__).resolve().parent.parent
except NameError:
    project_root = Path.cwd()

sys.path.insert(0, str(project_root))

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    # Permite elegir el navegador desde la línea de comandos:
    # pytest --browser_name=chrome
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")

        # Usamos una sesión privada para evitar que Chrome recuerde credenciales,
        # popups de password manager o estado viejo de la última ejecución.
        chrome_options.add_argument("--incognito")

        # Desactivamos avisos del Password Manager que pueden bloquear la automatización.
        chrome_options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordLeakDetection")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        })

        # Cada prueba corre con un perfil temporal limpio.
        chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp(prefix='selenium-chrome-')}")

        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = "/home/melina/.local/firefox/firefox"
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Firefox(
            options=firefox_options,
            service=Service(executable_path="/home/melina/.local/bin/geckodriver")
        )
    else:
        raise ValueError(f"Browser not supported: {browser_name}")

    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.quit()
