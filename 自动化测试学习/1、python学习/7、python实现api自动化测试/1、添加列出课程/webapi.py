import requests
#添加课程
def add_course(name,desc,idx):
    payload = {'action':'add_course',
               'data':'{"name":"%s","desc":"%s","display_idx":"%s"}'%(name,desc,idx)}

    resp = requests.post("http://localhost/api/mgr/sq_mgr/",data=payload)
    retObj = resp.json()
    return retObj
#列出课程

def list_course():
    payload = {'action':'list_course','pagenum':1,'pagesize':20}
    resp = requests.get("http://localhost/api/mgr/sq_mgr/",params=payload)
    retlist = resp.json()['retlist']
    return retlist



