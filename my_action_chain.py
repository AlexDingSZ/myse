from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec

import  os
os.system("taskkill /im chromedriver.exe /f")
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
ec.title_is()

driver.find_element_by_class_name("input").send_keys("admin")

driver.find_element_by_css_selector("#user_pass").send_keys("123456")

button = driver.find_element_by_xpath("//input[@id='wp-submit']")
ActionChains(driver).double_click(button).perform()

