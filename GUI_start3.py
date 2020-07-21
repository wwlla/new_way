from bottle import route, post, run, template,request

@post('/message')
def index():
    print('body:',request.body.read().decode('utf-8'))
    return '<h>没问题</h>'

run(host='localhost', port=8080)