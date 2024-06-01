import random


class Date:

    def __init__(self, driver):
        self.driver = driver

    def departure_date_in_flight(self, By, sleep):
        departure_date = self.driver.find_element(by=By.XPATH, value='//*[text()="تاریخ رفت"]').click()
        sleep(2)
        date_list_of_day = self.driver.find_elements(by=By.XPATH, value='//*[@class="day_day__G5CoD"]')
        count_of_date = len(date_list_of_day)
        enable_day = []
        for i in range(count_of_date):
            if date_list_of_day[i].is_enabled():
                enable_day.append(date_list_of_day[i])
            else:
                None
        chiose_random = random.choice(enable_day)
        chiose_random.click()
        sleep(6)
        click_on_approve = self.driver.find_element(by=By.XPATH, value='//*[text()="تائید"]').click()
        sleep(2)