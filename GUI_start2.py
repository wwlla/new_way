from bottle import route, run, template

@route('/你好/<name>')
def index(name):
    return template('<b>你好 {{name}}</b>', name=name)
run(host='127.0.0.1', port=8080)