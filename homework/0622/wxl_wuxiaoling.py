from selenium import webdriver
import  os
import  time
os.system("taskkill /im chromedriver.exe /f")
driver=webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
driver.find_element_by_id("user_login").send_keys("admin")
time.sleep(1)
driver.find_element_by_name("pwd").send_keys("123456")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='wp-submit']").click()
time.sleep(1)
driver.get("http://autotest/wordpress/wp-admin/post-new.php")
driver.find_element_by_xpath("//*[@id='title']").send_keys(u"这是一篇文章")
driver.find_element_by_id("content").send_keys(u"这是一篇很短的文章，今天是2018年6月21日，所以hello world！")
driver.find_element_by_id("submitpost").find_element_by_id("publish").click()
time.sleep(2)
driver.find_element_by_id("mceu_24").click()
driver.switch_to.frame(driver.find_element_by_id("content_ifr"))
driver.find_element_by_id("tinymce").send_keys(u"这是一篇很短的文章，今天是2018年6月21日，所以hello world！")
driver.switch_to.default_content()
time.sleep(3)
driver.find_element_by_id("submitpost").find_element_by_id("publish").click()




