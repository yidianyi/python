#-*-coding:utf-8-*-
import time
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
QueueManager.register('get_requeue')
m = QueueManager(address=('127.0.0.1', 50000), authkey='abracadabra')
m.connect()
queue = m.get_queue()
result= m.get_requeue()
for i in  range(50):
    time.sleep(0.3)
    v= queue.get() #从queue对象获取值
    print('%s client1 get %s from queue do %s *  %s '%(i,v,v,v))
    result.put(v*v) #处理后添加到requeue中