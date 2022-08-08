from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.get('admin:pass@192.168.1.1')

time.sleep(2)

closeSpam = browser.find_element(By.ID, 'armor_close')

closeSpam.click()

time.sleep(1)

advanced = browser.find_element(By.ID, 'AdvanceTab')

advanced.click()

time.sleep(2)

setupTab = browser.find_element(By.ID, 'AdminId')

setupTab.click()

time.sleep(1)

settingsMenu = browser.find_element(By.ID, 'config_backup')

settingsMenu.click()

time.sleep(2)

upFile = browser.find_element(By.ID, 'file')

upFile.sendKeys('~/Downloads/NETGEAR_CAX80.CFG')
