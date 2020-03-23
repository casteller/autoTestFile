from webapi1 import *

loginresp,sessionid = login("auto","sdfsdfsdf")
assert loginresp["retcode"] == 0


#先列出课程
ret = list_course(sessionid)

#如果total等于0，则新增一门课程
if ret['total'] == 0:
    add_course("python","一种编程语言",1)

#列出新增后的课程
before = list_course(sessionid)

#删除课程
kcid = before['retlist'][0]['id']
resp = delete_course(kcid,sessionid)

if resp == {'retcode': 0}:
    print("删除成功")
print(resp)
#列出删除后的课程
after = list_course(sessionid)

#判断两次响应内容是否相等
if before != after:
    print('-----测试通过-----')