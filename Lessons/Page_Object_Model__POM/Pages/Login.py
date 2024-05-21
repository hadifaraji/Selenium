# مرحله اول
# هنگامی که از کلاس یک نمونه ایجاد میکنیم میاد دستورات یا فانکشن هایی که داخل کلاس نوشتیم رو اجرا میکنه
# در اصل به دستورات یا فانکشن داخل کلاس conestractor میگیم
# class A    Webelement + Method
# بین import ها و کلاس ها باید دوتا فاصله بدیم   ctrl + alt + l

from Page_Object_Model__POM.Locators import username_textbox_id, password_textbox_id, login_botton_id


class Login:
    def __int__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', password_textbox_id).send_keys(password)

    def click_on_login_botton(self):
        self.driver.find_element('id', login_botton_id).click()
