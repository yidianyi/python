#-*-coding:utf-8 -*-
#中文必须指定编码,添加上面的语句
#!/usr/bin/env python #告诉linux/mac 这个是可执行python程序

print '***************输入输出*******************'
def test():
    read = raw_input('请输入名字:')
    print  "hello",read
#test()

print "test ok"

print '***************if else语句***************'
i=0
i=4+90
if i>100:
    print (-i)
elif i>90:
    print '三方'
else:
    print (i)

print " test ok"

print  "****************循环while*****************"

i=19
while i>0:

    print i
    i-=1
print "*********************循环for****************"
list=['好','寻路']
for x in  range(0,3):
    print x
    for y in list:
        print y



print  "=========数据类型 整型 浮点型 bool 字符串 常量 变量 空============"
#字符串 注意与c字符串不同改变a ,b不会变  多行'''  '''   多行原格式 r'''  ''''
a="字符串"
b=a
a="i' shfl"
print a,b

print (''' 多行格式''
\n执行''')
print (r'''多行原格式''
\n不执行''')

#常量大小字母开头
P=3.1415926
#整型
i =3
#浮点型
f=3.0
#bool类型,区分大小写
t=True
f =False
#空
print (None)

print "------------------------与或非 and or not--------------------"
if not None:
    if False or True:
        if False and True:
            print '3'
        print '2'
    print '1'

print '****************数据类型转换********************************'
name="数据类型转换"
print int("12")
print float('12.4')
print str(31)
print int(12.53)
print unicode('111')
print bool(1)
print bool('2')
print bool('')
print bool(0)


print '*************字符串和编码*********************'

#asiic 码与字符  的转换//python3.x默认' '和u' '为unicode
print (chr(65))
print (ord('A'))
#u' ' 使用unicode 4个字节 utf-8可变的 ,1个字节为单位,但可以变长,根据字符选择1-6个字节
ui= u'法'
utf=ui.encode('utf-8')#编码为utf-8
l=len(utf)
print 'unicode转utf-8  ',l,'个utf-8字符'
un =utf.decode('utf-8')#解除utf-8编码,为原来编码
l=len(un)
print 'utf-8转unicode  ',l,'个unicode字符'
print len("法")

#格式化
print '1+3=%d'%(1+3)
print  'today is %s, hello %s' %('m','小白')
print  '1%%2=%d' %(3%2)



#使用list  []
print '*************列表 [value]******************'
list=['a','V','3']
print list
list.insert(1,'41')
print list
list.append([1.0,True,'1'])
print list
list.pop(0)
print list
list[2]='51'
print list
print list[0]
print list[-1]
print list[-1][1]
print len(list)

print "***********元组 (value)********************"
#元组 tuple    () 只有一个元素时(1,) ,与list类似,但初始化后不能修改,所有少了一些方法
t=('哈哈','呵呵',1,'2',True,('6',7,'8'),['list',1,'9'])
print t
print t[0]
print t[5][2]
t[6][0]='change' #list可以改变
print t.index(1)#获取字符的下标
print t[-1].index(1)
print len(t)

print '***********字典 {strKey:value}*********************'
#key 为不可变对象,字符串也是不可变对象,所以通常使用字符串为key
name="字典dict"
dit={'1': 10,'one':12,2:'20'}
print dit
print dit.has_key(2)
dit.pop(2)
print dit
print dit.get('1')
dit['one']=223
print dit
dit['name']='good'
print dit



print '*******************无序不重复集合 set()***************************'
s=set([1,2,3,3,4,5])
print s
s1=set({'shfl':1,'shf':1,'hslf2':3}) #不存储 值
print s1
jiaoji= s & s1
print jiaoji
bingji = s|s1
print bingji

print'***********导入模块 import*****************'
import math

#调用函数
print math.fabs(-12)
print abs(-32)
print '*************函数r1,r2 = fun(i,j=3,*tuple,**dict)************************'
#函数定义 ,空函数 使用 pass 表示什么都不做 也可以用在if  for 等空操作
def nop():
    pass

#参数类型检查
def checkType(i):
    if not isinstance(i,(float,int)) :
        raise TypeError('类型不是整型或浮点型')
    return True
#checkType('3')
checkType(2)

#默认参数,且为不可变对象字符串和基本类型,空等 ,默认参数也是个变量,会储存传入参数,如z=[],这次对z进行添加元素,下次调用,z就含有上次添加的元素
def power(i,z=2):
    if not isinstance(i,(int,float))or not isinstance(z,(int,float)):
        raise TypeError('类型错误')
    print  i**z

power(3)
power(3,3)
#power('2')
#power(3,'上海市')

#可变参数 *参数 .实际是传入tuple
def sum1(*number):
    s=0
    for x in number:
        s = s+x
    print s


sum1(1,3,45,67,3)
t=(3,52,52)
sum1(*t)
sum1()

#关键字参数 **参数  实际是一个字典 传参数使用 key=value或传入  **字典
def person(name,age,**other):
    print name,age,'岁','other',other

person('xiaoming',33)
person('xianghei',34,city='shanghai')
dit={'key':'value'}
person('xsd',42,**dit)
person('sdxs',234,**{'sleep':43})

#多个返回值
def add(i,j):
    return i+1,j+2
a,b= add(2,4)
print a,b
t=add(3,4)
print t
a,b=(23,53)
print a,b



print '*******************高级特性***********'

print '-----切片 [开始:结束:下标增量]----'
list = range(0,20)
print list
t = (0,3,'sl','df','s')
s='请问如题哦一片;啊看到几号回来给你,bvxzv'
print t
print list[:]#整个list
print list[1:]#下表为2到最后
print list[2:4] #取下标2开始,4-2个
print list[-6:-1]#取下标倒数第2开始,-1- (-2)个       -1为最后一个
print list[0:-1:2]#重每次下标加2再取数据
print list[::2]#每次下标加2再取数据
print s[-5:]
print s[0:3]#注意中文的占字符个数

print '-------迭代for key in dict for k,v in dict.iteritems   for v in list or tuple --------'
list = [0]*10
print list
list = range(0,10)
print list
dit = {'one': 1, 'two': 2, 'three': 3}
print dit
s = 'Abs'
for c in s:
    print c
re = 0
for lis in list:
    re = re + lis
print re
for index, v in enumerate(list): #enumerate(list) 转换为(下标,value),..
    print index,v
for k in dit:
    print k
for k,v in dit.iteritems():
    print k,v

print '*****判断是否可迭代 isinstance(s , Iterable)***'
from collections import  Iterable
print isinstance(s , Iterable)
print isinstance(dit,Iterable)
print isinstance(list,Iterable)
i=123
print isinstance(i,Iterable)

c=[(1,3),(2,4),(5,7),(6,8)]
if isinstance(c,Iterable):
    for x,y in c:
        print x , y

print  '**********列表生成式 [初始化值表达式 for条件表达式] **********'
list=[i**2 for i in range(0,5) if i%2==0]
print list
list=[i*v for i in list for v in list]
print list
dit = {'one':1,'two':2,'three':3}
list = [s.upper() for s in dit if s=='two']
print list
list = [k+str(v) for k,v in dit.iteritems() if v==2]
print list

print '***********生成器 1. (初始化值表达式 for表达式)  2.  含有yield()的方法***********'
#生成器好处:不是一次性初始化全部,当使用到时才使用表达式创建 省内存
#创建方法1
t =(i**3 for i in range(1,5))
print t
for x in t:
    print x

#创建方法2
print '****yield**'
def g(*li):
    print li
    list = []
    for i in li:
        list.append(i**2)
        print list.pop()
        yield () #运行到此处让出执行时间,直到外部调用.next()时继续执行
    return
list1=[11,2,3,4,5]
ger = g(*list1)
for x in range(0,5):
    ger.next()

print '***************函数式编程 ************'
print '--函数名是变量 可以赋值,可以传递-------'
def printf1(i):
    print abs(i)
def f(i):
    print i

f(-1)
printf1(-1)
f,printf1 = printf1,f
f(-11)
printf1(-11)

def func(i,function):
    function(i)

func(-123,f)
func(-123,printf1)

print '--------------map()/reduce()'
print 'map(f,[]) 映射 ,x属于[...] 执行f(x),返回结果列表 '
def q(i):
    return i**2

l= map(q,[x for x in range(1,9)])
print l

print'reduce(f,[]) x,y属于[...],1.第一次从列表中pop() 2个作为参数,2.结果作为第一个参数,3.从列表中取出一个作为第二个参数,在重复第2步,最后返回值'
def f(x,y):
    return x+y
r = reduce(f,[x for x in range(0,5)])
print r

print'-----------filter()---------------------'
print 'filter(f,[]) 筛选序列 x属于[...],执行f(x) 结果为Ture不改变,执行结果为False,从列表中删除x '
def f(i):
    if i in range(0,10):
        return True
    else:
        return False
l = [1234,1,2,4,123,43,5,667]
r =  filter(f,l)
print r

print'---------------sorted()---------------'
print'sorted([],f)排序 ,根据f(x,y)的结果排序,返回 1 时交换位置'
l = [2,34,1,3,6,5,4,22]
print l
print sorted(l)
def comp(x,y):
    if x < y:
        return 1
    elif x>y:
        return -1
    else:
        return 0
print sorted(l,comp)

print '-----------返回函数------------------'
print'1.闭包,其内部定义的局部变量,返回函数可以使用 ,返回函数不立即调用'
def f():
    fs=[]
    for s in range(1,4) :
        def g():#不执行,只是声明定义
            return s*s #在外部可以使用局部变量s,但是函数不是立即执行,循环变量都迭代完了,为s==3
        fs.append(g)
    return fs  #返回函数列表

x,y,z=f()
print x(),y(),z()

print '以绑定到函数参数的值不会变,在外面添加一层'
def f():
    ls = []
    for s in range(1,4):
        def tmp(s): #函数参数的值不会变
            def g():
                return s*s
            return g
        ls.append(tmp(s))#依次调用tmp(1),tmp(2),tmp(3) 并把返回的g函数添加到列表
    return ls

x,y,z=f()
print x(),y(),z()


print '------------匿名函数 lambda -----------------------'
f1=lambda x:x*x
print f1(31)

print '-----------装饰器 -----------------------------'
print '1,定义一个包装函数 2,在需要包装的函数的定义前加 @包装函数名'
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call func %s'%(func.__name__)
        return func(*args,**kw)
    return wrapper

def now():
    print '2015-5-5'

now =log(now)#返回wrapper函数给now
now()



#简写
def log(func):   #1 定义一个包装函数
    @functools.wraps(func) #更改wrapper的 __name__属性为被包装的__name__
    def wrapper(*args,**kw):
        print 'call func %s'%(func.__name__)
        return func(*args,**kw)
    return wrapper

@log          #2 在此处声明,实际执行now =log(now)
def now():
    print '2015-5-5'
now()


#带参数的
def func(text):
    def f(func):
        @functools.wraps(func)
        def werpper1(*args,**kw):
            print '狼多肉少',text
            return func(*args,**kw)
        return werpper1
    return f


@func('xiaom')
def now1():
    print '111111111'

now1()



print '----------偏函数-------------'
print ' 返回一个修改了函数默认参数的函数'
import functools
print int('101010')
print int('101010',2)
int2 = functools.partial(int,base=2)
print int2('101010')


print '************模块*****************'
print '''一个abc.py文件就是一个模块名为abc
如果文件名冲突,就把文件放到不同的文件夹下,那么模块名变成 文件夹名.abc
注意每层文件夹下要有 __init__.py文件,否则,无法找到abc.py文件,可以多层文件夹'''

print '''
                          模块格式
#!/usr/bin/env python              #第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-            #第2行注释表示.py文件本身使用标准UTF-8编码

' a test module '                #第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = '小白'                    #第6行使用__author__变量把作者写进去

import sys                         #导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

def test():
    args = sys.argv               #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':                   #运行.py文件时解析器会把__name__置为__main__ 执行test(), import 模块时,__name__属性的值解析器不会改变,不执行test()
    test()
'''


print'---------------------模块别名-- import  ... as ... -------------------------'
try:
    import cStringIO as StringIO  #cstringIO 的别名为StringIO ,代码里只用StringIO
except ImportError:              #导入cstringIO失败时捕获到错误
    import StringIO              #执行导入StringIO



print'-------------------**********作用域******---------------------------------'
print'python没有限制变量的访问,但我们应该遵守以下习惯:用 _ 来区分'
print'_变量名 or __变量名 :私有变量     变量名:公有变量   __变量名__:特殊变量 可以被引用 '
import  sys
import  test

def m():
    test.test()
    test._p()#一般不应该使用,这是模块内部调用
    test._private #一般不应该使用
    test.i


print'-------------安装第三方库---pip or easy_install-------------------'

print'命令行下 pip install 库名 ,库的名称，可以在官网或者pypi上搜索'
#命令行 pip install PIL --allow-external PIL --allow-unverified PIL
#或命令行 easy_install PIL
import Image

im = Image.open('1.png') #打开一张图片
print im.size,im.mode,im.format
im.thumbnail((200, 50)) #制作缩略图
im.save('thumb1.jpg', 'JPEG')#保存

#assert isinstance(im, object) #插入这句,可以出现代码提示


print '模块搜索路径,Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：'
print sys.path
sys.path.append('C:\HOME\Python27\Lib\site-packages\PIL') #添加搜索路径,这种方法是在运行时修改，运行结束后失效,第二种方法是设置环境变量PYTHONPATH。
print sys.path



print '-------------__future__模块----------------------'
print "Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性"
print '新版特性测试'
import  test__future__

test__future__.test()



print '**************面向对象编程************************'

print '--------类-------------------'
class Person(object):  #定义如果没有父类,那么都继承object
    static = 12                    #类属性
    s_i = 0
    def __init__(self,name,age):  #self ,永远为第一个参数(解析器填写),用例绑定成类属性 成员 方法
        self.__name=name          #__开头的变量为私有
        self.__age=age            #实例属性self.xxx
        self.count=0
    def __set(self,tmp):          #私有方法
        self.__name=tmp
    def getName(self):            #public
        return self.__name
    def setName(self,tmp):        #public
        self.__set(tmp)
    def do(self):
        print 'Pesion do()'

p = Person('小马',33)
print Person.static ,'类属性'
p11=p
p11.other='p11对象有other属性,p对象没有,这与静态语言不通,python的类对象可以添加自己独有的属性'
print p11.other #p没有other属性
p1 = Person('xiaom',24)
print p.getName(),p1.getName(),p11.getName()
print p.count,p1.count
p.count=10
print p.count ,p1.count

def friendFunction():
    print '外部定义函数'
p.func=friendFunction #绑定方法
print p.getName()
p.func()

print '---------继承-----------'
class Studen(Person): #继承person
    def __init__(self,name,age,score):
       self.score=score
       super(Studen, self).__init__(name,age) #父类初始化
    def do(self):
        print 'Studen do'
    def display(self):
        print self.score,self.getName()
s = Studen('小沙',23,88)
s.display()

print '------多继承------'
class Test(object):
    def dotest(self):
        print'考试中'

class studentsAndTeacher(Studen,Test):
    def __init__(self,name,age,score):
        super(studentsAndTeacher, self).__init__(name,age,score)
    def dip(self):
        print self.getName()
        self.dotest()


str1 = studentsAndTeacher('ss',32,8)
str1.dip()

print '---------多态------------------'
class Teacher(Person):
    def __init__(self,name,age):
        super(Teacher, self).__init__(name,age)
    def do(self):
        print 'Teacher do'

def watch(ww):
    print  ww.getName()
    ww.do()


w = watch(Teacher('小细',24))
w = watch(Studen('xioa ',11,88))

print'-------------获取对象信息------------------------'

print '1.--type()--'
a=Teacher('xs',23)
def func():
    pass
f = func
print  type(f)
print type(123)
print type('123')
print type(12.5)
print type(abs)
print type(a)
print type(int)
print type(float)
print type(Teacher)

import  types         #Python把每种type类型都定义好了常量，放在types模块里
print ' type(123)==types.IntType     ',type(123)==types.IntType
print 'type(\'123\')==types.UnicodeType',type('123')==types.UnicodeType


print '2------isinstance()----------'
print '判断继承关系方便'
print type(Teacher('ss',32))
print isinstance(Teacher('ss',23),(Person))
print isinstance(Teacher('ss',23),(Teacher))
print isinstance(Teacher('ss',23),(Studen))
print isinstance(Teacher('ss',23),(Person,Teacher))
print isinstance(Teacher('ss',23),(Person,Studen))

print '3-----dir()-----------------'
print '获取对象的方法和属性,返回的是一个list'
print dir('123')
print dir(dict)
print dir(Teacher('ww',12))
print '对象的__xxx__方法实际是xxx(object), \'123\'.__len__()等于 len(\'123\') ?', '123'.__len__()== len('123')


print '把属性和方法列出来，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态,一般不这么操作,除非不知道对象信息'
class unknow(object):
    def __init__(self):
        self.name='ms'
        self.result='22'
    def func(self):
        print 'function sss'

l = unknow()
print dir(l)

def t():
   print hasattr(l,'name')
   att = getattr(l,'name','没有该属性返回默认值')
   print att
   att1 = getattr(l,'sfsfsf','没有该属性返回默认值')
   print  att1
   if hasattr(l,'result'):
       setattr(l,'result',2345)
       print getattr(l,'result')
   if hasattr(l,'func'):
       f=getattr(l,'func')
       f()
t()

#正确用法,假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取
def readData(fd):
    pass
def readImage(fd):
    if hasattr(fd,'read'):
        return readData(fd)


print '***********面向对象高级编程********************'

print '----没有指定__slots__属性,可以任意动态添加属性---------------'
class F(object):


    pass

f=F()
f.name='动态添加实例属性'
f.fuc=lambda x:x**2
print  f.name
print f.fuc(2)
F.count='动态添加类属性'
print F.count

print '------指定__slots__ 变量 只能动态添加指定属性--------'
class F1(object):
    __slots__=('name','age') #只能动态添加的属性,

f1=F1()

'''
f1.count=1 #错误 AttributeError: 'F1' object has no attribute 'count' '''
f1.name='name在__slots__中可以动态添加'
print f1.name



print '*********************@property 把方法变成属性********************'

class func(object):
    @property         #把name方法 变成 name属性的读方法 ,内部储存变量 self._name
    def name(self):
        return self._name  #获取语句,
    @name.setter      #把name方法 变成 name属性的写方法
    def name(self,value):
        self._name=value  #赋值语句



t=func()
t.name='123'
print t.name


print '***************定制类***************************'
print'使用class中的特殊属性__xxx__ 可以定制类'

print '---------__str__--------------'
class Customer():
    def __init__(self,*argv):
        self.__name = argv
    def __str__(self): #打印对象时调用
        return 'Customer object (name:%s)'%(self.__name)
    __repr__ = __str__   #调试(隐式调用)时调用__repr__()
cus= Customer('小马')
print cus #没重写__str__  之前输出<__main__.customer instance at 0x0230F828>
          #重写__str__ 之后输出  Customer object (name:小马)


print '------------__iter__-----------------------'
''' 如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。'''

class mylist(object):
    def __init__(self):
      self.a,self.b=1,1
    def __iter__(self):
        return self #返回自己
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a>100000:  #退出条件
            raise StopIteration()
        return self.a #返回下个值

l=mylist()
for x in l:
    print x
print isinstance(l,Iterable)

print  '-------__getitem__-----------------'
''' 可以使用[x]获取子项,类似重载[]运算符'''

class Mylist(object):
    def __getitem__(self, item):
        self.a,self.b=1,1
        for i in range(0,item):
            self.a,self.b = self.b,self.a+self.b
        return self.a

l = Mylist()
print l[15]


print'----------__getattr__--------------'
print '当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, \'score\')来尝试获得属性'

class My(object):
    def __init__(self):
        self.path=''
    def __getattr__(self, item):
        if item =='user':
            return '没有该属性'

l = My()
print l.user

class GetApi(object):
    def __init__(self,path=''):
        self.path=path
    def __getattr__(self, item):
        return GetApi('%s/%s'%(self.path,item))
    def __str__(self):
        return self.path
    __repr__ =__str__
    def __call__(self, item):
        return GetApi('%s/%s'%(self.path,item))

l= GetApi().status.user.timeline.list
print l
s=GetApi().users('hello').repos
print s


print'-----__call__--------------'
print'我们用instance.method()来调用。使用__call__()直接在实例本身上调用.类似instance(),类似重载()运算符'
class fun():
    def __init__(self,name):
        self._name=name

    def __call__(self): #
        print '__call__  do name is %s'%self._name

ins = fun('xxx')
ins() #会调用__call__()函数

print'判断对象是否可调用 callable(ins) ',callable(ins)
print callable(Teacher('sss',32))


print '-----------------使用元类----------------------------------'
print r'''动态创建一个类type('类名',(父类1,...),dict(属性名=属性实现,方法名=方法实现))'''

def fn(self):  #注意第一个参数为self
    print'动态创建类,并绑定方法属性'

MyClass = type('MyClass',(object,),dict(myfunc= fn,name='笑吧'))
l=MyClass()
l.myfunc()
print l.name




print'-------------__metaclass__------------------------------'
print '''先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。
换句话说，你可以把类看成是metaclass创建出来的“实例”。

当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，
它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合。'''
class my_list(object):
    def __init__(self):
       self.L=[]
    def append(self,value):
        self.L.append(value)


class ListMetaclass(type):#一定要继承type,因为要调用type动态创建类
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)#动态添加add()方法
        attrs['getList']=lambda self: self.L
        return type.__new__(cls,name,bases,attrs)



class Mylist(my_list):
    __metaclass__ = ListMetaclass #实例对象时,会调用ListMetaclass.__new__()
    def my(self):
        print 'mylist'

myl=Mylist()
myl.add(1)
print myl.getList()
myl.my()

print '----编写简单ORM------'

class Filed(object):
    def __init__(self,name,typee):
        self.name=name
        self.type=typee
    def __str__(self):
        return '<%s,%s>'%(self.name,self.type)

class IntergerFied(Filed):
    def __init__(self,name):
        super(IntergerFied, self).__init__(name,'bigint')

class StringField(Filed):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')

class ModeMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        mappings=dict()
        for k,v  in attrs.iteritems():
            if isinstance(v,Filed):
                print 'found mappings %s===>%s '%(k,v)
                mappings[k]=v
        for key in mappings.iterkeys():
            attrs.pop(key)
        attrs['__table__']=name
        attrs['__mappings__']=mappings
        return type.__new__(cls,name,bases,attrs)
class Model(dict):
    __metaclass__ = ModeMetaclass #动态创建Model类
    def __init__(self,**kw):      #初始化Model类
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key]=value

    def save(self):
        fileds=[]
        params=[]
        args=[]
        for k,v in  self.__mappings__.iteritems():
            fileds.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)'%(self.__table__,','.join(fileds),','.join(params) )
        print 'SQL: %s'%sql
        print 'ARGS: ',args



class User(Model):
    id = IntergerFied('id')
    name =StringField('name')
    email=StringField('email')
    password=StringField('password')


user=User(id=123,name='xiaom',email='xxx@xxx.xxx',password='xxsx')
user.save()


print '*************错误 调试 测试**************************'

print'-----捕获错误-------------'
print 'try except finally'
def dev(a):
    try:
        10/int(a)
    except ZeroDivisionError:
        print '除数不能为零'
    finally:
        print'一定会执行的'
    print '继续执行  end'

dev(1)
dev(0)


def dev1(a):
    try:
        10/int(a)
    except ZeroDivisionError:
        raise ValueError('--除数不能为零')

try:
    dev1(0)
except ValueError,e:
    print  str(e)



print '---------调试---------------------------------'
name='xx'
assert name=='xx','不相等会抛出AssertionError 终止程序'

import logging
logging.basicConfig(level=logging.DEBUG)#设置日志等级
logging.info('日志信息输出')
logging.warning('警告信息')#次最高级
logging.error('错误信息')#最高级
logging.debug('调试信息') #最低级


print'-----------单元测试---------------------'


import unittest              #导入测试模块
from myunitstest import Dict #导入被测试模块

class TestDict(unittest.TestCase): #创建测试类,要继承unittest.TestCase
    def setUp(self):
        print 'setUp...进入测试前运行'

    def tearDown(self):
        print 'tearDown...退出测试运行'

    def test_init(self):           #创建测试方法,要以test开头的方法就是才是测试方法,否则不会执行
        d=Dict(b=2,c=45,s=s)       #测试操作
        self.assertEqual(d.b,2)
        self.assertEqual(d.c,45)
        self.assertEquals(d.s,s)
    def test_key(self):           #测试方法
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):         #测试方法
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):  #测试方法
        d = Dict()
        with self.assertRaises(KeyError): #断言就是期待抛出指定类型的Error
            value = d['empty']           #通过d['empty']访问不存在的key时，断言会抛出KeyError

    def test_attrerror(self): #测试方法
        d = Dict()
        with self.assertRaises(AttributeError): #而通过d.empty访问不存在的key时，我们期待抛出AttributeError
            value = d.empty


print '运行单元测试 方法1 命令行通过python  -m unittest hello  直接运行单元测试'
'''方法2
if __name__ == '__main__': #
    unittest.main()
'''

print '-------文档测试---------------------------'
'''Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
例如docTest.py文件

命令行运行 python docTest.py
'''


print '*************IO编程******************'
print '同步'


print '-----文件读写--------------'
name='test.txt'
try:
    print '打开文件'
    f=open(name,'r') #r 只读 ,r+可读写,若文件不存在报错, w+可读写,若文件不存在,就创建
except IOError:
    print '文件不存在,新建中..'
    f=open(name,'w')
    print'打开成功'
else:
    print '读取文件内容:' ,f.read()
    f.close()
    print'关闭文件'
finally:
    print'结束'

print '读文件'
try:
    f = open(name, 'r')
    print f.read()
    f.read()
finally:
    if f:
        f.close()

#Python引入了with语句来自动帮我们调用close()方法：
with open(name,'r') as f:
    #print f.read()#读取所有字节
    #print f.read(1)#读取一个字节
    #print f.readline()#读取一行
    #print f.readlines()#读取所有行 返回list

    for l in f.readlines():
        #print l #带有\n
        print l.strip()


print '读取二进制文件'
with open('1.png','rb') as f:
    l=f.read()
    print l

print '字符编码'
import codecs
print ''
with open('gb232.txt','rb') as f:
    l= f.read()
    print isinstance(l,unicode)
    print l
    lc = l.decode('gbk')
    print isinstance(lc,unicode)
    print lc

with codecs.open('gb232.txt','r','gbk') as f:#利用codecs 直接读出unicode
    l= f.read()
    print isinstance(l,unicode)
    print l
print '写文件'
with open(name,'a') as f: #a或ab 追加模式
    print f.tell()
    f.write('100 ')
    f.write('hao123 ')
    f.writelines('name1')
    print f.tell()
with open(name,'r') as f:
    print f.read()

print '操作文件和目录'

import os #与系统相关的模块 nt 是window posix 是unix linux mac
print  os.name #系统名字
#print  os.uname()#系统详细信息 window不支持
print os.environ#环境变量


l = os.path.abspath('.')
print '查看当前绝对路径',l
p = os.path.join(l,'newdir')
print '拼接创建目录的路径',p
print '创建目录'
try:
    os.mkdir(p)
except WindowsError,e:
    if e.args==(183,''):
        os.removedirs(p)


l=os.path.abspath('test.txt')#获取文件绝对路径
print '获取文件的绝对路径',l
p=os.path.split(l) #分割文件名和文件夹路径
print '%s 文件路径 %s  文件名 %s'%(p, p[0],p[1])
t=os.path.splitext(p[1])#分割文件和后缀
print '%s 文件名无后缀 %s  后缀 %s'%(t,t[0],t[1])

print '重命名'
try:
    os.rename('test1.txt','1.txt')
except WindowsError ,e:
   if e.args==(2,''):
        os.rename('1.txt','test1.txt')

print '删除'
try:
    os.remove('remove')
except WindowsError:
    p=os.path.join(os.path.abspath('.'),'')
    logging.info('%s',p)
    with open(p+'remove','w'):
        print'创建'
print '文件复制 ,移动'
import shutil
try:
    shutil.copy('1.png','1_copy.png')
    shutil.move('1_copy.png','test/1_copy.png')
    os.remove('t')
except IOError:
    pass
except WindowsError:
    shutil.copy('1.png','t')
    pass
print '异步'

print '查看文件夹内容'
l = os.listdir('.')
print  l
print '当前路径查找出所有文件夹'
p= [x for x in os.listdir('.') if os.path.isdir(x)]
print p
print '找出当前文件夹所有py文件'
py =[x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py' and os.path.isfile(x)]
print py

print  '查找指定目录下的某个文件'
#print [x for x in os.listdir('.')  if os.path.isdir(x) for x in os.listdir(os.path.abspath(x))  os.path.isfile(x) and str(x).find(test)>=0 ]

def seach(myPath,text):
    for nextpath in os.listdir(myPath):
        if os.path.isdir(os.path.join(myPath,nextpath)):#注意要判断的条件,不能只判断nextpath
            seach(os.path.join(myPath,nextpath),text)
        elif text in nextpath :
            print os.path.join(os.path.abspath(myPath),nextpath)

seach('.','1')

if not os.path.isdir('ccc'):#只是判断程序所在的那层目录有没有ccc文件夹
    print 'ccc 被认为不是文件夹'
if os.path.isdir(os.path.join('.','ccc')):
    print 'ccc是文件夹'
if os.path.isdir('test'):
    print 'test 是文件夹'




print '-------------序列化---------------'
'''我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等'''


try:
    import cPickle as Pickle
except ImportError:
    import cPickle

d=dict(a=123,b=456,c='789')
dl = Pickle.dumps(d) #打印序列化后的对象
print dl,'序列化'
dld = Pickle.loads(dl)
print dld,'恢复'
with open('Pickle_dumps.txt','wb') as f:
    Pickle.dump(d,f)    #从内存中写入文件

with open("Pickle_dumps.txt",'rb') as f:
    dd=Pickle.load(f)  #从文件中写入内存

print dd ,'从文件读取的序列化对象'


print '----------JSON------------'
import json
js=dict(y=123,age=456,sf=38)
j= json.dumps(js)
print j
print json.loads(j)

print 'Json 进阶'
class students(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

def studensToDict(std):#转换函数
    return {'name':std.name,
            'age': std.age
            }
print json.dumps(students('xxx',11),default=studensToDict)

jsl= json.dumps(students('xiao',23) ,default=lambda obj:obj.__dict__  ) #转成字典再序列化
print jsl

#恢复
def dictToStudents(d):
    return students(d['name'],d['age'])
rjsl= json.loads(jsl,object_hook=dictToStudents)
print rjsl.name,rjsl.age,rjsl


print '***************进程和线程***************************'
'''多线程  多进程   多进程+多线程'''

'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
'''
'''
#window 没有fork()
import os
print ('prossing %s starting'%(os.getpid()))
p=os.fork()
if p==0:
    print  '我是子进程%s,我的父进程是%s'%(os.getpid(),os.getppid())
else:
    print '我 %s 刚创建了一个子进程 %s'%(os.getpid(),p)

'''
'''
#因为该文件有其他代码会执行多次次代码所以独自写在一个文件中
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
'''

print'多进程例子 见mulProcess.py'

print '进程池 见 mypool.py'

print '进程间通信Queue Pipes myQueue.py'

print  '多线程'
'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用threadfun命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
'''

import  threading,time
def threadfun(): #线程执行操作
    print '%s thread is running ...'%threading.current_thread().name
    n=0
    while n<5:
        n+=1
        print '%s thread ====>%s'%(threading.current_thread().name,n)
        time.sleep(0.5)

    print '%s thread end'%threading.current_thread().name

print '%s thread is running...'%threading.current_thread().name

thr=threading.Thread(target=threadfun,name ='threadfun')
thr.start()
thr.join()
print '%s thread end'%threading.current_thread().name


'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''
print '------Lock---'


import  threading,time
balance=0 #定义全局变量,线程共享
def changeit(n):
    #理论上balance 一直为零,但这是多线程中
    global balance
    balance=balance+n
    balance=balance-n
def thread_run(n):
    for i in range(100000):
        changeit(n)


thr1=threading.Thread(target=thread_run,name='thread_run1',args=(5,))
thr2=threading.Thread(target=thread_run,name='thread_run2',args=(8,))
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print balance,'无lock,值被修改' #每次运行结果多不同,被改了

'''使用lock'''
import  threading,time
balance1=0 #定义全局变量,线程共享,进程是每个自己一份
lock=threading.Lock() #定义线程锁
#print dir(lock),help(lock)#查看帮助
def changeit(n):
    #理论上balance 一直为零,但这是多线程中
    global balance1 #声明使用全局变量
    balance1=balance1+n
    balance1=balance1-n
def thread_run(n):
    for i in range(100000):

        lock.acquire()#上锁
        try:
            changeit(n)
        finally:
            lock.release() #解锁

thr1=threading.Thread(target=thread_run,name='thread_run1',args=(5,))
thr2=threading.Thread(target=thread_run,name='thread_run2',args=(8,))
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print balance1,'有lock 正常'

'''多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。'''
print '----ThreadLocal-------'
'''线程应使用局部变量,因为只有线程自己本身见,不会影响其他线程,而全局变量的修改必须加锁
而线程局部变量在函数调用不方便,有没有一个全局的变量,所有线程都可以访问,但访问的是对应自己的线程局部变量?
理论:使用一个全局自动,字典的key 为线程的名字,那么根据线程名就可以存取自己的变量,实现就是ThreadLoacl
'''
import threading,random
G_local=threading.local() #定义一个全局的线程局部变量
def pross_studen():
    print 'hello %s age %s (in %s)'%(G_local.student,G_local.age,threading.current_thread().name)

def process_thread(name):
    #绑定ThreadLocal的studen
    G_local.student=name
    G_local.age=random.random()
    pross_studen()

t1=threading.Thread(target=process_thread,args=('xxx',))
t2=threading.Thread(target=process_thread,args=('zzz',))
t1.start()
t2.start()
t1.join()
t2.join()
'''
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
'''

print '-------------线程vs进程---------------'
'''
多进程和多线程，这是实现多任务最常用的两种方式。现在，我们来讨论一下这两种方式的优缺点。

首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

线程切换

无论是多进程还是多线程，只要数量一多，效率肯定上不去，为什么呢？

我们打个比方，假设你不幸正在准备中考，每天晚上需要做语文、数学、英语、物理、化学这5科的作业，每项作业耗时1小时。

如果你先花1小时做语文作业，做完了，再花1小时做数学作业，这样，依次全部做完，一共花5小时，这种方式称为单任务模型，或者批处理任务模型。

假设你打算切换到多任务模型，可以先做1分钟语文，再切换到数学作业，做1分钟，再切换到英语，以此类推，只要切换速度足够快，这种方式就和单核CPU执行多任务是一样的了，以幼儿园小朋友的眼光来看，你就正在同时写5科作业。

但是，切换作业是有代价的，比如从语文切到数学，要先收拾桌子上的语文书本、钢笔（这叫保存现场），然后，打开数学课本、找出圆规直尺（这叫准备新环境），才能开始做数学作业。操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。

所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

计算密集型 vs. IO密集型

是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。

计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

异步IO

考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单进程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。
'''

print '-------分布式进程 -------------'
'''
在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：



例子 Service.py 服务器
     addTask.py 连接服务器,添加任务到queue中,从一个requeue接收任务结果
     client.py 连接服务器,从queue中获取任务,处理后,将结果添加到requeue中
     client1.py 连接服务器,从queue中获取任务,处理后,将结果添加到requeue中
'''

print '**************正则表达式*****************'

import re
















'''
print '**************初学者17个技巧***************'
print '----- 交换------'
x=3
y=34
x,y=y,x
print x,y

print '----- if 语句在行内------'
print 'hello'if False else 'Wind'

print '----- 连接------'
#list tuple可以
n=['sssss','jjjj','kls']
m=['ssss1','sldkfj','ksjf']
f=n+m
print f
print str(3)+'sk'

print '-------计数技巧------'
print 10**2 #10的2次方
print 3.0//2  #无进位取整
print 0.3/0.1
print 0.3//0.1 #结果为2 浮点运算不准确

print '-----------数值比较---------'
x = 49
if  2< x <50:
    print x
if 2> x <50:
    print x
'''