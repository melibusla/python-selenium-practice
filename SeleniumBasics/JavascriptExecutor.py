import time

from selenium import webdriver

#Headless mode: tests run in invisible/silent mode. It is faster
#Head mode: see browser in action

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # en versiones nuevas se recomienda con doble guion
chrome_options.add_argument("--no-sandbox")  # casi obligatorio en Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # evita crashes por memoria compartida limitada
chrome_options.add_argument("--ignore-certificate-errors") #Bypass SLL certificate

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
# javascript script
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# screenshot
driver.get_screenshot_as_file("screen.png")
driver.execute_script("window.scrollBy(0,500);")


time.sleep(2)
driver.quit()