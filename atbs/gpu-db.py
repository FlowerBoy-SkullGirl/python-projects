from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
from selenium.webdriver.common.action_chains import ActionChains

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
time.sleep(3)

while True:
	try:
		elementNext = browser.find_element(By.CLASS_NAME, 'sku-list-page-next')
	except:
		break

#try:
#elementNext = browser.find_element(By.CLASS_NAME, 'sku-list-page-next')
#except:
#break
#elementNext.click()
	time.sleep(5)

	try:
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
		try:
			elementNext = browser.find_element(By.CLASS_NAME, 'sku-list-page-next')
		#actions = ActionChains(browser)
		#print("Made action chain")
		#actions.move_to_element(elementNext).perform()
		#print("Scrolled to element")
			time.sleep(0.5)
			browser.execute_script("arguments[0].scrollIntoView(true);", elementNext)
			time.sleep(0.5)
			browser.execute_script("window.scrollBy(1000,-150);")
			time.sleep(0.8)
			elementNext.click()
		except:
			break
	except:
		break

print ("end signal")
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
