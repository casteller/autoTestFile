import requests
#登录
def login(username,password):
    payload = {"username":username,"password":password}
    resp = requests.post("http://localhost/api/mgr/loginReq",data=payload)
    retobj = resp.json()
    return retobj,resp.cookies["sessionid"]
#添加课程
def add_course(name,desc,idx,sessionid):
    payload = {'action':'add_course',
               'data':'{"name":"%s","desc":"%s","display_idx":"%s"}'%(name,desc,idx)}

    resp = requests.post("http://localhost/api/mgr/sq_mgr/",data=payload,cookies={'sessionid':sessionid})
    retObj = resp.json()
    return retObj

#列出课程
def list_course(sessionid):
    payload = {'action':'list_course','pagenum':1,'pagesize':20}
    resp = requests.get("http://localhost/api/mgr/sq_mgr/",params=payload,cookies={'sessionid':sessionid})
    retlist = resp.json()
    return retlist

#修改课程
def modify_course(id,name,desc,idx,sessionid):
    payload = {'action':'modify_course','id':id,'newdata':{"name":name,"desc":desc,"display_idx":idx}}
    response = requests.put("http://localhost/api/mgr/sq_mgr/",data=payload,cookies={'sessionid':sessionid})
    return response.json()

#删除课程
def delete_course(id,sessionid):
    payload = {'action':'delete_course','id':id}
    response = requests.delete("http://localhost/api/mgr/sq_mgr/",data=payload,cookies={'sessionid':sessionid})
    return response.json()