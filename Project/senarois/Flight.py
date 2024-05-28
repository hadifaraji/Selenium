from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.flytoday.ir/')
sleep(5)
click_on_flight = driver.find_element(by=By.CSS_SELECTOR, value='.nav_navButtonRight__WIalm  ').click()
click_on_source = driver.find_element(by=By.XPATH, value="//*[text()='مبدا']").click()
sleep(2)
get_list_city = driver.find_elements(by=By.XPATH, value="//*[@class='autocomplete_optionsWrapper__FJAB3' ]//*[@role='button']")
print(get_list_city)
