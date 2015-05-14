#-*-coding:utf-8-*-
from flask import Flask
from flask import request

app=Flask(__name__) #创建一个web app

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
@app.route('/signin',methods=['GET'])  #html methods 没s
def signin_form():
    return '''<form action="/signin" method="POST">
    <p><input name="username"/>></p>
    <p><input name="password" type="password"/>></p>
    <p><button type="submit" >signin</button></p>
    </form>'''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password': #从请求中获取内容
        return '<h1>Welcome %s</h1>'%request.form['username']
    return '<h1>Bad username or password</h1>'
if __name__ =='__main__':
    app.run()   #运行
