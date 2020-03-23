import requests
#获取验证码
payload = {"phone":17358983751}
req = requests.post("https://ob.oacrm.com/login/rcode",data=payload)
txt = req.text
print(txt)
rcode1 = txt.split('"reg[rcode]"')[1].split("size")[0].replace(" ","").replace('"',"").split("value=")[1]
print(rcode1)
#注册
def zhuce(phone,ver,cname,comname,password1,password2,rcode):

    payload = {"phone":phone,"ver":ver,"reg[cname]":cname,
               "reg[comname]":comname,"reg[passwd1]":password1,
               "reg[passwd2]":password2,"reg[rcode]":rcode1}
    resp = requests.post("https://ob.oacrm.com/login/rsubmit",data=payload)
    redict = resp.text
    if redict == '<script>top.location.href="/"</script>':
        print("注册成功")

zhuce(17358983751,3,"内部测试1227","内部测试1227",666666,666666,rcode1)





