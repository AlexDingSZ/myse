from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import os
os.system("taskkill /im chromedriver.exe /f")
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
driver.find_element_by_id("user_login").send_keys("admin")
driver.find_element_by_id("user_pass").send_keys("123456")
driver.find_element_by_id("wp-submit").send_keys(Keys.ENTER)



