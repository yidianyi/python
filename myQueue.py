#-*-coding:utf-8-*-
'进程间通信'
'''以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据'''
from multiprocessing import Process,Queue
import os,time,random
#写进程操作
def writeTo(q):
    for i in [1,4,3,666,78,334,45]:
        print 'put %s to queue'%i
        q.put(i)
        time.sleep(random.random())
#读进程操作
def readFrom(q):
    while True:
        value= q.get(True)
        print 'get %s from queue'%value

if __name__=='__main__':
    q=Queue() #创建通信对象
    readp=Process(target=readFrom,args=(q,))
    writep=Process(target=writeTo,args=(q,))
    writep.start() #启动写进程
    readp.start() #启动读进程
    writep.join()#等待写进程结束
    readp.terminate() #终止都进程,因为是死循环

'''
在Unix/Linux下，multiprocessing模块封装了fork()调用，
使我们不需要关注fork()的细节。由于Windows没有fork调用，
因此，multiprocessing需要“模拟”出fork的效果，
父进程所有Python对象都必须通过pickle序列化再传到子进程去，
所有，如果multiprocessing在Windows下调用失败了，
要先考虑是不是pickle失败了。
    '''