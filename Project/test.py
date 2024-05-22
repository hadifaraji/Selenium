from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://dev02.flytoday.ir/")
driver.find_element('xpath', "//*[text()='ورود']").click()
driver.find_element('xpath', "//*[@name = 'emailOrMobile']").send_keys('09356671285')
driver.find_element('xpath', "//*[text()='ادامه']").click()
driver.find_element('xpath', "//*[@name='pass']").send_keys('Aa123456')
sleep(0.5)
driver.find_element('xpath', "//*[text()='ورود' and @type='primary']").click()
sleep(0.5)
driver.find_element('xpath', "//*[text()='ویزا']").click()
sleep(5)
driver.find_element('xpath' , "//*[text()='ویزا توریستی']").click()
sleep(5)
driver.execute_script('window.scrollTo(0,100)')
sleep(4)
x = driver.find_elements('xpath', "//*[@class='itinerary-list_itineraryList__5CLVr']")[0].click()
sleep(5)
