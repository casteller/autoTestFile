from selenium import  webdriver
import time


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('http://localhost/mgr/login/login.html')

driver.find_element_by_id('username').send_keys('auto')
driver.find_element_by_id('password').send_keys('sdfsdfsdf')

driver.find_element_by_tag_name('button').click()


time.sleep(1)

driver.implicitly_wait(1)

while True:

    delButtons = driver.find_elements_by_css_selector(
    '*[ng-click^=delOne]')

    if delButtons == []:
        break

    delButtons[0].click()
    driver.find_element_by_css_selector('.modal-footer  .btn-primary').click()

    time.sleep(1)


driver.implicitly_wait(5)