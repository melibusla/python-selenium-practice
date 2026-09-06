import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

options = webdriver.FirefoxOptions()
# The system Firefox command is a snap launcher, not the executable Selenium needs.
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
driver = webdriver.Firefox(
    service=Service("/snap/bin/geckodriver"),
    options=options,
)
driver.implicitly_wait(2)
# driver.get("https://the-internet.herokuapp.com/iframe")
# SITE IS NO LONGER ACCESSIBLE
# driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.ID, "tinymce").clear()
# driver.find_element(By.ID, "tinymce").send_keys("Hello Frames")
# driver.switch_to.default_content()
# print(driver.find_element(By.CSS_SELECTOR, "h3").text)
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
driver.switch_to.frame("courses-iframe")
text = driver.find_element(By.CSS_SELECTOR, "div.header-text h2 span").text
print(text)

driver.switch_to.default_content()

time.sleep(2)
driver.quit()