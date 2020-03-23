# coding=utf8
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = 'test'
#desired_caps['app'] = r"E:\apk\sqauto.apk"
desired_caps['appPackage'] = 'com.sqauto'
desired_caps['appActivity'] = 'com.sqauto.MainActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
#获取目标位置y坐标
target = driver.find_element_by_accessibility_id("songqin recommend")
target_y = target.location['y']
#每次移动的距离为应用图标的高度
app_img=driver.find_element_by_xpath('//android.widget.TextView[@content-desc="songqin recommend"]/following-sibling::android.widget.ImageView')
move_distance=app_img.size['height']
#确定拖动起点
ele=driver.find_element_by_accessibility_id('cramp fast')
xPos=ele.location['x']+ele.size['width']/2
yPos=ele.location['y']+ele.size['height']/2

driver.implicitly_wait(0.5)
while True:
    driver.swipe(xPos,yPos,xPos,yPos-move_distance,500)

    kb_ele=driver.find_elements_by_accessibility_id('best reputation')
    if kb_ele:
        #找到口碑最佳
        break

driver.implicitly_wait(10)

#直接将口碑滑动到松勤推荐的位置
driver.swipe(xPos, kb_ele[0].location['y'], xPos,target_y+150,3000)

xpath='//android.widget.TextView[@content-desc="best reputation"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]'

app_eles=driver.find_elements_by_xpath(xpath)
print('口碑最佳应用有：')

[print(ele.text) for ele in app_eles]

input('press any key to exit')
driver.quit()