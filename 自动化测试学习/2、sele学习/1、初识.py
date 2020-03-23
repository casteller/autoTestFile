from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
ele = driver.find_element_by_id("forecastIDg")
ele = driver.find_element_by_class_name()
print(ele.text)
citysWeather = ele.text.split(u'℃\n')
lowest = 100
lowestCity = []
for one in citysWeather:
    one = one.replace("℃","")
    #城市
    curcity = one.split("\n")
    #最低温度
    lowerweather = one.split("\n")[1].split("/")[0]
    lowerweather = int(lowerweather)

    if lowerweather < lowest:
        lowest = lowerweather
        lowestCity = [curcity]
    # elif lowerweather == lowest:
    #     lowestCity.append(curcity)
print(lowestCity)
driver.quit()
