from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-admin/")
driver.find_element_by_id("user_login").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("123456")
driver.find_element_by_xpath("//*[@id='wp-submit']").click()
driver.find_element_by_xpath("//*[@id='menu-posts']/a/div[3]").click()
driver.find_element_by_xpath("//*[@id='menu-posts']/ul/li[3]/a").click()
driver.find_element_by_id("title").send_keys("获取元素发表文章")
time.sleep(3)
#driver.find_element_by_id("content_ifr").send_keys("  获取元素发表文章，这是第一篇文章-lm")
driver.find_element_by_id("content").send_keys("  获取元素发表文章，这是第一篇文章-lm")

time.sleep(5)
driver.find_element_by_xpath("//*[@id='publish']").click()
driver.find_element_by_xpath("//*[@id='menu-posts']/ul/li[2]/a").click()
driver.close()
