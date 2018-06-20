from page_object.base_page import  base_page
from selenium.webdriver.common.by import By

class welcome_page(base_page):
    login_name = (By.XPATH,"//*[@id='wp-admin-bar-my-account']/a/span")

    def __init__(self, driver=None):
        base_page.__init__(self, driver)

    def get_login_name(self):
        return self.get_element(*self.login_name)