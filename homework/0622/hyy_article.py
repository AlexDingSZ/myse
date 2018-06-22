from selenium import  webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
#登录
driver.find_element_by_id("user_login").send_keys("admin")
driver.find_element_by_id("user_pass").send_keys("123456")
driver.find_element_by_xpath("//input[@type='submit']").click()
#写文章
driver.get("http://autotest/wordpress/wp-admin/post-new.php")

#driver.find_element_by_xpath("//*[@href='http://localhost/wordpress/wp-admin/post-new.php']").click()
driver.find_element_by_name("post_title").send_keys(u"开心")
sleep(1)
#driver.find_element_by_id("content_ifr").send_keys("yep")
driver.find_element_by_id("content").send_keys("yep")
sleep(3)
driver.find_element_by_id("publish").click()
sleep(3)

# driver.quit()