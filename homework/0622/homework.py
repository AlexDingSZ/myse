from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import  os
os.system("taskkill /im chromedriver.exe /f")
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")

#driver.find_element_by_id("user_login").send_keys("admin")
driver.find_element_by_class_name("input").send_keys("admin")
#driver.find_element_by_name("pwd").send_keys("123456")
driver.find_element_by_css_selector("#user_pass").send_keys("123456")
driver.find_element_by_xpath("//input[@id='wp-submit']").click()
driver.find_element_by_xpath("//div[.='文章']").click()

driver.find_element_by_xpath("//a[.='写文章']").click()
driver.find_element_by_id("title").send_keys("mytest")
driver.find_element_by_id("content").send_keys("testtest")
driver.find_element_by_id("publish").click()
# frame = driver.find_element_by_id("content_ifr")
# driver.switch_to.frame(frame)
# driver.find_element_by_id("tinymce").send_keys("hhahahah")
# driver.switch_to.default_content()
#driver.find_element_by_id("publish").click()
#driver.find_element_by_id("original_publish").click()
#driver.find_element_by_id("publishing-action").click()
#driver.execute_script('var  a = document.getElementById("publish"); a.click()')
#driver.execute_script('var  a = document.getElementById("publish"); a.click()')
#driver.execute_script('$(#publish)[0].click()')


#driver.find_element_by_partial_link_text(u"更换主题").click()
#driver.find_element_by_partial_link_text(u"换主题").click()
#driver.find_element_by_x1path("//button[@class='button button-primary customize-theme']").click()
#//button[@class='button button-primary customize-theme']

#driver.find_element_by_xpath("//button[@class='button button-primary customize-theme']").click()

#driver.find_element_by_xpath("//button[@class='button button-primary customize-theme']").click()
