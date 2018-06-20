from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

os.system("taskkill /im chromedriver.exe /f")
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
title = ec.title_is(u"登录 ‹ autotest — WordPress")
print(title(driver))

driver.find_element_by_class_name("input").send_keys("admin")
driver.find_element_by_css_selector("#user_pass").send_keys("123456")
WebDriverWait(driver,30).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='wp-submit']"))).click()






