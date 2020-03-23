from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.51job.com")
driver.find_element_by_id("kwdselectid").send_keys("python")
driver.find_element_by_id("work_position_input").click()
time.sleep(2)
#去掉已经选中的城市
ele = driver.find_element_by_css_selector("#work_position_click_multiple_selected").find_element_by_tag_name("em").click()
#选中杭州
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
#保存选择信息
driver.find_element_by_id("work_position_click_bottom_save").click()
#搜素
driver.find_element_by_css_selector(".ush button").click()
jobs = driver.find_elements_by_css_selector("#resultList div.el")
for job in jobs[1:]:
    job_msgs = job.find_elements_by_tag_name("span")
    msgs = [msg.text for msg in job_msgs]
    print("|".join(msgs))
driver.quit()