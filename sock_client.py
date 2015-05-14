#-*-coding:utf-8 -*-
#获取新浪首页
import socket
soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ip4 socket流
soc.connect(('www.sina.com.cn',80)) #连接服务器
soc.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n') #发送数据
buffer=[]
while True:
    d = soc.recv(1024) #接收1024 字节
    if d:
        buffer .append(d)
    else:
        break
data=''.join(buffer)
soc.close()#关闭连接
'''接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件'''
header,html=data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
    f.write(html)