from selenium import  webdriver
#driver = webdriver.Chrome()
driver = webdriver.Chrome(r"D:\env\android-sdk\tools\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.get(r"C:\Users\Administrator\PycharmProjects\myse\iframe.html")
driver.maximize_window()
iframe_baidu = driver.find_element_by_xpath("//iframe[@name='百度']")
iframe_sougou = driver.find_element_by_xpath("//iframe[@name='搜狗']")
#driver.switch_to.frame("baidu")
#driver.switch_to.frame(u"百度")
#driver.switch_to.frame(iframe_baidu)
driver.switch_to.frame(0)
driver.find_element_by_id("kw").send_keys("baidu selenium")
driver.find_element_by_id("su").click()
driver.switch_to.default_content()
driver.switch_to.frame(iframe_sougou)
driver.find_element_by_id("query").send_keys("sougou selenium")
driver.find_element_by_id("stb").click()

