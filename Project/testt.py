from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.flytoday.ir/')
driver.implicitly_wait(5)

driver.find_element(by=By.XPATH,  value='//*[@id="deny"]').click()
sleep(5)
