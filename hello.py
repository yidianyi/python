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
listVar=['好','寻路']
for x in  range(0,3):
    print x
    for y in listVar:
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
listVar=['a','V','3']
print listVar
listVar.insert(1,'41')
print listVar
listVar.append([1.0,True,'1'])
print listVar
listVar.pop(0)
print listVar
listVar[2]='51'
print listVar
print listVar[0]
print listVar[-1]
print listVar[-1][1]
print len(listVar)

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
listVar = range(0,20)
print listVar
t = (0,3,'sl','df','s')
s='请问如题哦一片;啊看到几号回来给你,bvxzv'
print t
print listVar[:]#整个list
print listVar[1:]#下表为2到最后
print listVar[2:4] #取下标2开始,4-2个
print listVar[-6:-1]#取下标倒数第2开始,-1- (-2)个       -1为最后一个
print listVar[0:-1:2]#重每次下标加2再取数据
print listVar[::2]#每次下标加2再取数据
print s[-5:]
print s[0:3]#注意中文的占字符个数

print '-------迭代for key in dict for k,v in dict.iteritems   for v in list or tuple --------'
listVar = [0]*10
print listVar
listVar = range(0,10)
print listVar
dit = {'one': 1, 'two': 2, 'three': 3}
print dit
s = 'Abs'
for c in s:
    print c
re = 0
for lis in listVar:
    re = re + lis
print re
for index, v in enumerate(listVar): #enumerate(list) 转换为(下标,value),..
    print index,v
for k in dit:
    print k
for k,v in dit.iteritems():
    print k,v

print '*****判断是否可迭代 isinstance(s , Iterable)***'
from collections import  Iterable
print isinstance(s , Iterable)
print isinstance(dit,Iterable)
print isinstance(listVar,Iterable)
i=123
print isinstance(i,Iterable)

c=[(1,3),(2,4),(5,7),(6,8)]
if isinstance(c,Iterable):
    for x,y in c:
        print x , y

print  '**********列表生成式 [初始化值表达式 for条件表达式] **********'
listVar=[i**2 for i in range(0,5) if i%2==0]
print listVar
listVar=[i*v for i in listVar for v in listVar]
print listVar
dit = {'one':1,'two':2,'three':3}
listVar = [s.upper() for s in dit if s=='two']
print listVar
listVar = [k+str(v) for k,v in dit.iteritems() if v==2]
print listVar

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
#pip uninstall PIL 删除  easy_install -m PIL 删除 但还要收动删除egg文件或文件夹
'''
安裝：pip install PackageName

更新：pip install -U PackageName

移除：pip uninstall PackageName

搜索：pip search PackageName

帮助：pip help
'''
from PIL import Image
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
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345') #匹配返回对象
print re.match(r'^\d{3}\-\d{3,8}$', '010 12345') #不匹配返回空

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print 'ok'
else:
    print 'failed'

print '--------------分割----------'
resu = re.split(r'[\s\,]+', 'a,b, c  d')
print resu

print re.split(r'[\s\,\;]+', 'a,b;; c  d')


print '---------分组---------'
'''
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：

^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
'''
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m ,m.group(0),m.group(1),m.group(2)

print '-----预编译匹配表达式---------'
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
用编译后的正则表达式去匹配字符串。
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()


print '*************常用内建模块*****************'
import collections

print '-------------namedtuple---------------------'
'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''
Point= collections.namedtuple('Point',['x','y']) #定义一个点
Point.x =12.0
Point.y =100.0
print Point.x*10,Point.y*0.5
circle=collections.namedtuple('circle',['x','y','r'])
circle.x =10
circle.y=100
circle .r=20
print dir(circle)


print '-------deque-----------'
'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
de=collections.deque(['a','b','c'])
de.append('w')
de.appendleft('1')
print de

print '------defaultdict--------------'
'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
defdict=collections.defaultdict(lambda :'N/A') #设置返回默认值'N/A'
defdict['x']='sds'
print defdict['x'],defdict['2']

print '-----------OrderDict--------------------'
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
'''
myDict=dict()
myDict['z']=1
myDict['y']=12
myDict['1']=89
print myDict
orderDict=collections.OrderedDict()
orderDict['z']=123
orderDict['y']=456
orderDict['c']=33
print orderDict

print '实现FIFO'
class FIFO(collections.OrderedDict):
    def __init__(self,capacity):
        super(FIFO, self).__init__()
        self.capacity=capacity
    def __setitem__(self, key, value):
        containsKey=1 if key in self else 0
        if len(self)-containsKey>=self.capacity:
            last=self.popitem(last=False) #删除最早插入的
            print 'remove ',last
        if containsKey:
            del self[key]
            print 'set ',(key,value)

        else:
            print  'add',(key,value)
        collections.OrderedDict.__setitem__(self,key,value)

f= FIFO(4)
f['a']=1232
f['b']=1236
f['v']=1237
f['bq']=1238
f['nn']=1239
f['a1']=1230
f['a2']=12310
f['a1']=1


print  '------Counter----------'
'''Counter是一个简单的计数器，例如，统计字符出现的个数：
'''

counter=collections.Counter()
for char in 'hlsfsb23232351391034sfsncqrgzc.s':
    counter[char]=counter[char]+1

print counter


print '*****base64********'
'''
Base64的原理很简单，首先，准备一个包含64个字符的数组：
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4小组，每小组正好6个bit：

这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。

所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
'''
import base64
print base64.b64encode('A')
print base64.b64encode('AA')
l= base64.b64encode('AAA')
print l ,base64.b64decode(l)
print base64.b64encode('好23'),len('好23')

'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''
print(base64.b64encode('i\xb7\x1d\xfb\xef\xff'))
urlBase64=base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff') #\xb7 算一个字节
print urlBase64
decode = base64.urlsafe_b64decode(urlBase64)
print repr(decode)


'''
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：

# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'
'''
def safedecode(s):
    s+= len(s)%4*'='
    return base64.urlsafe_b64decode(s)
print  safedecode('YWJjZA')


print'*******struct****************'
'''
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
<
=
!
Format	    C Type	Python type	   Standard size	Notes
x	    pad byte	 no value
c	    char	    string of length 1	1
b	    signed      char	    integer	1	(3)
B	    unsigned    char	    integer	1	(3)
?	    _Bool	    bool	    1	        (1)
h	    short	    integer	    2	        (3)
H	    unsigned    short	    integer	2	(3)
i	    int	        integer	    4	        (3)
I	    unsigned    int	        integer	4	(3)
l	    long	    integer	    4	        (3)
L	    unsigned    long	    integer	4	(3)
q	    long long	integer	    8	        (2), (3)
Q	    unsigned    long long	integer	8	(2), (3)
f	    float	    float	    4	        (4)
d	    double	    float	    8	        (4)
s	    char[]	    string
p	    char[]	    string
P	    void *	    integer	 	            (5), (3)
'''

import struct
print repr( struct.pack('>I', 10240099) )#struct的pack函数把任意数据类型变成字符串

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')#unpack把str变成相应的数据类型

'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。

所以，组合起来用unpack读取：
'''
def checkBmp(path):
    with open(path,'rb') as p:
     tmp=p.read(30)
    print repr(tmp)
    bmp= struct.unpack('<ccIIIIIIHH',tmp)
    print bmp
    if 'B'and 'M' in bmp:
        print ('图片大小: %s X %s ,颜色数:%s '%(bmp[6],bmp[7],bmp[9]))

checkBmp('struct.bmp')


print '------hashlib--------------'
'''
摘要算法简介
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
'''
import  hashlib
md = hashlib.md5()
md.update('3721')
print dir(md)
print (md.hexdigest())

md5 = hashlib.md5()
md5.update('37')
md5.update('21')
print md5.hexdigest()

db={}
def register(userName,password):
    md5=hashlib.md5()
    md5.update(userName+password+'好123')
    db[userName]=md5.hexdigest()

def login(userName,password):
    if userName in db.keys():
        md5=hashlib.md5()
        md5.update(userName+password+'好123')
        if db[userName] == md5.hexdigest():
            print '登陆成功'
        else:
            print '密码错误'
    else:
        print '用户名错误'

register('qqqq','666')
register('说话了','好')
login('qqqq','666')
login('说话了','好')
login('qqqq','6666')
login('sf','666')


print  '------------itertools-----------------------'
import itertools
print 'chain 可以把一组迭代对象串联起来，形成一个更大的迭代器'
for i in itertools.chain([1,2,4,5,7,8,9],'hao123'): #可以把一组迭代对象串联起来，形成一个更大的迭代器
    print i
print 'group 迭代器中相邻的重复元素挑出来放在一起'
for key ,group in itertools.groupby('qqqqqqqqqs3333s3gg'):
    print key ,list(group)

print "'无限'迭代器"
'''#count
natuals=itertools.count(3,2)
for i in natuals:
    print(i)
'''
'''#cycle
for i in itertools.cycle([1,2,3,4]):
    print i
'''
for i in itertools.repeat('好',10): #repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
    print i
'''
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
'''
natuals=itertools.count()
for i in itertools.takewhile(lambda x:x<10,natuals):
    print  i

print  ' imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。'
for i in itertools.imap(lambda x,y :x*y,[10,20,30],natuals): #因为重用natuals,所有从11开始
    print i
'''
注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕
当你调用imap()时，并没有进行任何计算：
必须用for循环对返回迭代对象进行迭代，才会在每次循环过程中计算出下一个元素：
这说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列：
'''

print'itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算。'

print '----------------xml-----------------------'
'''
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：
<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
'''
from xml.parsers.expat import ParserCreate
class xmlParsersHandler(object):
    def start_enlement(self,name,attrs):
        print 'sax:start_elemen: %s  attrs %s'%(name,str(attrs))
    def end_element(self,name):
        print 'sax: end_element: %s'%name
    def char_data(self,text):
        print'sax:charData :%s'%text
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler =xmlParsersHandler()
xmlP = ParserCreate()
xmlP.returns_unicode=True
xmlP.StartElementHandler=handler.start_enlement
xmlP.EndElementHandler=handler.end_element
xmlP.CharacterDataHandler=handler.char_data
xmlP.Parse(xml)


class xmlParsersHandlerA(object):
    def __init__(self):
        self.l=[]
    def start_enlement(self,name,attrs):
        print 'sax:start_elemen: %s  attrs %s'%(name,str(attrs))
        if name=='yweather:forecast':
            self.l.append(attrs)

    def end_element(self,name):
        print 'sax: end_element: %s'%name
    def char_data(self,text):
        print'sax:charData :%s'%text
    def debug(self):
        for x in self.l:
            print '%s %s %s 温度最高%s度 最底%s度'%(x['date'].encode('utf-8'),x['day'].encode('utf-8'),x['text'].encode('utf-8'),x['high'].encode('utf-8'),x['low'].encode('utf-8'))


with open('xml.txt','r') as f:
    handler1 =xmlParsersHandlerA()
    xmlP1 = ParserCreate()
    xmlP1.returns_unicode=True
    xmlP1.StartElementHandler=handler1.start_enlement
    xmlP1.EndElementHandler=handler1.end_element
    xmlP1.CharacterDataHandler=handler1.char_data
    xml1=f.read()
    print xml1
    xmlP1.Parse(xml1)
    handler1.debug()


print '---------HTMLParser--------------'
'''
如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
假设第一步已经完成了，第二步应该如何解析HTML呢？
HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
好在Python提供了HTMLParser来非常方便地解析HTML，
'''
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):#开始标签
        print('<%s %s>' % (tag,attrs))

    def handle_endtag(self, tag):#结束标签
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):#类<img /> 开始结束都在<>内
        print('<%s %s/>' % (tag,attrs))

    def handle_data(self, data):#内容
        print('data:%s'%data)

    def handle_comment(self, data):#注释内容
        print('<!--%s-->'%data)

    def handle_entityref(self, name):#特殊符号 命名实体 Δ : &Delta;
        print('特殊符号命名实体: &%s;' % name)

    def handle_charref(self, name):#特殊符号 十进制编码 Δ : &#916;
        print('特殊符号十进制编码: &#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body>&#916;<p>Some<!--zhusi--> &Delta;<img scr=\'#\'/> <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')


from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
class MyHtmlParserA(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.l=[]
        self.flag=False

    def handle_starttag(self, tag, attrs):
        if tag=='time'or (tag =='span'and  attrs.__contains__(('class','event-location'))or (tag=='h3' and attrs.__contains__(('class', 'event-title')))):
                self.flag=True
    def handle_data(self, data):
        if self.flag :
            #print repr( data)
            self.flag=False
            self.l.append(data)

    def myDebug(self):
        return  self.l


htmlP=MyHtmlParserA()
with open('html.txt','r') as f:
    html = f.read()
    htmlP.feed(html)

    r=htmlP.myDebug()
    for i in range(len(r)/3):
        print '会议标题 %s 举行时间:%s  会议举行地点:%s'%(r[0+i*3],r[1+i*3],r[2+i*3])



print '****************第三方模块***********************'
'''
除了内建的模块外，Python还有大量的第三方模块。

基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用easy_install或者pip安装。
'''
print '----PIL-----'
'''
缩放 切片、旋转、滤镜、输出文字、调色板等
PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图
要详细了解PIL的强大功能，请请参考PIL官方文档：
http://effbot.org/imagingbook/

64位 win 使用 pillow 代替
例子文件 MYpil.py
'''



print '**************图形编程***********************'

'''
Python支持多种图形界面的第三方库，包括
Tk
wxWidgets
Qt
GTK
等等。
但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。
'''
'''
from  Tkinter import * #1 导入TKinter 所有东西
class Application(Frame):  #2 重Frame 派生
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.pack() #把 widgets加入父容器
        self.creatWidgets() #创建一个widgetd
    def creatWidgets(self):
        self.helloLabe=Label(self,text='Hello Python Gui') #创建一个标签
        self.helloLabe['fg']='red'
        self.helloLabe.pack({'side':'left'})#添加到父容器
        self.helloButten=Button(self,text='quit',command=self.quit)#创建一个按钮
        self.helloButten.pack({'side':'left'})
root =Tk() #创建根容器
app =Application(master=root) #创建实例
app.master.title('Hello')
app.mainloop()#窗口主消息循环
root.destroy() #销毁根容器
'''
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
'''
在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
'''
from    Tkinter import *
import  tkMessageBox
class ApplicationA(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.creatWidgets()
    def creatWidgets(self):
        self.newLable=Label(self)
        self.newLable['text']='好奇'
        self.newLable['fg']='green'
        self.newLable.pack({'side':'right'})
        self.input=Entry(self)
        self.input.pack()
        self.alertButten=Button(self,text='hello world',command=self.alert1) #注意是函数变量 不是执行 alert()
        self.alertButten.pack()

    def alert1(self):
        name= self.input.get() or'word'
        tkMessageBox.showinfo('好','hello %s'%name)

root1 =Tk()
appA=ApplicationA()
appA.master.maxsize(960,640)
appA.mainloop()
#root1.destroy()

print '********网络编程************'
'''
tcp
socket_service.py
socket_client.py

udp
UDP_service.py
UDP_client.py
'''
print '***********电子邮件*********************'
'''
电子邮件软件被称为MUA：Mail User Agent——邮件用户代理。
Email从MUA发出去，不是直接到达对方电脑，
而是发到MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等
一封电子邮件的旅程就是：
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：

编写MUA把邮件发到MTA；

编写MUA从MDA上收邮件。
发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。

收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，所以，你得填163提供的SMTP服务器地址：smtp.163.com，为了证明你是163的用户，SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。

在使用Python收发邮件前，请先准备好至少两个电子邮件，如xxx@163.com，xxx@sina.com，xxx@qq.com等，注意两个邮箱不要用同一家邮件服务商。

'''
print '---------------SMTP 发邮件-------------------'
'''
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
'''
'''
from email.mime.text import MIMEText
msg=MIMEText('hello send by Pthon','plain','utf-8')

#注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

print 'smtp 发邮件'
from_addr=raw_input('From:') #email地址
password=raw_input('Password:')#email 密码
smtp_service=raw_input('SMTP Service:') #stmp 服务器地址 #网易smtp.163.com
to_add=raw_input('To:') #收件人地址

import smtplib
service=smtplib.SMTP(smtp_service,25)# SMTP协议默认端口是25
service.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
service.login(from_addr,password) #login()方法用来登录SMTP服务器
service.sendmail(from_addr,to_add,msg.as_string())#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
service.quit()
'''
'''
仔细观察，发现如下问题：
邮件没有主题；
收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
明明收到了邮件，却提示不在收件人中。
这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
'''
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import  smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8')if isinstance(addr,unicode) else addr
        ))

from_addr=raw_input('From:')
password=raw_input('Password:')
to_addr=raw_input('To:')
smtp_service=raw_input('SMTP Service:')

msg =MIMEText('hello send by Python ','plain','utf-8')
msg['From']=_format_addr(u'Python爱好者 <%s>'%from_addr)
msg['To']=_format_addr(u'管理员 <%s>'%to_addr)
msg['Subject']=Header(u'来自STMP的问候...','utf-8'.encode())

service=smtplib.SMTP(smtp_service,25)
service.set_debuglevel(1)
service.login(from_addr,password)
service.sendmail(from_addr,to_addr,msg.as_string())
service.quit()
'''
'''
我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。

msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。

发送HTML邮件

如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
'''

'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import  smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8')if isinstance(addr,unicode) else addr
        ))

from_addr=raw_input('From:')
password=raw_input('Password:')
to_addr=raw_input('To:')
smtp_service=raw_input('SMTP Service:')

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From']=_format_addr(u'Python爱好者 <%s>'%from_addr)
msg['To']=_format_addr(u'管理员 <%s>'%to_addr)
msg['Subject']=Header(u'来自STMP的问候...','utf-8'.encode())

service=smtplib.SMTP(smtp_service,25)
service.set_debuglevel(1)
service.login(from_addr,password)
service.sendmail(from_addr,to_addr,msg.as_string())
service.quit()
'''
'''
发送附件

如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
再继续往里面加上表示附件的MIMEBase对象即可：
'''
'''
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import MIMEBase
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import  smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8')if isinstance(addr,unicode) else addr
        ))

from_addr=raw_input('From:')
password=raw_input('Password:')
to_addr=raw_input('To:')
smtp_service=raw_input('SMTP Service:')

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('cat.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpeg', filename='cat.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='cat.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

service=smtplib.SMTP(smtp_service,25)
service.set_debuglevel(1)
service.login(from_addr,password)
service.sendmail(from_addr,to_addr,msg.as_string())
service.quit()
'''
'''
发送图片

如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？
答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
'''
'''
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import MIMEBase
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import  smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8')if isinstance(addr,unicode) else addr
        ))

from_addr=raw_input('From:')
password=raw_input('Password:')
to_addr=raw_input('To:')
smtp_service=raw_input('SMTP Service:')

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('cat.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpeg', filename='cat.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='cat.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

service=smtplib.SMTP(smtp_service,25)
service.set_debuglevel(1)
service.login(from_addr,password)
service.sendmail(from_addr,to_addr,msg.as_string())
service.quit()
'''
'''
同时支持HTML和Plain格式

如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。

利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
'''
'''
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import MIMEBase
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import  smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8')if isinstance(addr,unicode) else addr
        ))

from_addr=raw_input('From:')#邮箱地址
password=raw_input('Password:')#邮箱密码
to_addr=raw_input('To:')#收件邮箱地址
smtp_service=raw_input('SMTP Service:')#smtp.163.com

# 邮件对象:
msg = MIMEMultipart('alternative')#指定subtype是alternative：
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('cat.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpeg', filename='cat.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='cat.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

service=smtplib.SMTP(smtp_service,25)
service.set_debuglevel(1)
service.login(from_addr,password)
service.sendmail(from_addr,to_addr,msg.as_string())
service.quit()
'''
'''
加密SMTP

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。

必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...
只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样。

如果因为网络问题无法连接Gmail的SMTP服务器，请相信我们的代码是没有问题的，你需要对你的网络设置做必要的调整。
'''
'''
小结

使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：

Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
这种嵌套关系就可以构造出任意复杂的邮件。你可以通过email.mime文档查看它们所在的包以及详细的用法。
'''

print  '-------------POP3 收邮件---------------------'

'''
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
#文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset = msg.get_charset()# 先从msg对象获取编码:
    if charset is None:   # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
#邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
def decode_str(s):
    value, charset = decode_header(s)[0]#decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素,这里测试只取第一个
    if charset:
        value = value.decode(charset)
    return value
#但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。所以我们要递归地打印出Message对象的层次结构：
def print_info(msg, indent=0):#indent打印缩进
    if indent == 0:
        for header in ['From', 'To', 'Subject']:   # 邮件的From, To, Subject存在于根对象上:
            value = msg.get(header, '')
            if value:
                if header=='Subject':   # 需要解码Subject字符串:
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)   # 需要解码Email地址:
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):   # 如果邮件对象是一个MIMEMultipart,  # get_payload()返回list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)  # 递归打印每一个子对象:
    else:
         # 邮件对象不是一个MIMEMultipart,
        # 就根据content_type判断:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html': # 纯文本或HTML内容:
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)    # 要检测文本编码:
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:  # 不是文本,作为附件处理:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

email = raw_input('Email: ')
password = raw_input('Password: ')
pop3_server = raw_input('POP3 server: ') #网易 pop3.163.com

server = poplib.POP3(pop3_server)
#server.set_debuglevel(1)
print(server.getwelcome())
# 认证:
server.user(email)
server.pass_(password)
print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
# 获取最新一封邮件, 注意索引号从1开始:
resp, lines, octets = server.retr(len(mails))
# 解析邮件:
msg = Parser().parsestr('\r\n'.join(lines))
# 打印邮件内容:
print_info(msg)
# 慎重:将直接从服务器删除邮件:
# server.dele(len(mails))
# 关闭连接:
server.quit()

'''
print '****************数据库*********************'

print '-------sqlite3---------'
''' M_sqlite3.py'''
print'------------mysql------------------'
''' mysql.py'''

print '--------ORM框架是SQLAlchemy---------------'

'''orm.py
数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表：

[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
Python的DB-API返回的数据结构就是像上面这样表示的。

但是用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：

class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。是不是很简单？

但是由谁来做这个转换呢？所以ORM框架应运而生。

在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。

首先通过easy_install或者pip安装SQLAlchemy：
启动wamp
启动sql数据库
orm.py
my_sql.py
'''

print '-----------mongodb-------'
'''
mongodb.py
要先启动mongodb服务,
start_Sever.bat
'''
















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

print '*********web**********'
print '---------http 协议---------'
'''
HTTP请求

跟踪了新浪的首页，我们来总结一下HTTP请求的流程：

步骤1：浏览器首先向服务器发送HTTP请求，请求包括：

方法：GET还是POST，GET仅请求资源，POST会附带用户数据；

路径：/full/url/path；

域名：由Host头指定：Host: www.sina.com.cn

以及其他相关的Header；

如果是POST，那么请求还包括一个Body，包含用户数据。

步骤2：服务器向浏览器返回HTTP响应，响应包括：

响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；

响应类型：由Content-Type指定；

以及其他相关的Header；

通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。

步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。

HTTP格式

每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。

HTTP协议是一种文本协议，所以，它的格式也非常简单。HTTP GET请求的格式：

GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
每个Header一行一个，换行符是\r\n。

HTTP POST请求的格式：

POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

HTTP响应的格式：

200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。
'''

print '-----------Html-------------------------'
print '-------Css--------------'
print'------javascript----------------'

print '----------WSGI 接口---------------------'
'''
了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：

浏览器发送一个HTTP请求；

服务器收到请求，生成一个HTML文档；

服务器把HTML文档作为HTTP响应的Body发送给浏览器；

浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface。


wsgi.py
helloWeb.py
'''
print '-----web 框架--------'
'''

了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。

但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。

每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。

一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断：

def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path='/signin':
        return handle_signin(environ, start_response)
    ...
只是这么写下去代码是肯定没法维护了。

代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。

由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——Flask来使用。
除了Flask，常见的Python Web框架还有：

Django：全能型Web框架；

web.py：一个小巧的Web框架；

Bottle：和Flask类似的Web框架；

Tornado：Facebook的开源异步Web框架。

有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。
Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。
'''
print '----flask-----------'
print '-------------dijago--------'
print '----------Pyramid---------'

print '----------HTML模板------------------'
'''
Web框架把我们从WSGI中拯救出来了。现在，我们只需要不断地编写函数，带上URL，就可以继续Web App的开发了。

但是，Web App不仅仅是处理逻辑，展示给用户的页面也非常重要。在函数中返回一个包含HTML的字符串，简单的页面还可以，但是，想想新浪首页的6000多行的HTML，你确信能在Python的字符串中正确地写出来么？反正我是做不到。

俗话说得好，不懂前端的Python工程师不是好的产品经理。有Web开发经验的同学都明白，Web App最复杂的部分就在HTML页面。HTML不仅要正确，还要通过CSS美化，再加上复杂的JavaScript脚本来实现各种交互和动画效果。总之，生成HTML页面的难度很大。

由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。

使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：

mvc-seq

这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；

包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

mvc.png
上面的例子中，Model就是一个dict：

{ 'name': 'Michael' }
只是因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model。


除了Jinja2，常见的模板还有：

Mako：用<% ... %>和${xxx}的一个模板；

Cheetah：也是用<% ... %>和${xxx}的一个模板；

Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

小结

有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。
'''
print '----jinja2 -----'
#Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2
print'注意一定要把模板放到正确的templates目录下，templates和app.py在同级目录下：'




print '************协程 gevent********************'
'''
Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。

gevent是第三方库，通过greenlet实现协程，其基本思想是：

当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：
geventTest.py
'''
