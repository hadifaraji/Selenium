from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.flytoday.ir/')
sleep(5)
x = driver.switch_to.alert.dismiss()
sleep(2)