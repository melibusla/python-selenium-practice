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

# Xpath //tagname [@attribute = 'value'] => //input[@type= 'submit']
# CSS tagname[attribute='value'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#lee el mensaje de exito
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello!")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(5)
driver.quit()