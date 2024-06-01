class Change_Search:

    def __init__(self, driver):
        self.driver = driver

    def change_search_in_flight(self, By, sleep):
        no_result = self.driver.find_element(By.XPATH,"//*[@class='text-primary-black fw-bold tw-mb-6 text-center  fs-4 ']").get_attribute('class')
        if no_result == 'text-primary-black fw-bold tw-mb-6 text-center  fs-4 ':
            change_search = self.driver.find_element(By.XPATH, "//*[text()='تغییر جستجو']").click()
            sleep(2)
            departure_date = self.driver.find_element(by=By.XPATH, value='//*[text()="تاریخ رفت"]').click()
            sleep(1)
            self.driver.find_element(By.XPATH, "//*[text()='16']").click()
            click_on_approve = self.driver.find_element(by=By.XPATH, value='//*[text()="تائید"]').click()
            sleep(2)
            click_on_search = self.driver.find_element(By.XPATH, '//*[text()="جستجو"]').click()
            sleep(10)
        else:
            None
