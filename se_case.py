from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains


def login():
    os.system("taskkill /im chromedriver.exe /f")
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome("D:\\pycode\\Selenium_python3_framework\\tools\\chromedriver.exe")
    driver.get("http://autotest/wordpress/wp-login.php?loggedout=true")
    driver.find_element_by_id("user_login").send_keys("admin")
    driver.find_element_by_id("user_pass").send_keys("123456")
    driver.find_element_by_id("wp-submit").click()
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//span[@class='display-name']")).perform()
    driver.find_element_by_css_selector("#wp-admin-bar-logout > a").click()
    driver.quit()

login()
