import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise")

#Instructions
# Go to the page and click the green banner, Free access etc
# In that window, grab the email id from the text, use split, trim
#Copy it and paste in the username of the parent window
# Fill the rest of the fields, and click sign in
#Grab the error message and print it in the output

#Click the banner
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
#Change to the child window
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
#Grab the email
email = driver.find_element(By.CSS_SELECTOR, "a[href='mailto:mentor@rahulshettyacademy.com']").text
print(email)
#Switch back to the parent window
driver.close()
driver.switch_to.window(windowsOpened[0])
#Input the email in the field username
driver.find_element(By.NAME, "username").send_keys(email)
#Fill the rest of the fields and click Sign in
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "signin").click()
#Verify the alert is shown
wait = WebDriverWait(driver, 10)
#tuple
alert_locator = (By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")
#wait until the element exists and contains the text
wait.until(expected_conditions.text_to_be_present_in_element(
    alert_locator, "Incorrect username/password."
))
#* means it will paste the tuple as is, as 2 separate arguments
alert_text = driver.find_element(*alert_locator).text
print(alert_text)
assert "Incorrect username/password." in alert_text

#**********************************
#ALTERNATIVE

# driver.implicitly_wait(4)
#
# driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
# windowsOpened = driver.window_handles
#
# driver.switch_to.window(windowsOpened[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
# driver.close()
# driver.switch_to.window(windowsOpened[0])
# driver.find_element(By.ID, "username").send_keys(var)
# driver.find_element(By.ID, "password").send_keys(var)
# driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)




time.sleep(2)
driver.quit()