# coding=utf-8
import  requests
import os
from bs4 import BeautifulSoup

res = requests.get("http://www.qishu.cc/")
res.encoding="Gbk"
html = res.text
soup = BeautifulSoup(html,'lxml')
#获取热门小说链接
hots = soup.select(".leftshad div[class='sideContainer']+div a")
for hot in hots:
    link = "http://www.qishu.cc"+str(hot['href'])
    #获取下载地址
    loadres = requests.get(link)
    loadres.encoding='gbk'
    loadhtml = loadres.text
    soup = BeautifulSoup(loadhtml,'lxml')
    loadAddress = soup.select("#downAddress>a:nth-of-type(1)")
    for loadAddres in  loadAddress:
        url = loadAddres['href']
        name = url.split("/")[-1].split('.')[0]
        print('正在下载小说'+name)
        print(url)
        dirname='D:\小说'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        os.chdir(dirname)
        file = requests.get(url)
        with open(name+r'.rar','wb')as f:
            f.write(file.content)




# if __name__=='__main__':
#     getChapter()

