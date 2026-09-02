import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium 4 can usually locate ChromeDriver automatically on Linux/macOS.
driver = webdriver.Chrome()

driver.get("http://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CssSelector, Classname, name, linkText

driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID, "exampleCheck1").click()

time.sleep(5)
driver.quit()