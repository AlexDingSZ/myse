from selenium import  webdriver
import  os
import  time
os.system("taskkill /im chromedriver.exe /f")
driver= webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//a[.='新闻']").click()
driver.find_element_by_id("ww").send_keys("abcd")
driver.find_element_by_id("s_btn_wr").click()
#获取当前的句柄并保存变量
main_handle = driver.current_window_handle
eles = driver.find_elements_by_xpath("//a[contains(@href,'http')][contains(@target,'_blank')]")
#找出所有搜索结果的链接元素
eles = driver.find_elements_by_xpath("//div/h3/a")
for ele in eles:
    print(ele.text)
    ele.click() #循环点击
    time.sleep(2)
    # 由于点击存在2个标签页，获取这些标签页的句柄
    handles = driver.window_handles
    for i in handles:
        #循环读取标签页句柄，如果不是搜索结果标签页，就关闭
        if i!=main_handle:
            driver.switch_to.window(i)
            driver.close()
    #切换回到搜索结果页面
    driver.switch_to.window(main_handle)
driver.close()
