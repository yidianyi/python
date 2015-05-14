#-*-coding:utf-8 -*-
print  '跨平台多进程'
import os
from multiprocessing import Process
print'%s进程----'%os.getpid()
def myProcess(name):#定义子进程操作函数
    print 'run process %s %s '%(name,os.getpid())
print'%s进程****'%os.getpid()
if __name__=='__main__':
    print '父进程是%s'%(os.getpid())
    p= Process(target=myProcess,args=('test',)) #创建子进程,参数为执行函数和执行函数的参数
    print '子进程将开始'
    p.start() #启动子进程,重新从第一行开始执行,但与父进程不同的是它还执行了定义的子进程函数
    p.join() #等到子进程结束,在往下执行
    print '子进程返回'
