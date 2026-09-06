import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedProducts = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []

#time.sleep = it waits the full set of seconds
#Implicit = global timeout with a parameter of max wait, if it takes less time, it will proceed. ie driver.implicitly_wait(5). It applies to all the lines
#Explicit = target one element and apply the seconds only to that step

# Selenium 4 can usually locate ChromeDriver automatically on Linux/macOS.
driver = webdriver.Chrome()

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
# a time.sleep is added here because otherwise the list would be empty, it only validates that it exists

#find and count the products
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
# verify there are results
assert count > 0
# run through the results and click "add to cart"
for result in results:
    #chaining elements. It's like sending "//div[@class='products']/div/div/button" but "//div[@class='products']/div" is already in the var 'results'.
    #alternative path for comparing lists
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

#Grab the results and check if the text matches
# products = driver.find_elements(By.CSS_SELECTOR, ".product-name")
# print(products)
assert expectedProducts == actualList

#click the cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    #convert the str to int
    sum = sum + int(price.text)

# print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

#add promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#Add an explicit wait for promo code to apply
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
#check confirmation of promo code
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# validating that Total after Discount is less than total amount
discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discountAmount < totalAmount











driver.quit()