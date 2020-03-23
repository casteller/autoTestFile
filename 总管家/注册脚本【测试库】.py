import requests

def getyzm(phone):
    payload = {"phone":phone}
    req = requests.post("http://120.24.18.140:8092/login/rcode",data=payload)
    txt = req.text
    rcode1 = txt.split('"reg[rcode]"')[1].split("size")[0].replace(" ","").replace('"',"").split("value=")[1]
    return rcode1


def zhuce(phone,ver,cname,comname,password1,password2,rcode):

    payload = {"phone":phone,"ver":ver,"reg[cname]":cname,
               "reg[comname]":comname,"reg[passwd1]":password1,
               "reg[passwd2]":password2,"reg[rcode]":rcode1}
    resp = requests.post("http://120.24.18.140:8092/login/rsubmit",data=payload)
    redict = resp.text
    if redict == '<script>top.location.href="/"</script>':
        print("注册成功")
    else:
        print("注册失败")

zhuce(17358983751,3,"内部测试1227","内部测试1227",666666,666666,rcode1)



