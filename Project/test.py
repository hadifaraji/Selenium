from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random


driver = webdriver.Chrome()
driver.get('https://flytoday.ir/')
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to.frame('webpush-onsite')
driver.find_element(by=By.XPATH, value='//*[@id = "deny"]').click()
click_on_flight = driver.find_element(by=By.XPATH, value="//*[text()='پرواز']").click()
sleep(2)
click_on_source = driver.find_element(by=By.XPATH, value='//*[text()="مبدا"]').click()
sleep(1)
driver.find_element(By.XPATH, "//*[text()='کیش']").click()
click_on_destination = driver.find_element(by=By.XPATH, value='//*[text()="مقصد"]').click()
sleep(1)
driver.find_element(By.XPATH, "//*[text()='شیراز']").click()
departure_date = driver.find_element(by=By.XPATH, value='//*[text()="تاریخ رفت"]').click()
sleep(1)
driver.find_element(By.XPATH, "//*[text()='14']").click()
click_on_approve = driver.find_element(by=By.XPATH, value='//*[text()="تائید"]').click()
sleep(2)
click_on_search = driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
sleep(10)
for i in range(2):
    no_result = driver.find_element(By.XPATH, "//*[@class='text-primary-black fw-bold tw-mb-6 text-center  fs-4 ']").get_attribute('class')
    if no_result == 'text-primary-black fw-bold tw-mb-6 text-center  fs-4 ':
        try:
            change_search = driver.find_element(By.XPATH, "//*[text()='تغییر جستجو']").click()
            sleep(2)
            departure_date = driver.find_element(by=By.XPATH, value='//*[text()="تاریخ رفت"]').click()
            sleep(2)
            driver.find_element(By.XPATH, "//*[text()='15']").click()
            click_on_approve = driver.find_element(by=By.XPATH, value='//*[text()="تائید"]').click()
            sleep(2)
            click_on_search = driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
            sleep(20)
        except:
            departure_date = driver.find_element(by=By.XPATH, value='//*[text()="تاریخ رفت"]').click()
            sleep(2)
            driver.find_element(By.XPATH, "//*[text()='17']").click()
            click_on_approve = driver.find_element(by=By.XPATH, value='//*[text()="تائید"]').click()
            sleep(2)
            click_on_search = driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
            sleep(20)
    else:
        i += 1
raise Exception('page no result')