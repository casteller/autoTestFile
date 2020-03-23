from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.51job.com")
#点击高级搜素
driver.find_element_by_css_selector(".more").click()
driver.find_element_by_id("kwdselectid").send_keys("python")
driver.find_element_by_id("work_position_input").click()
time.sleep(2)
#去掉已经选中的城市
ele = driver.find_element_by_css_selector("#work_position_click_multiple_selected").find_element_by_tag_name("em").click()
#选中杭州
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
#保存选择信息
driver.find_element_by_id("work_position_click_bottom_save").click()
#点一下别的地方
driver.find_element_by_css_selector(".tit").click()
#选择职能类别高级软件工程师
driver.find_element_by_id("funtype_click").click()
driver.find_element_by_css_selector("#funtype_click_center_left li").click()
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
#选择公司性质 外欧美
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('#cottype_list span.li[data-value="01"]').click()
#选择工作年限 1-3年
driver.find_element_by_id("workyear_list").click()
driver.find_element_by_css_selector('#workyear_list span.li[data-value="02"]').click()
#搜素
driver.find_element_by_css_selector(".p_but").click()
#获取返回职位信息
jobs = driver.find_elements_by_css_selector("#resultList div.el")
for job in jobs[1:]:
    job_msgs = job.find_elements_by_tag_name("span")
    msgs = [msg.text for msg in job_msgs]
    print("|".join(msgs))
driver.quit()










