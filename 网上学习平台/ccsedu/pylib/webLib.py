# coding=utf-8
from ccsedu.cfg  import *
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
class webLib(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        pass
    #打开浏览器
    def openb_rowser(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)
    #关闭浏览器
    def close_browser(self):
        self.wd.quit()
    #登录
    def login(self,username,password):
        self.wd.get(loginurl)
        self.wd.find_element_by_xpath("//div[@class='box-login']//div//select/option[2]").click()
        self.wd.find_element_by_name("username").send_keys(username)
        self.wd.find_element_by_name("password").send_keys(password)
        self.wd.find_element_by_xpath("//button").click()
    #添加老师
    def addteacher(self):
        self.wd.find_element_by_xpath("//ul[contains(@class,'main')]/li[5]//div/span").click()
        self.wd.find_element_by_xpath("//ul[contains(@class,'main')]/li[5]//ul//span").click()
        time.sleep(2)
        self.wd.find_element_by_xpath("//div[@ng-controller='lecturerListController']//div[2]/button[1]").click()
        self.wd.find_element_by_xpath("//div/input[@ng-model='lecturer.name']").send_keys("李睿")
        time.sleep(2)
        self.wd.find_element_by_xpath("//div/span[@ng-click='selectCompany()']").click()
        self.wd.find_element_by_xpath("//div[@class='box-tree']").click()
        time.sleep(1)
        self.wd.find_element_by_xpath("//div/button[@ng-click='ok()']").click()
        self.wd.find_element_by_xpath("//div/input[@ng-model='lecturer.position']").send_keys("物理老师")
        self.wd.find_element_by_xpath("//div/input[@ng-model='lecturer.masterCourse']").send_keys("物理")
        self.wd.find_element_by_xpath("//div/input[@ng-model='lecturer.mobile']").send_keys("15928604750")
        self.wd.find_element_by_xpath("//div/input[@ng-model='lecturer.phone']").send_keys("02882777172")
        self.wd.find_element_by_xpath("//div/input[@ng-model='lecturer.email']").send_keys("917880821@qq.com")
        self.wd.find_element_by_xpath("//div/textarea[@ng-model='lecturer.introduction']").send_keys("资深物理老师")
        self.wd.find_element_by_xpath("//div/button[@ng-click='save()']").click()
    #添加课件
    def addkejian(self):
        self.wd.find_element_by_xpath("//ul[contains(@class,'main')]/li[6]//div/span").click()
        self.wd.find_element_by_xpath("//ul[contains(@class,'main')]/li[6]//ul[1]//li[1]//span").click()
        time.sleep(2)
        self.wd.find_element_by_xpath("//div[@ng-controller='coursewareListController']//div[2]/button[1]").click()
        self.wd.find_element_by_xpath("//div/input[@ng-model='courseware.name']").send_keys("课件名称")
        time.sleep(1)
        self.wd.find_element_by_xpath("//div[@ng-model='courseware.specialty']").click()
        self.wd.find_element_by_xpath("//div[@ng-model='courseware.specialty']//ul//li//div[3]/a").click()
        self.wd.find_element_by_xpath("//div/textarea[@ng-model='courseware.explain']").send_keys("课件简介")
        self.wd.find_element_by_xpath("//div/button[@ng-click='save()']").click()
        self.wd.find_element_by_xpath("//div/button[@ng-click='back()']").click()





if __name__ == '__main__':
     op = webLib()
     op.openb_rowser()
     op.login("zhangqingqin","1qaz@WSX")
    # op.addteacher()
    # op.addkejian()