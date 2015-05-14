#-*-coding:utf-8-*-
from wsgiref.simple_server import make_server
from helloWeb import application  #自己实现的处理接口函数

http=make_server('',8000,application) #服务器地址,端口号,处理函数
print 'Service Http on prot 8000...'
http.serve_forever()

#启动,并在浏览器输入http://localhost:8000/Python