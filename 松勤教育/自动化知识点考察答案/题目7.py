# coding=utf-8
from  selenium import  webdriver
import time

brower = webdriver.ChromeOptions()
brower.set_headless()
d= webdriver.Chrome(chrome_options=brower)
d.get(" https://music.163.com/")
d.maximize_window()
#点击排行榜
d.find_element_by_css_selector("a[data-module='toplist']").click()
d.implicitly_wait(10)
cnt = 1
while True:
    d.switch_to.frame("g_iframe")
    # 点击进入云音乐新歌榜
    d.find_element_by_xpath("//div[@id='toplist']//ul[1]//li[2]//p/a").click()
    #获取歌曲列表
    elements = d.find_elements_by_xpath("//tbody/tr//b")
    #点击歌曲名字
    songname = elements[cnt-1].click()
    #获取评论信息
    pl = d.find_element_by_xpath("//div[@class='m-cmmt']/div[2]/div[1]/div[2]")
    #作者
    author = pl.find_element_by_xpath("./div[1]//a").text
    #评论内容
    content = pl.find_element_by_xpath("./div[1]/div").text.replace(author + '：', '')
    #评论时间
    pltime = pl.find_element_by_xpath("./div[2]/div").text
    #点赞数量
    zancnt = pl.find_element_by_xpath("./div[2]/a[1]").text.split("(")[1].split(")")[0]
    print('=======================================')
    print("以下是排名第"+str(cnt)+"的歌曲的评论信息:\n作者："+author+"\n评论内容:"+content,"\n评论时间："+pltime,"\n点赞数量："+str(zancnt))
    d.back()
    d.implicitly_wait(5)
    cnt+=1
    if cnt>3:
        break
# input("press any key to exit")
d.quit()