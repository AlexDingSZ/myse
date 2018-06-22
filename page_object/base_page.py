from selenium import webdriver
import  os
from page_object.logger import Logger
import time

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

    def wait_element(self,*locator):
        ele = None
        count = 0
        while ele is None:
            count = count + 1
            try:
                ele = self.driver.find_element(*locator)
            except:
                pass
            flag = ele is not None
            logger.info("查找元素第%d次 %s %s " % (count,flag,str(locator)))
            time.sleep(0.1)
            if count > 99:
                logger.info("没有找到元素 %s" % str(locator))
                break
        return ele
