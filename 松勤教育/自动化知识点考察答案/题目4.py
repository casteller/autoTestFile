# coding=utf-8
'''4、下面的函数目的是把参数字符串倒序返回，请补全代码，完成功能
下面的程序用来将字符串倒序，
请补全代码
def reverseStr(source):
    # 将字符串中的每个字符放入列表中
    tmp = [c for c in source]
    # 列表倒序
    tmp.reverse()
    return __________
print (reverseStr('hello'))'''
def reverseStr(source):
    # 将字符串中的每个字符放入列表中
    tmp = [c for c in source]
    # 列表倒序
    tmp.reverse()
    print(tmp)
    return "".join(tmp)
print (reverseStr('hello'))