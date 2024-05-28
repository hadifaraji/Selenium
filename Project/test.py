from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
import random

driver = webdriver.Chrome()
alert = Alert(driver)
driver.get('https://www.flytoday.ir/')
driver.implicitly_wait(5)

driver.find_element(by=By.CSS_SELECTOR, value=".nav_navButtonRight__WIalm  ").click()
sleep(5)
driver.find_element(by=By.XPATH, value='//*[text()="مبدا"]').click()
sleep(6)
x = driver.find_elements(by=By.CLASS_NAME, value='autocomplete_optionsWrapper__FJAB3')
print(x)
y = random.choice(x)
y.click()
sleep(5)
