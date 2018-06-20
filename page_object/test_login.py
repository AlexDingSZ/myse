import  unittest
from page_object.login_page import  login_page
from ddt import ddt,data,unpack
from page_object.logger import Logger
logger = Logger(logger="test_login").getlog()
@ddt
class test_login(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        logger.info("开始测试")
        test_login_page = login_page()
        test_login_page.driver.get("http://autotest/wordpress/wp-login.php")
        test_login_page.get_ele_user_name().send_keys("admin")
        test_login_page.get_ele_password().send_keys("123456")
        test_welcome_page = test_login_page.login_btn_click()
        logger.info("点击登录")
        pdr = test_welcome_page.driver
        print(pdr)
        ele = test_welcome_page.get_login_name().text
        print(ele)
        self.assertEqual(ele,"admin")

        # abc =  test_login_page.get_element()
        # abc.send_keys("sss")
        # abc.send_keys("ssss")

       # test_login_page.driver.find_element(user_name).send_keys("bbbb")


if __name__ =="__main__":
    unittest.main