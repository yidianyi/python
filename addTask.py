#-*-coding:utf-8-*-
from multiprocessing.managers import BaseManager
import random,time
class QueueManager(BaseManager): pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_queue')
QueueManager.register('get_requeue')
m = QueueManager(address=('127.0.0.1', 50000), authkey='abracadabra')
m.connect()#连接服务器
queue = m.get_queue()#获取Queue对象
for i in range(100):#添加任务
    n=i
    queue.put(n) #添加到queue中
    print ('put %s to queue'%n)

requue = m.get_requeue()
for i in range(100):
    time.sleep(0.5)
    v=requue.get() #从requeue 对象中获取值
    print  ('%s get %s from requeue'%(i,v))
