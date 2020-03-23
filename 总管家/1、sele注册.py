from selenium import webdriver
import time,traceback
d = webdriver.Chrome()
d.maximize_window()
#打开网址
try:
    d.get("http://120.24.18.140:8092/")
    d.find_element_by_xpath("//div[@id='zlinks']/a[1]").click()
    d.find_element_by_name("phone").send_keys("17358983751")
    # d.find_element_by_id("zhuce").click()#正式库
    d.find_element_by_xpath("//input[@onclick]").click()#测试库
    d.find_element_by_xpath("//input[@value='3']").click()
    d.find_element_by_id("cname").send_keys("内部测试0122")
    d.find_element_by_name("reg[comname]").send_keys("内部测试0117")
    d.find_element_by_name("reg[passwd1]").send_keys("666666")
    d.find_element_by_name("reg[passwd2]").send_keys("666666")
    d.find_element_by_xpath("//input[@onclick]").click()
    print('注册成功')
except:
    print(traceback.format_exc())
finally:
    input("press any key to exit")
    d.quit()