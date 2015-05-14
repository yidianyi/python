#-*-coding:utf-8-*-
'''
实现 WSGI接口 处理函数
HTTP请求的所有输入信息都可以通过environ获得
HTTP响应的输出都可以通过start_response()加上函数返回值作为Body
'''
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

