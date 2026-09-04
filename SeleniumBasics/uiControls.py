import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Selenium 4 can usually locate ChromeDriver automatically on Linux/macOS.
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")

# Dynamic checkboxes
# in case there is no id value nor name
# Save all the checkboxes in a variable and iterate to find the correct one
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# Same way for radiobuttons
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

# alternative with css but with a fixed list of radiobuttons
radiobuttons2 = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons2[2].click()
assert radiobuttons2[2].is_selected()

# Check if an element is displayed or hidden
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
# negation in assertion
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


time.sleep(2)
driver.quit()