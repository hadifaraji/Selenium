from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "*[data-test=/"flight-service-landing/"]")