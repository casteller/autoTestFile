# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('https://www.baidu.com/')


# ----------------------------------
driver.get_screenshot_as_file('shot.png')

ele = driver.find_element_by_id('su')
ele.screenshot('e:\\button.png')
# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出