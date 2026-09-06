from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")  # en versiones nuevas se recomienda con doble guion
chrome_options.add_argument("--no-sandbox")  # casi obligatorio en Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # evita crashes por memoria compartida limitada
chrome_options.add_argument("--ignore-certificate-errors") #Bypass SLL certificate
#chrome_options.add_argument("--window-size=360,640")

# Recent Chrome versions may no longer include "Pixel 5" in their built-in
# device list, so define the device metrics explicitly.
# chrome_options.add_experimental_option(
#     "mobileEmulation",
#     {
#         "deviceMetrics": {
#             "width": 393,
#             "height": 851,
#             "pixelRatio": 3.0,
#             "mobile": True,
#         }
#     },
# )
#iphone 17 dimensions
chrome_options.add_experimental_option(
    "mobileEmulation",
    {
        "deviceMetrics": {
            "width": 402,
            "height": 874,
            "pixelRatio": 3.0,
            "mobile": True,
        }
    },
)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)


driver.quit()