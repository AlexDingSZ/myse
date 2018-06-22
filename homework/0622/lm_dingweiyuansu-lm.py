from selenium import webdriver
import time
import  os
os.system("taskkill /im chromedriver.exe /f")
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw")
driver.find_element_by_name("wd")
driver.find_element_by_link_text(u"新闻").click()
driver.find_element_by_partial_link_text("音").click()
driver.find_element_by_xpath("/html/body/div[5]/div[2]/span").click()
driver.find_element_by_xpath("//*[@id='responsive']/div[2]/div/ul/li[2]/a").click()
driver.find_element_by_id("ww").send_keys("喜欢你")
driver.find_elements_by_class_name("s_btn")
driver.find_element_by_tag_name("input").click()
driver.close()
