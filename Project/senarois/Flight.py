from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Project.modules.click_on_city import City

driver = webdriver.Chrome()
driver.get('https://flytoday.ir/')
driver.implicitly_wait(10)
click_on_flight = driver.find_element(by=By.XPATH, value="//*[text()='پرواز']").click()
sleep(2)
City(driver).click_on_city_in_flight_source(By, sleep)
City(driver).click_on_city_in_flight_destination(By, sleep)
departure_date = driver.find_element(by=By.XPATH, value='//*[text()="تاریخ رفت"]').click()
sleep(2)
date_list_of_day = driver.find_elements(by=By.XPATH, value='//*[@class="day_day__G5CoD"]')
print(len(date_list_of_day))




