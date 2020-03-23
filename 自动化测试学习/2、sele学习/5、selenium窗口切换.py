from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
d = webdriver.Chrome()
d.implicitly_wait(10)
d.maximize_window()
d.get("https://www.vmall.com/")
d.find_element_by_xpath("//div[@class='s-sub']//li[2]/a").click()
handles = d.window_handles
#保存主窗口句柄
main_window = d.current_window_handle

for handle in handles:
    if handle != main_window:
        #保存官网窗口句柄
        second_window = handle
        d.switch_to_window(handle)

title = ['智能手机','笔记本','平板','智能穿戴','智能家居','更多产品','软件应用','服务与支持']
title1 =[]
eles = d.find_elements_by_xpath("//ul[@class='clearfix nav-cnt']/li")
for ele in eles:
    title1.append(ele.text)
if title1 == title:
    print("huawei page pass")
else:
    print("huawei page fail")
#窗口切换到主窗口
d.switch_to_window(main_window)
#鼠标悬停
attrible = d.find_element_by_css_selector("li#zxnav_1")
ActionChains(d).move_to_element(attrible).perform()
time.sleep(2)
text = ['平板电脑','笔记本电脑','笔记本配件']
text1 = []
elements = attrible.find_elements_by_css_selector("li#zxnav_1>div+div span")
for element in elements:
    text1.append(element.text)
if text1 == text:
    print("vamll page pass")
else:
    print("vmall page fail")
d.quit()
