# coding=utf-8
'''3、下面的列表里面包含了一些字符串元素
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
请用while 循环 写一段代码打印其中所有包含ok的字符串元素'''
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
cnt = 1
lenth = len(info)
while cnt<=lenth:
    if "ok" in info[cnt-1]:
        print(info[cnt-1])
    cnt += 1

