import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp is sock_dgram
soc.bind(('127.0.0.1',9999))
while True:
    data,addr= soc.recvfrom(1024)
    print 'received from %s:%s'%addr
    soc.sendto('hello %s'%data,addr )



