#-*-coding:utf-8-*-
import socket
import  threading,time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',9999))#绑定
sock.listen(5)#监听5个连接
print 'waiting for connect....'
def tcpLink(sockt,addr):
    print 'Accepet new connect from %s%s'% addr
    sockt.send('Wellcome!')
    while True:
        data=sockt.recv(1024)
        time.sleep(1)
        if data=='exit'or not data:
            break
        sockt.send('Hello %s'%data)
        sock.close()
        print 'connect from %s:%s close'%addr
while True:
    socketA, address=sock.accept()
    t=threading.Thread(target=tcpLink,args=(socketA,address))
    t.start()
