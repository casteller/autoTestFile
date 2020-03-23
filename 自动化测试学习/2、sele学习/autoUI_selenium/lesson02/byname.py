
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson02/s1.html') # 打开网址

# -----------------------------------

eles = driver.find_elements_by_name('button')
if len(eles)<1:
    print('fail')
else:
    print('pass')



# -----------------------------------


input('press any key to quit...')
driver.quit()

