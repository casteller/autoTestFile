#读取文件合并内容
with open("C:\cfiles\gbk编码.txt", encoding="gbk")as f1,\
    open("C:\cfiles\\utf8编码.txt", encoding="utf-8")as f2:
    content1 = f1.read()
    content2 = f2.read()
    newcontent = content1 + " " +content2
    print(newcontent)

#将合并后的内容存到新文件里
newfilename = input("请输入新文件名称：")
f = open("C:\cfiles\%s" % newfilename, "w", encoding="utf-8")
f.write(newcontent)
f.close()

#打印出新命名的文件内容
with open("C:\cfiles\%s" % newfilename,encoding="utf-8") as f3:
    content3 = f3.read()
    print(content3)

