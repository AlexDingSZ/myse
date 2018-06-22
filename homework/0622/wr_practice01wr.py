from selenium import webdriver
import time
import os
from  selenium.webdriver.common.action_chains import ActionChains
os.system("taskkill /im chromedriver.exe /f")       #  /im指进程名称，/f指强制停止
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
driver.find_element_by_xpath("//input[@id='user_login']").send_keys("admin")     #   使用xpath方法定位
time.sleep(1)
driver.find_element_by_id("user_pass").send_keys("123456")       #    使用id定位
time.sleep(1)
checkboxlist  = driver.find_elements_by_class_name("button-large")       #  使用批量class_name定位
for eachcheckbox in checkboxlist:
    if eachcheckbox.is_selected() is False:
        eachcheckbox.click()
time.sleep(2)
driver.find_element_by_partial_link_text("撰写").click()          #    使用超链接text来模糊定位
time.sleep(1)

driver.find_element_by_name("post_title").send_keys(u"自动化测试介绍")
# driver.find_element_by_class_name("switch-html").click()
# driver.find_element_by_class_name("wp-editor-area").send_keys("123")
# time.sleep(1)
# driver.find_element_by_class_name("wp-editor-area").clear()       #   清除输入框
# time.sleep(1)
# driver.find_element_by_class_name("switch-tmce").click()

#driver.find_element_by_id("content_ifr").send_keys(u"         自动化测试一般是指软件测试的自动化，软件测试就是在预设条件下运行系统或应用程序，评估运行结果，预先条件应该包括正常条件和异常条件。")
driver.find_element_by_id("content").send_keys(u"         自动化测试一般是指软件测试的自动化，软件测试就是在预设条件下运行系统或应用程序，评估运行结果，预先条件应该包括正常条件和异常条件。")
time.sleep(2)
#driver.find_element_by_name("publish").click()
#ActionChains(driver).move_to_element(driver.find_element_by_id("publish")).perform()
#driver.execute_script('var  a = document.getElementById("publish"); a.click()')
driver.find_element_by_id("publish").click()
