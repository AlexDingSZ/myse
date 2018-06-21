import  unittest
from page_object.login_page import  login_page
from ddt import ddt,data,unpack
from page_object.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
logger = Logger(logger="test_login").getlog()
@ddt
class test_login(unittest.TestCase):

    t_user = (("admin", "123456"), ("admin", "123456"), ("admin", "123456"))
    test_login_page = login_page()

    def setUp(self):
        pass

    @data(*t_user)
    @unpack
    def test_login(self,name,password):
        logger.info("开始测试")
        self.test_login_page.driver.get("http://autotest/wordpress/wp-login.php")
        self.test_login_page.get_ele_user_name().send_keys(name)
        self.test_login_page.get_ele_password().send_keys(password)
        test_welcome_page = self.test_login_page.login_btn_click()
        logger.info("点击登录")
        pdr = test_welcome_page.driver
        print(pdr)
        ele = test_welcome_page.get_ele_login_name().text
        print(ele)
        self.assertEqual(ele,"admin")
        ActionChains(self.test_login_page.driver).move_to_element(test_welcome_page.get_ele_login_name()).perform()
        test_welcome_page.get_ele_logout().click()


        # abc =  test_login_page.get_element()
        # abc.send_keys("sss")
        # abc.send_keys("ssss")

       # test_login_page.driver.find_element(user_name).send_keys("bbbb")


if __name__ =="__main__":
    unittest.main