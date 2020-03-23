# coding=utf-8
import requests,json,time
from pprint import pprint
class  studyLib(object):
    time = time.strftime("%Y-%m-%d", time.localtime())
    def  header(self):
        headers = {
            'Host': '10.206.20.47:8097 ',
            'Cookie': 'APP_SESSIONID=88488cb0-3130-4e73-af8e-50056a5451c8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        return headers
    #登录
    def login(self,type,username,password):
        url = "http://10.206.20.47:8097/ccsedu/a/login.do "
        payload = {'args':None,'usertype':type,'username':username,'password':password}
        r = requests.post(url,data =payload)
        logincookie = r.cookies
        return logincookie
    #添加老师
    def addteacher(self,name,masterCourse,externalUnit,position):
        url = "http://10.206.20.47:8097/ccsedu/a/js/jsgl/saveLecturer "
        payload = {'name':name,'sex':1,'levels':1,'type':2,'masterCourse':masterCourse,'externalUnit':externalUnit,'position':position}
        res = requests.post(url,data=payload,headers=SL.header())
        print(res.json())
    #添加课件
    def addkejian(self,name,explain,specialty):
        url = "http://10.206.20.47:8097/ccsedu/a/kc/kjgl/saveCourseware"
        payload = {'name':name,'explain':explain,'specialty':specialty,'corpId':510101,'deptId':51000005,'createBy':89787,'createDate':studyLib.time}
        r = requests.post(url,data=payload,headers=SL.header())
        print(r.json())
    #添加课程
if __name__ == '__main__':
    SL = studyLib()
    cookies = SL.login(2,'zhangqingqin','1qaz@WSX')
    print(cookies)
    #res = SL.addteacher("李睿",'数学','未知机构','职务数学老师')
    # for i in range(10):
    #     coursename = "测试添加课件"+str(i)
    #     explain = "测试课件简介"+str(i)
    #     re = SL.addkejian(coursename,explain,1)