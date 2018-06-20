from selenium import webdriver
from selenium.webdriver.common.keys import  k
import os
os.system("taskkill /im chromedriver.exe /f")
driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")

driver.execute_script('document.getElementById("user_login").value="admin"')
driver.execute_script('document.getElementById("user_pass").value="123456"')
driver.execute_script('a = document.getElementById("wp-submit"); a.click()')

