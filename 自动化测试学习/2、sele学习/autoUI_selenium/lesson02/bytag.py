
from selenium import webdriver

# driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver = webdriver.Firefox(r'd:\tools\webdrivers')

driver.get('http://baidu.com') # 打开网址

# -----------------------------------
title=driver.find_element_by_tag_name('title').text
print(title)

# -----------------------------------


input('press any key to quit...')
driver.quit()

