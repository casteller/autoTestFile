import requests
class webapizy(object):
    #登录
    def login(self,username,password):
        payload = {"username":username,"password":password}
        resp = requests.post("http://localhost/api/mgr/loginReq",data=payload)
        retobj = resp.json()
        return resp.cookies["sessionid"]

    #添加老师
    def addteacher(self,username,realname,desc,idx,sessionid,password):
        payload ={'action':'add_teacher','data':'{"username":"%s","courses":[],"realname":"%s","desc":"%s","display_idx":"%s","password":"%s"}'%(username,realname,desc,idx,password)}
        resp = requests.post("http://localhost/api/mgr/sq_mgr/", data=payload,cookies={'sessionid':sessionid})
        retObj = resp.json()
        return retObj

    #列出老师
    def listteacher(self,sessionid):
        payload = {'action': 'list_teacher', 'pagenum': 1, 'pagesize': 20}
        resp = requests.get("http://localhost/api/mgr/sq_mgr/",params=payload,cookies={'sessionid':sessionid})
        retlist = resp.json()
        return retlist

    #删除老师
    def deleteteacher(self,id,sessionid):
        payload = {'action':'delete_teacher','id':id}
        response = requests.delete("http://localhost/api/mgr/sq_mgr/",data=payload,cookies={'sessionid':sessionid})
        return response.json()

    #删除所有老师
    def deleteallteacher(self):
        # 先列出所有老师
        sessionid = self.login('auto','sdfsdfsdf')
        rd =  self.listteacher(sessionid)
        # 删除所有的老师
        for one in rd['retlist']:
            self.deleteteacher(one['id'],sessionid)
        #再列出所有老师检查是否删干净
        rd =  self.listteacher(sessionid)
        if rd['retlist'] != []:
            raise  Exception("删除所有的老师失败")

if __name__ == '__main__':
    a = webapizy()
    sessionid = a.login('auto', 'sdfsdfsdf')
    print(sessionid)
    b = a.addteacher('lirui1', '李睿1', '天文老师', 2, sessionid, "sq888")
    print(b)
    c = a.listteacher(sessionid)
    print(c)
    d = a.deleteteacher(1, sessionid)
    print(d)
    e = a.deleteallteacher()
    print(e)