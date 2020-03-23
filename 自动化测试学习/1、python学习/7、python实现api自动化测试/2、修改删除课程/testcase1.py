from webapi1 import *

loginresp,sessionid = login("auto","sdfsdfsdf")
assert loginresp["retcode"] == 0

#先列出课程
courselistBefore = list_course(sessionid)

#如果total等于0，则新增一门课程
if courselistBefore['total'] == 0:
    add_course("python","一种编程语言",1,sessionid)
courselistAfter = list_course(sessionid)
print(courselistAfter)
cid = courselistAfter['retlist'][0]['id']
print(cid)
retDict = modify_course(cid,"java","一种编程语言",1,sessionid)
print(retDict)
assert retDict['retcode'] == 0
print("pass")

courselistFinal = list_course(sessionid)
if courselistFinal['retlist'][0]['name'] == "java":
    print("-----测试通过-----")




