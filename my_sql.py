#-*-coding:utf-8-*-
'''
安装MySQL驱动

由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。

目前，有两个MySQL驱动：

mysql-connector-python：是MySQL官方的纯Python驱动；

MySQL-python：是封装了MySQL C驱动的Python驱动。

可以把两个都装上，使用的时候再决定用哪个：

$ easy_install mysql-connector-python
$ easy_install MySQL-python



由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。
MySQL的SQL占位符是%s；
通常我们在连接MySQL时传入use_unicode=True，让MySQL的DB-API始终返回Unicode。

'''
# 导入MySQL驱动:
#import mysql.connector
import MySQLdb
# 注意把password设为你的root口令:
conn = MySQLdb.Connect(user='root', passwd='', db='test', use_unicode=True)
#conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor = conn.cursor()
cursor.execute('drop TABLE  user')
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
for i in range(12):
    cursor.execute('insert into user (id, name) values (%s, %s)', [i, 'hello python%s'%i])
print cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
#cursor.execute('select * from user where id = %s', ['1']) # %s占位 参数[]
cursor.execute('select * from user')
values = cursor.fetchall()
print values

# 关闭Cursor和Connection:
cursor.close()
True
conn.close()
