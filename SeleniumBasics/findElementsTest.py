import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Selenium 4 can usually locate ChromeDriver automatically on Linux/macOS.
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
len(countries)
# print(len(countries))
for country in countries:
    # print(country.text)
    if country.text == "India":
        country.click()
        break

#to get text that was generated dynamically, the text did not exist when landing in the page
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"







time.sleep(2)
driver.quit()