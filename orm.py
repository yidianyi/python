#-*-coding:utf-8-*-
from sqlalchemy import Column, String ,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base


#创建对象的基类
Base=declarative_base() #映射基类
#定义User对象
class User(Base):#继承declarative_base()返回的类型   #表示一个表
    #表的名字 __tablename__ 变量名不可变
    __tablename__='user'

    #表的结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))

#再添加另一个表对象
class School(Base):
    __tablename__='school'
    id=Column(String(20),primary_key=True)
    name=Column(String(20))

#初始化数据库连接,返回数据库引擎 ,'数据库+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名'
engine=create_engine('mysql+mysqldb://root:''@localhost:3306/yidianyi')
Base.metadata.create_all(engine) #创建所有继承Base的表对象,即在数据库创建table
#创建DBSession类型
DBSession=sessionmaker(bind=engine) #动态创建DBSession类

#创建一个数据库会话实例,对象可视为当前数据库连接。
session=DBSession()
#创建一条User表的记录
newUser=User(id='113',name='Python')
newSchool=School(id='22',name='hello')
session.add(newUser)#添加到session  #添加
session.add(newSchool)
session.commit()#提交到数据库
session.close_all()#关闭会话


#查询
session=DBSession()
user=session.query(User).filter(User.id=='113').one()
print 'type',type(user)
print 'name',user.name
session.query(School).filter(School.id=='22').update({School.name:'world'},synchronize_session='evaluate')#修改
session.query(User).filter(User.id=='113').delete(synchronize_session='evaluate') #删除
session.commit()
session.close()

