from selenium import webdriver
import time
d = webdriver.Chrome()
d.implicitly_wait(10)
d.maximize_window()
#打开12306
d.get("https://kyfw.12306.cn/otn/leftTicket/init")
d.find_element_by_id("fromStationText").click()
d.find_element_by_id("fromStationText").send_keys("南京南\n")
d.find_element_by_id("toStationText").click()
d.find_element_by_id("toStationText").send_keys("杭州东\n")
d.find_element_by_xpath("//select[@id='cc_start_time']/option[3]").click()
d.find_element_by_xpath("//*[@id='date_range']/ul/li[2]").click()
time.sleep(2)
trainlines = d.find_elements_by_xpath("//div[@id='t-list']/table/tbody/tr[@class]")
for one in trainlines:
    secondlevelsit = one.find_element_by_xpath(".//td[4]")
    clas = secondlevelsit.get_attribute("class")
    if clas =="yes" or clas=="t-num":
        print(one.find_element_by_xpath(".//div//a").text)
d.quit()
