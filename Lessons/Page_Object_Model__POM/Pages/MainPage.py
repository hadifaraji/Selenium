# مرحله 3
# همانطور که در مرحله 2 گفتیم وقتی وارد سیستم می شویم برای تست کیس های آن صفحه باید یک کلاس جدید ایجاد کنیم
# class C     Webelement or Method

# ستاره میاد کل locator.py هارو میخونه
# الان چون کمه به عنوان نمونه و مثال آوردیم تا معنی * رو بفهمیم
# ولی هنگامی که در آینده پروژه بزرگ تر می شود و locator.py ها زیاد می شود روش مناسبی نیست و ازش استفاده نمی کنیم
# from Locators.py import *
# فقط Locator هایی رو میاریم که در نوشتن کلاسمون بهشون نیاز داریم

from Page_Object_Model__POM.Locators import dashboard_lable_id


class MainPage:
    def __int__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.find_element('id', dashboard_lable_id)