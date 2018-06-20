from page_object.base_page import  base_page
from selenium.webdriver.common.by import By
from page_object.welcome_page import  welcome_page


class login_page(base_page):
    user_name = (By.ID,"user_login")
    password=(By.ID,"user_pass")
    btn = (By.ID,"wp-submit")

    def __init__(self, driver=None):
        base_page.__init__(self, driver)

    def get_ele_user_name(self):
        return self.get_element(*self.user_name)

    def get_ele_password(self):
        return self.get_element(*self.password)

    def login_btn_click(self):
        self.get_element(*self.btn).click()
        return welcome_page(self.driver)



