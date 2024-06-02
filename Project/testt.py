from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Project.modules.date_of_login import Date


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
for i in range(10):
    no_result = driver.find_element(By.XPATH, "//*[@class='text-primary-black fw-bold tw-mb-6 text-center  fs-4 ']").get_attribute('class')
    no_result == 'text-primary-black fw-bold tw-mb-6 text-center  fs-4 '
    try:
            change_search = driver.find_element(By.XPATH, "//*[text()='تغییر جستجو']").click()
            sleep(2)
            Date(driver).departure_date_in_flight(By, sleep)
            click_on_search = driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
            sleep(20)
    except:
            Date(driver).departure_date_in_flight(By, sleep)
            click_on_search = driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
            sleep(20)
    i += 1
driver.find_element(By.XPATH, "//*[text()='جزئیات و خرید']").click()
sleep(5)
