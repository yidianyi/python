#-*-coding:utf-8-*-
from  pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client=MongoClient(host='localhost',port=27017)#创建mongo客户端并连接 主机和端口  客户端有n个数据库
print client
db=client['test_database'] #获取数据库 等同db = client.test-database  数据库有n个文档集合
print db
collection = db['test-collection']#获取文档集合  collection = db.test_collection  有n个文档, 一个字典为一个文档
print collection
dictA ={'name':'python','say':'hello world'} #创建一个文档,包含多个字段
dictB ={'name':'python','say':'Python is ?'}
collection.insert(dictA)                    #添加文档到文档集合
collection.insert(dictB)
re= collection.find_one({'say':'Python is ?'})                #获取一个文档 ,返回的文档包含"_id"，这自动添加插入。
print re

print '批量输入'
#批量插入
many=[
    {'name':'小白','age':22,'hao':123},
    {'name':'小王','age':52,'hao':3},
    {'name':'小黑','age':32,'hao':23},
    {'name':'小蓝','age':27,'hao':1},
]
collection.insert_many(many)
for post in collection.find():
    print post

print collection.find({'age':22}).count()

print '范围查询'
for pos in collection.find({ "age": { '$lt': 50 ,'$gte':23}}): #age 小于50大于22
    print pos

print '排序'
for pos in collection.find({ "age": { '$lt': 50 ,'$gte':23}}).sort('hao'):
    print pos

print '更新'
collection.find_one_and_replace({'hao':123},{'hao':123456,'liu':66666})#替换
print collection.find_one({'hao':123456})
collection.find_one_and_update({'hao':123456},{'$inc':{'hao':10000000}}) #hao的值加10000000
print collection.find_one({'liu':66666})

print '索引'
collection.create_index([("age", 1)]) #为字段age 添加索引
'''
地理位置索引
文本索引.....
'''
collection.drop() #删除文档集合