# مرحله دوم
# برای هر صفحه یک کلاس مجزا ایجاد می کنیم و تست کیس ها یا تست متدها در این کلاس قرار میگیرند که در اینجا صفحه لاگین میشه
# class B     senarois or TestMethod

from Page_Object_Model__POM.Pages.Login import Login
from selenium import webdriver
from time import sleep
# مرحله سوم
from Page_Object_Model__POM.Pages.MainPage import MainPage
# مرحله چهارم
# در فایل های تست به صورت کلی دوتا بخش داریم setup و teardown
# setup
# دراینجا آماده سازی محیط برای تست روانجام می دهیم و بخش اصلی تست است کهassersion,validationومابقی موارداست رومی نویسیم
# suit_setup or class_setup
# فقط یک بار قبل از همه تست کیس ها اجرا می شود یعنی اگر 100تا تست کیس داشته باشیم 1بار قبلش اجرا میشه
# test_setup
# قبل از هر تست کیس یکبار اجرا می شود یعنی اگر 100تا تست کیس داشته باشیم 100بار اجرا می شود
# teardown
# در اینجا تمام تغییرات که تست داشته در دیتابیس یا جاهای دیگه بر می گردانیم
# سشن کلی تست هم می بندیم یعنی درایور رو ()close و ()quit می کنیم تا بعدا مجدد بتوانیم تست های دیگه رو اجرا کنیم
# suit_teardown or class_teardown
# فقط یک بار بعد از همه تست کیس ها اجرا می شود یعنی اگر 100تا تست کیس داشته باشیم 1بار بعدش اجرا میشه
# test_teardown
# بعد از هر تست کیس یکبار اجرا می شود یعنی اگر 100تا تست کیس داشته باشیم 100بار اجرا می شود
import unittest


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def valid_login_test(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        login.username_textbox_id('Admin')
        login.password_textbox_id('admin123')
        login.click_on_login_botton()
        main_page.check_main_page()
        sleep(4)

    def invalid_login_test(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        login.username_textbox_id('Admin')
        login.password_textbox_id('admin1234')
        login.click_on_login_botton()
        main_page.check_main_page()
        sleep(4)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()



