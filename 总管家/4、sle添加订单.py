from selenium import webdriver
import time,traceback
d = webdriver.Chrome()
d.maximize_window()
#打开网址
d.get("http://120.24.18.140:8092/")
#登录
try:
    d.find_element_by_name("username").send_keys("10700000080")
    d.find_element_by_name("password").send_keys("666666")
    d.find_element_by_id("submit1").click()
    d.find_element_by_id("mainstk").click()
    #操作按钮
    d.find_element_by_xpath("//tbody//tr[@class='table-line'][1]//button").click()
    d.find_element_by_xpath("//tbody//tr[@class='table-line'][1]//ul[@data-id]/li[1]").click()
    time.sleep(2)
    d.find_element_by_xpath("//div[@class='modal-body']/div[2]/div[31]/div[2]/a").click()
    time.sleep(2)
except Exception:
    print(traceback.format_exc())
finally:


    d.quit()
