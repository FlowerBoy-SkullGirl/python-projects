from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4

browser = webdriver.Firefox()

browser.get('https://www.bestbuy.com')

#time.sleep(1)

#elementTarget = browser.find_element(By.CLASS_NAME, 'shop-account-menu')

#elementTarget.click()

#time.sleep(1)

#elementSignIn = browser.find_element(By.PARTIAL_LINK_TEXT, 'Sign In')

#elementSignIn.click()

#time.sleep(1)

#elementUser = browser.find_element(By.NAME, 'fld-e')

#elementUser.click()

#elementUser.send_keys('user@gmail.com')

#time.sleep(1)

#elementPass = browser.find_element(By.NAME, 'fld-p1')

#elementPass.click()

#elementPass.send_keys('pass')

#elementPass.submit()

#time.sleep(2)

#elementEmp = browser.find_element(By.ID, 'employeeNumber')

#elementEmp.send_keys('num')

#elementEmp.submit()

time.sleep(2)

elementSearch = browser.find_element(By.ID, 'gh-search-input')

elementSearch.send_keys('graphics card')

elementSearch.submit()

time.sleep(5)

listEntries = browser.find_elements(By.CLASS_NAME, "sku-item")
elementPrice = browser.find_elements(By.XPATH, "//div[@class='priceView-hero-price priceView-customer-price']//span[1]")


for i in range(len(listEntries)):

#	elementName = listEntries[i].find_element(By.XPATH, "//h4[@class='sku-title']//a[1]")
	elementName = listEntries[i].find_element(By.CLASS_NAME, "sku-title")
	elementName = elementName.find_element(By.XPATH, "a[1]")

	print("piping data")

	print(elementName.text)

#	elementPrice = listEntries[i].find_element(By.XPATH, "div[@class='priceView-hero-price priceView-customer-price']//span[1]")

	print(elementPrice[i].text)

print ("end signal")

browser.close()

#SOUP PLAN
# gpus = soup.select('class name')
# for i in range(len(gpus))
#      gpus[i].get('a')
#Something like this to get all results on page
#Can maybe do this with selenium too
# elements = browser.find_elements(By.ID 'gh-blabla')
# for i in range(len(elements
