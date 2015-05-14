#-*-coding:utf-8 -*-
import socket
soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip4 socket流
soc.connect(('127.0.0.1',9999)) #连接服务器
print soc.recv(1024)

for  data in ['mar','123456789','好123','nao','疏花火烧兰s','圣弗朗西斯科']:
    soc.send(data)
    print soc.recv(1024)
soc.send('exit')
soc.close()