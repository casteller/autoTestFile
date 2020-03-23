from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import Select
import time
import datetime

print(datetime.datetime.now())
# 获取地址信息，存入到listtemp这个列表中
filename = r'D:\phonenumber.txt'
fo = open(filename, encoding='UTF-8')
ele = fo.readlines()
listtmp = []
for each in ele:
    listtmp.append(each)
driver = webdriver.Ie(r'C:\Program Files\internet explorer\iedriverserver.exe')
# driver=webdriver.Chrome(r'C:\Users\hdy\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get(r'http://133.37.79.142:9001/zxcc/unitview/login.jsp')
driver.implicitly_wait(30)

# 输入用户名和密码
driver.find_element_by_id('operatorId').clear()
driver.find_element_by_id('operatorId').send_keys('7372')
driver.find_element_by_id('password').send_keys('abcabc123123')

# 选择省客服中心
select = Select(driver.find_element_by_id('vcid'))
# select.deselect_all()
select.select_by_visible_text('省客服中心')

time.sleep(2)
# 点击登陆
# driver.find_element_by_id('butLogin').click()
js = "var q=document.getElementById('butLogin').click()"
driver.execute_script(js)

input('请输入验证码')
# 输入验证码再次点击登陆
js = "var q=document.getElementById('butLogin').click()"
time.sleep(2)
driver.execute_script(js)
time.sleep(10)

# 选择电话号码
select = Select(driver.find_element_by_id('sel_notype'))
select.select_by_value('2')
time.sleep(1)

driver.implicitly_wait(30)
# driver.maximize_window()

number_zhuangtai = 0
number_result = 0
number_speed = 0
number_hinder = 0  # 群障
number_version = 0  # 终端能力
number_order = 0  # 在途单
number_internet = 0  # 上网记录
number_online = 0  # 在线状态
number_address = 0
numother = 0
timesall = 0
j = 1
listerror = []
for i in range(j):
    for phonenumber in listtmp:
        m = 1
        while m:
            try:

                # 输入宽带账号
                select = Select(driver.find_element_by_id('mainCallCity'))
                select.select_by_value('10100')
                time.sleep(1)

                driver.find_element_by_css_selector('span #customerno').clear()
                driver.find_element_by_css_selector('span #customerno').send_keys(phonenumber)
                time.sleep(1)
                select = Select(driver.find_element_by_id('mainCallCity'))
                select.select_by_value('10100')
                time.sleep(1)

                js = "var q=document.getElementById('btn_cha').click()"
                driver.execute_script(js)
                time.sleep(10)
                # 判断是否有查询结果
                driver.switch_to.frame(driver.find_element_by_css_selector('iframe#frame_customerInfo'))
                texttmp = driver.find_element_by_css_selector('#body_prod tr td').text

                if texttmp == '查询中，请稍候...':
                    print(texttmp)
                    driver.switch_to.parent_frame()
                    js = "var q=document.getElementById('btn_cha').click()"
                    driver.execute_script(js)
                    time.sleep(10)
                    driver.switch_to.frame(driver.find_element_by_css_selector('iframe#frame_customerInfo'))

                onetel = driver.find_elements_by_css_selector('#body_prod tr')
                driver.switch_to.default_content()
                # print(len(onetel))
                if len(onetel) < 2:
                    listerror.append(phonenumber)
                    number_result += 1
                    break

                driver.switch_to.default_content()

                # 选择宽带障碍，并点宽带障碍（需要确认一下列表是否是固定的）
                driver.switch_to.frame(driver.find_element_by_css_selector('iframe#frame_customerInfo'))
                js = "var q=document.getElementById('kd_id0').click()"
                driver.execute_script(js)

                driver.switch_to.default_content()
                time.sleep(15)

                driver.switch_to.frame('frame_zasg')
                driver.switch_to.frame('frame_zhuangyiweishengao')

                # 这里进行断言处理
                # 业务账号状态判断
                text1 = driver.find_element_by_id('crmState').text
                # print(text1)
                if text1 == '':
                    driver.switch_to.default_content()
                    number_zhuangtai += 1
                    break
                # 宽带签约速率判断
                text2 = driver.find_element_by_id('CDMAspeed').text
                # print(text2)
                if len(text2) < 2:
                    listerror.append(phonenumber)
                    currnet_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
                    filename = currnet_time + '.png'
                    driver.get_screenshot_as_file(filename)
                    driver.switch_to.default_content()
                    number_speed += 1
                    break
                if text2 == '查询失败!':
                    listerror.append(phonenumber)
                    currnet_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
                    filename = currnet_time + '.png'
                    driver.get_screenshot_as_file(filename)
                    driver.switch_to.default_content()
                    number_speed += 1
                    break
                # 是否有群张
                text3 = driver.find_element_by_css_selector('#selectTable #largeBug').text
                # print(text3)
                if text3 == '':
                    listerror.append(phonenumber)
                    driver.switch_to.default_content()
                    number_hinder += 1
                    break
                # 终端能力
                text8 = driver.find_element_by_css_selector('#cdmaterminaltittle td span').text
                # print(text8)
                if text8 == '':
                    listerror.append(phonenumber)
                    driver.switch_to.default_content()
                    number_version += 1
                    break

                # 检查是否有在途工单
                text5 = driver.find_elements_by_css_selector('#hirstory tr')
                # print(text5)
                if len(text5) < 1:
                    listerror.append(phonenumber)
                    driver.switch_to.default_content()
                    number_order += 1
                    break
                # driver.switch_to.default_content()#记得调试完了之后把这段代码删掉

                # 滚动页面
                # js = 'window.scrollTo(0,document.body.scrollHeight)'
                js = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js)
                time.sleep(1)
                driver.switch_to.frame(driver.find_element_by_css_selector('#pretreat'))

                # 点击上网记录查询

                js = "document.querySelectorAll('#box #tools #Binos_RecordList_btn')[0].click()"
                driver.execute_script(js)
                time.sleep(2)

                # 检查是否有上网记录查询
                eles = driver.find_elements_by_css_selector('#qryRst > table > tbody > tr > td > table > tbody>tr')
                # print(len(eles))
                if len(eles) < 2:
                    listerror.append(phonenumber)
                    driver.switch_to.default_content()
                    number_internet += 1
                    break

                # #关闭弹窗
                js = "var q=document.getElementsByClassName('close-reveal-modal')[6].click()"
                driver.execute_script(js)
                time.sleep(1)

                # 点击上网日志查询
                js = "var q=document.getElementById('Binos_Record_btn').click()"
                driver.execute_script(js)
                time.sleep(2)

                # 关闭弹窗
                js = "var q=document.getElementsByClassName('close-reveal-modal')[5].click()"
                driver.execute_script(js)
                time.sleep(1)

                # 点击在线用户查询
                js = "var q=document.getElementById('Binos_Operate_12_btn').click()"
                driver.execute_script(js)
                time.sleep(2)

                text6 = driver.find_element_by_css_selector(
                    '#qryRst > table > tbody > tr:nth-child(1) > td:nth-child(2)').text
                # print(text6)
                if text6 == '':
                    listerror.append(phonenumber)
                    driver.switch_to.default_content()
                    number_online += 1
                    break

                # 关闭弹窗
                js = "var q=document.getElementsByClassName('close-reveal-modal')[4].click()"
                driver.execute_script(js)

                driver.switch_to.default_content()
                # 点击更多信息
                js = "var q=document.getElementsByClassName('icon_right')[0].click()"
                driver.execute_script(js)

                # 点击查看
                js = "document.querySelectorAll('#postAddr a')[0].click()"
                driver.execute_script(js)
                time.sleep(1)

                # 客户地址查询
                text4 = driver.find_element_by_css_selector('#postAddr').text
                # print(text4)
                if text4 == '':
                    listerror.append(phonenumber)
                    driver.switch_to.default_content()
                    number_address += 1
                    break

                # 关闭弹窗
                js = "document.querySelectorAll('#customerInfo_plus img')[0].click()"
                driver.execute_script(js)
                time.sleep(1)
            except ElementNotInteractableException:
                # 76行定位的元素报错了
                ele = driver.find_element_by_css_selector('span #customerno')
                ele.get_attribute('outerHTML')

            print(datetime.datetime.now())
            listerror.append(phonenumber)
            # 打印失败时的截图
            currnet_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            filename = currnet_time + '.png'
            driver.get_screenshot_as_file(filename)

            numother += 1
            driver.refresh()
            time.sleep(8)
            select = Select(driver.find_element_by_id('sel_notype'))
            select.select_by_value('2')
            time.sleep(1)
            # print(datetime.datetime.now())
        m = 0
    numberall = number_address + number_online + number_internet + number_order + number_version + number_hinder + number_speed + number_zhuangtai + numother + number_result
    timesall += 1
    print(listerror)
    print(
        '第%s次执行10000号流程,总共失败%s,输入账号查询失败%s,业务账号状态失败%s,宽带签约速率%s,群障查询失败%s,终端能力查询失败%s,在途工单查询%s,上网记录查询%s,在线用户查询%s,客户地址查询%s,宽带账号%s' % (
        timesall, numberall, number_result, number_zhuangtai, number_speed, number_hinder, number_version, number_order,
        number_internet, number_online, number_address, phonenumber))
print(datetime.datetime.now())
print(listerror)

















