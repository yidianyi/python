#-*-coding: utf-8-*-
#!/user/bin/evn Python
import  sqlite3

try:
    s=sqlite3.connect('mytest.db') #连接数据库,没有创建
    cur= s.cursor() #获取cursor
    try:
        cur.execute('create table userA (id varchar(20) primary key, name varchar(20))') #执行语句
    except sqlite3.OperationalError as e:
        print '表以存在',e
    try:
        cur.execute('insert into userA (id, name) values ("1", "hello python")')
    except sqlite3.IntegrityError as e:
        print e
    count= cur.rowcount #获得插入的行数

finally:
    cur.close() #关闭cursor
    s.commit() #提交事务
    s.close() #关闭连接


try:
    s=sqlite3.connect('mytest.db')
    cur= s.cursor()
    cur.execute('select * from userA where id=?','1' ) #有几个?占位符就必须对应几个参数
    value=cur.fetchall() #featchall()可以拿到结果集 [(x,xxx),(y,yyy)]
    print value
finally:
    cur.execute('DROP Table  userA') #删除表
    cur.close()
    s.close()



'''
使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：

cursor.execute('select * from user where id=?', '1')
SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。


在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。

要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。
'''