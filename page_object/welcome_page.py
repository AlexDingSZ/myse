from page_object.base_page import  base_page
from selenium.webdriver.common.by import By

class welcome_page(base_page):
    #login_name = (By.XPATH,"//*[@id='wp-admin-bar-my-account']/a/span")
    login_name = (By.XPATH,"//*[@id='wp-admin-bar-my-account']/a/span")

    #logout=(By.XPATH,"//a[.='登出']")
    logout=(By.CSS_SELECTOR,"#wp-admin-bar-logout > a")

    def __init__(self, driver=None):
        base_page.__init__(self, driver)

    def get_ele_login_name(self):
        return self.get_element(*self.login_name)

    def get_ele_logout(self):
        return self.wait_element(*self.logout)

   # ActionChains(driver).move_to_element(driver.find_element_by_xpath("//span[@class='display-name']")).perform()
   # driver.find_element_by_css_selector("#wp-admin-bar-logout > a").click()