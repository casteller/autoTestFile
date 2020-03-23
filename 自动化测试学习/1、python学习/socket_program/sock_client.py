#导入socket库
import socket
from socket import *

#创建一个socket对象
#AF_INET代表ipv4协议，SOCK_STREAM代表TCP协议
sock=socket(AF_INET,SOCK_STREAM)

#建立起一个连接
sock.connect(('127.0.0.1', 9999))

#发送http请求
# request='GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'

# sock.send(request.encode('utf8'))

# buffer=[]
while True:
    msg = input('>>')
    # 如果不输入，就退出并断开连接
    if len(msg) < 1:
        break
    # 发送数据
    sock.send(msg.encode())
    data=sock.recv(1024)
    if data:
        # buffer.append(data.decode('utf8'))
        print(data.decode('utf8'))
    else:
        break

# res=''.join(buffer)
# print(res)

#关闭连接
sock.close()

