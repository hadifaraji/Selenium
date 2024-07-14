from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.java.com/en/")
def wait_until_page_successfully_laoded(timeout=10):
    for i in range(timeout * 2):
        try:
            state = driver.execute_script("return document.readyState")
            assert state == 'complete'
            print("page is loaded")
            return
        except:
            sleep(0.5)
            print('Loading...')
wait_until_page_successfully_laoded()
