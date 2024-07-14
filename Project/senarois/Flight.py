from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Project.modules.click_on_city import City
from Project.modules.date_of_login import Date

driver = webdriver.Chrome()
driver.get('https://flytoday.ir/')
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to.frame('webpush-onsite')
driver.find_element(by=By.XPATH, value='//*[@id = "deny"]').click()
click_on_flight = driver.find_element(by=By.XPATH, value="//*[@id='back-to-top-anchor']/header/div/div[1]/nav/div/div/a[1]/button").click()
sleep(2)
City(driver).click_on_city_in_flight_source(By, sleep)
City(driver).click_on_city_in_flight_destination(By, sleep)
Date(driver).departure_date_in_flight(By, sleep)
click_on_search = driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
sleep(10)









