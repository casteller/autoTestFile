from selenium import webdriver
import time
d = webdriver.Chrome()
d.maximize_window()
#打开网址
d.get("https://oc.oacrm.com")
#登录
d.find_element_by_name("username").send_keys("10028604750")
d.find_element_by_name("password").send_keys("666666")
d.find_element_by_id("submit1").click()
d.find_element_by_id("subMenu4").click()
time.sleep(2)
#添加报告
d.find_element_by_css_selector("div button[aria-expanded=false]").click()
d.find_element_by_id("addReport").click()
time.sleep(2)
d.find_element_by_xpath("//*[@id='MyDelist']").click()
time.sleep(2)
d.find_element_by_name("385").click()
a = d.find_element_by_id("subContent")
current_time = time.strftime("%Y-%m-%d")
a.send_keys(current_time+"工作日志 测试网页端苹果端，发布苹果新版，处理销售反馈问题")
d.find_element_by_id("btnAddCon").click()
time.sleep(2)
# d.find_element_by_css_selector("#divTopBack button[aria-expanded=false]").click()
# time.sleep(2)
# d.find_element_by_xpath("//*[@id='divTopBack']/div/ul/li[8]/a").click()
d.quit()