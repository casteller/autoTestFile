from selenium import webdriver
import win32com.client
import time
#获取shell对象
shell = win32com.client.Dispatch("WScript.Shell")
d = webdriver.Chrome()
d.maximize_window()
d.get("https://tinypng.com/")
d.find_element_by_css_selector("section.upload").click()
time.sleep(2)
#使用shell对象的Sendkeys方法给应用程序发送字符串
shell.Sendkeys(r"C:\Users\Administrator\Pictures\李睿.png"+'{ENTER}'+'\n')
d.implicitly_wait(2)
txt = d.find_element_by_css_selector("li.upload>div").text
#验证是否上传成功
if "李睿.jpg" in txt:
    print("test pass")
else:
    print("test fail")
# input("press any key to exit")

