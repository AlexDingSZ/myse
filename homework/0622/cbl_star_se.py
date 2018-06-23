#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# Author:Luke chen

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://autotest/wordpress/wp-login.php")
driver.find_element_by_id("user_login").send_keys("admin")
time.sleep(0.3)
driver.find_element_by_name("pwd").send_keys("123456")
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='wp-submit']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='menu-posts']/a").click()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='wpbody-content']/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='title']").send_keys("title")
driver.find_element_by_xpath("//*[@id='publish']").click()
