from socket import *

#创建一个socket对象
tcpServSock=socket(AF_INET,SOCK_STREAM)
# 绑定地址和端口
tcpServSock.bind(('127.0.0.1', 9999))

#开始监听
tcpServSock.listen(5)

print('等待客户端连接...')


#接收客户端连接请求
while True:
    # 接收一个客户端连接,accept是一个阻塞式方法
    c_sock, addr = tcpServSock.accept()
    print('收到来自%s的连接'%addr[0])
    # 接收数据
    while True:
        # 接收消息，recv是阻塞式方法
        data = c_sock.recv(1024)
        print('收到来自%s的消息:%s' % (addr, data.decode()))
        # 当客户端主动断开连接时，socket会收到一个空字符串''，如果发送了EOF,我就认为是结束信号
        if not data or data.decode() == 'EOF':
            print('断开与%s的连接' % addr[0])
            c_sock.close()
            break
        # 如果发送过来的数据不为空,则把数据加上前缀发送出去
        else:
            msg = 'Hello! %s' % data.decode()
            c_sock.send(msg.encode())








