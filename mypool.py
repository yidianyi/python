#-*-coding:utf-8-*-
from multiprocessing import Pool
import os,random,time
def long_time_task(name):
    print 'run task %s (%s)'%(name,os.getpid())
    start= time.time()
    time.sleep(random.random()*3)#延时
    end=time.time()
    print 'task %s run %0.2f second'%(name,end-start)
    pass
if __name__=='__main__':
    print 'parent process is %s'%os.getpid()
    m_pool=Pool(4) #创建进程池实例对象,参数为可同时执行进程个数 参数默认为cpu内核个数
    for i in range(7):
        m_pool.apply_async(long_time_task,(i,)) #异步添加
    print '等待所有子进程完成'
    m_pool.close() #关闭进程池,(不能再添加进程),开始pool里的执行进程
    m_pool.join() #等待进程全部完成
    print'所有子进程以完成'
'''
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
调用close()之后就不能继续添加新的Process了。
请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
这是因为Pool的默认大小在我的电脑上是4，
因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：p = Pool(5)
'''