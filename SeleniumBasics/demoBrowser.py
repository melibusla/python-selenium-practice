import time

from selenium import webdriver

#Chrome driver service
driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)



time.sleep(2)