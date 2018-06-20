from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome()
driver.get(r"C:\Users\Administrator\PycharmProjects\myse\select.html")
#driver.find_element_by_xpath("//option[@value='saab']").click()
select = driver.find_element_by_name("cars")
select.find_element_by_xpath("//option[@value='saab']").click()
driver.quit()