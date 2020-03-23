from selenium import webdriver
import time,traceback
d = webdriver.Chrome()
d.maximize_window()
try:
    # 打开网址
    d.get("http://120.24.18.140:8092/")
    #输入账号密码
    d.find_element_by_name("username").send_keys("17358983751")
    d.find_element_by_name("password").send_keys("666666")
    # 点击设置
    d.find_element_by_id("submit1").click()
    # 点击老总管理设置
    d.find_element_by_id("mainset").click()
    # 点击老总管理设置
    d.find_element_by_xpath("//div[@sid='g7']").click()
    # 点击账户充值
    d.find_element_by_id("subMenu11").click()
    #点击注销企业
    xpath1 = "//div[@class='cssPadbody']//tr//td[@width='17%'][1]/p[4]"
    d.find_element_by_xpath(xpath1).click()
    time.sleep(2)
    # #点击确定按钮
    xpath2 = "//div[@id='alertBottom']/button[2]"
    d.find_element_by_xpath(xpath2).click()
    time.sleep(1)
    #输入注销验证码
    css1 = "body.modal-open>div>form input#VerificationCode"
    d.find_element_by_css_selector(css1).send_keys("201610")
    #点击注销按钮
    css2 = "body.modal-open>div>form button#zhuxiaoloading"
    d.find_element_by_css_selector(css2).click()
    #获取alert确认框
    dialog_box = d.switch_to_alert()
    #点击确认
    dialog_box.accept()
    time.sleep(1)
    dialog_box1 = d.switch_to_alert()
    dialog_box1.accept()
except:
    print(traceback.format_exc())
finally:
    input("press any key to exit")
    d.quit()