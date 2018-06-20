from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
test_input = driver.find_element_by_xpath("//*[@id='u1']/a[1]")
print(test_input.size)
print(test_input.text)
print(test_input.is_displayed())
print(test_input.is_enabled())
print(test_input.is_selected())
print(test_input.location)