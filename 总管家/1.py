str = ('<script>alert("登录名不存在");window.history.go(-1);</script>')
r = str.split('"')[1]
print(r)