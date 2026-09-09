from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    #Collect all veggie names in a list
    #if there is no plugin, in dev tools console type for xpath $x("//tr/td[1]")
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in veggieWebElements:
        browserSortedVeggies.append(ele.text)
    #Save a copy of the list with copy()(faster) or slice()
    originalBrowserSortedVeggies = browserSortedVeggies.copy()
    #Sort the original list
    browserSortedVeggies.sort()
    #Compare and verify the list is sorted
    assert browserSortedVeggies == originalBrowserSortedVeggies
