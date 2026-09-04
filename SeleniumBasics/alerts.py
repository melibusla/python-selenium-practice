import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name = "Mel"

# Selenium 4 can usually locate ChromeDriver automatically on Linux/macOS.
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
#change from browser to alert mode
alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText
alert.accept()
#cancel
# alert.dismiss()

time.sleep(2)
driver.quit()