from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Project.modules.click_on_city import City
import random

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
count_of_date = len(date_list_of_day)
enable_day = []
for i in range(count_of_date):
    if date_list_of_day[i].is_enabled():
        enable_day.append(date_list_of_day[i])
    else:
        None
chiose_random = random.choice(enable_day)
chiose_random.click()
sleep(5)
click_on_approve = driver.find_element()




