import requests,traceback
#登录
payload = {"username":15928604750, "password":666666,"qrid":'',"pwds":'',"randnumber":''}
r = requests.post("http://120.24.18.140:8092/login/login",data=payload)
str=(r.text)
if str.split('"')[1] == "登录名不存在":
    print("登录名不存在")
loginCookies = r.cookies
print(loginCookies)
#注销
try:
    payload = {"zcode":201610}
    resp = requests.post("http://120.24.18.140:8092/users/del_com_all",data=payload,cookies=loginCookies)
    redict = resp.json()
    if redict["err"] == 0:
        print("注销成功")
    else:
        print("注销失败")
except Exception:
    print(traceback.format_exc())
