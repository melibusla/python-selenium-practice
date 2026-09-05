import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
# The system Firefox command is a snap launcher, not the executable Selenium needs.
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
driver = webdriver.Firefox(
    service=Service("/snap/bin/geckodriver"),
    options=options,
)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
#grabs all the windows that are opened in a list
windowsOpened = driver.window_handles
#0 index is the main page/parent window and 1 is the new opened one/child window

#switch to the child window
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
#close the child window
driver.close()
#switch back to the parent window
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text

time.sleep(2)
driver.quit()