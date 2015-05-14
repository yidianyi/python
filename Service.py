#!/user/bin/evn python
#-*-coding:utf-8 -*-

from multiprocessing.managers import BaseManager
import time,random,Queue

#发送队列
taskq=Queue.Queue()
#接受队列
resultq=Queue.Queue()
# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass
# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_queue',callable=lambda :taskq)
QueueManager.register('get_requeue',callable=lambda :resultq)
# 绑定端口5000, 设置验证码'abc':
m=QueueManager(address=('',50000),authkey='abracadabra')
s=m.get_server() #获取服务实例
s.serve_forever()#永久打开服务



