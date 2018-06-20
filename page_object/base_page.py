from selenium import webdriver
import  os
from page_object.logger import Logger

logger = Logger(logger="base_page").getlog()
class base_page(object):
    def __init__(self,driver=None):
        if driver is None:
            os.system("taskkill /im chromedriver.exe /f")
            self.driver = webdriver.Chrome()
            #self.driver.find_element_by_id("a").text()
        else:
            self.driver=driver
        #self.driver.get("http://autotest/wordpress/wp-login.php")

    def get_element(self,*locator):
        logger.info("查找元素 %s" % str(locator))
        return self.driver.find_element(*locator)
