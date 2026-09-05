import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Selenium 4 can usually locate ChromeDriver automatically on Linux/macOS.
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")

#hover, long press, double click, right click
action = ActionChains(driver)
# action.double_click(driver.find_element(By.ID, "displayed-text"))
# action.context_click(driver.find_element(By.ID, "displayed-text"))
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#right click
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

driver.quit()