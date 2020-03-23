from selenium import webdriver
import time
import os
class Test_ab():
    def __init__(self):
        self.browser_type='Chrome'
    # 封装驱动
    def test_driver(self):
        if self.browser_type == "Firefox":
            self.driver=webdriver.Firefox()
        if self.browser_type == "Chrome":
            self.driver=webdriver.Chrome()
        if self.browser_type == "IE":
            self.driver=webdriver.Ie()
            return
    # 封装元素,sendkeys
    def test_element(self,type,value,inputvalue):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        if type =="id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        if type == "line_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        if type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        if type =="css_selector":
            self.driver.find_element_by_css_selector(value).send_keys(inputvalue)
    # 鼠标事件一
    def test_elements(self,type,value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        if type == "id":
            self.driver.find_element_by_id(value).click()
        if type == "line_text":
            self.driver.find_element_by_link_text(value).click()
        if type == "name":
            self.driver.find_element_by_name(value).click()
    # 鼠标事件二
    def Clear(self, type, value):
        if type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()
    #切换窗口
    def Current_handel(self):
        # 这时切换到新窗口
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)
    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
    # 浏览器后退操作
    def back(self):
        self.driver.back()
    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

        # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            self.get_windows_img()
     #跳转窗口
    def Current_handle(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)
    # 获取输入框的值
    def Get_attribute(self, type, value1, value2):
        if type == "xpath":
            Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.driver.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.driver.find_element_by_id(value1).get_attribute(value2)
            return Value
        elif type =="tag_name":
            Value = self.driver.find_element_by_tag_name(value1).get_attribute(value2)
            return Value
    # 获取下拉框的文本的值
    def Get_text(self, type, value):
        if type == "xpath":
            text = self.driver.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.driver.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.driver.find_element_by_id(value).text
            return text
    def abc(self,value):
        self.driver.switch_to.frame(value)
    def getout(self):
        self.driver.quit()

















