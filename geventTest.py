#-*-coding:utf-8-*-
from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()


print '''
可以看到，3个greenlet是依次运行而不是交替运行。

要让greenlet交替运行，可以通过gevent.sleep()交出控制权
'''

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

'''
3个greenlet交替运行，

把循环次数改为500000，让它们的运行时间长一点，然后在操作系统的进程管理器中看，线程数只有1个。

当然，实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换，代码如下：
'''
from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'http://www.ithome.com/'),
        gevent.spawn(f, 'http://www.hao123.com/'),
        gevent.spawn(f, 'http://www.baidu.com/'),
])

'''
从结果看，3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程。

小结

使用gevent，可以获得极高的并发性能，但gevent只能在Unix/Linux下运行，在Windows下不保证正常安装和运行。

由于gevent是基于IO切换的协程，所以最神奇的是，我们编写的Web App代码，不需要引入gevent的包，也不需要改任何代码，
仅仅在部署的时候，用一个支持gevent的WSGI服务器，立刻就获得了数倍的性能提升。

'''
