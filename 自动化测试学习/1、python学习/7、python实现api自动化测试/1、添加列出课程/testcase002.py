from webapi import *
def testcase2():
    #先添加一门课程
    retobj1 = add_course("python", "一种很火的编程语言", 2)
    #判断课程添加成功
    if retobj1["retcode"] == 0:
        print("添加成功")
    else:
        print("添加失败")
    #列出课程
    before = list_course()
    #再添加一门课程
    retobj2 = add_course("python", "一种很火的编程语言", 2)
    if retobj2["retcode"] == 2:
        print(retobj2)

    #再列出课程
    after = list_course()
    #判断两次列出的课程列表相等
    if before == after:
        print("-----测试通过-----")
testcase2()