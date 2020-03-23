import requests
#登录
payload = {"username":10028604750, "password":666666,"qrid":'',"pwds":'',"randnumber":''}
r = requests.post("https://ob.oacrm.com/login/login",data=payload)
loginCookies = r.cookies
#添加报告
def add_report(auid,content,type):
    payload = {"auid":auid,"content":content,"types":type}
    resp = requests.post("https://oc.oacrm.com/apply/add",data=payload,cookies=loginCookies)
    retdict = resp.json()
    if retdict["err"] == 0:
        print("主人，您的报告已经添加完毕\n报告内容为："+content)

add_report(385,"1226工作日志 测试安卓，处理销售反馈问题",1)