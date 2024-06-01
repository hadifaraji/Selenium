import random


class City:

    def __init__(self, driver):
        self.driver = driver

    def click_on_city_in_flight_source(self, By, sleep):
        click_on_source = self.driver.find_element(by=By.XPATH, value='//*[text()="مبدا"]').click()
        sleep(1)
        get_list_city = self.driver.find_elements(by=By.XPATH, value='//*[@class = "option_autocompleteOption__vJ6SE"]')
        sleep(1)
        choice_by_random = random.choice(get_list_city)
        choice_by_random.click()
        sleep(1)

    def click_on_city_in_flight_destination(self, By, sleep):
        click_on_destination = self.driver.find_element(by=By.XPATH, value='//*[text()="مقصد"]').click()
        sleep(1)
        get_list_city = self.driver.find_elements(by=By.XPATH, value='//*[@class = "option_autocompleteOption__vJ6SE"]')
        sleep(1)
        choice_by_random = random.choice(get_list_city)
        choice_by_random.click()
        sleep(1)