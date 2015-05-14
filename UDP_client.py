import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['1','2','4','5','55','66']:
    soc.sendto(data,('127.0.0.1',9999))
    print soc.recv(1024)
soc.close()