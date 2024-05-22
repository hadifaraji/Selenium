from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://www.yahoo.com/'
driver.get(url)
driver.execute_script('window.scrollTo(0,100)')
sleep(4)