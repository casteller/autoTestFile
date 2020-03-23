from selenium import webdriver
import time
def deletecourse():
    d = webdriver.Chrome()
    d.implicitly_wait(10)
    d.get("http://localhost/mgr/login/login.html")
    d.find_element_by_id("username").send_keys("auto")
    d.find_element_by_id("password").send_keys("sdfsdfsdf")
    d.find_element_by_css_selector("button").click()
    d.implicitly_wait(2)
    while True:
        eles=d.find_elements_by_css_selector("button[ng-click='delOne(one)']")
        if eles:
            eles[0].click()
            time.sleep(1)
            d.find_element_by_xpath("//div[@class='bootstrap-dialog-footer-buttons']//button[2]").click()
            time.sleep(1)
        else:
            break
    d.implicitly_wait(10)
    d.quit()