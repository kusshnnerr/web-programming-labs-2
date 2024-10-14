from flask import Flask, url_for, redirect, render_template
from lab1 import lab1 
from lab2 import lab2

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

@app.errorhandler(404)
def not_found(err):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='404.css') + '''">
        <title>Ошибка 404</title>
    </head>
    <body>
        <h1>ОЙ… Кажется такой страницы не существует</h1>
        <p>Возможно, она была удалена, переименована или никогда не существовала.</p>
        <img src="''' + url_for('static', filename='404_error.jpg') + '''">
        <a href="/index">Вернуться на главную</a>
    </body>
''', 404

@app.route('/error400') 
def error_400(): 
    return ''' 
<!doctype html> 
<html> 
    <body> 
        <h1>400 - Bad Request</h1> 
        <p>Сервер не может обработать ваш запрос.</p> 
    </body> 
</html> 
''', 400

@app.route('/error401') 
def error_401(): 
    return ''' 
<!doctype html> 
<html> 
    <body> 
        <h1>401 - Unauthorized</h1> 
        <p>Доступ запрещен. Требуется авторизация.</p> 
    </body> 
</html> 
''', 401 

@app.route('/error402') 
def error_402(): 
    return ''' 
<!doctype html> 
<html> 
    <body> 
        <h1>402 - Payment Required</h1> 
        <p>Требуется оплата для доступа к ресурсу.</p> 
    </body> 
</html> 
''', 402 

@app.route('/error403') 
def error_403(): 
    return ''' 
<!doctype html> 
<html> 
    <body> 
        <h1>403 - Forbidden</h1> 
        <p>Доступ к ресурсу запрещен.</p> 
    </body> 
</html> 
''', 403 

@app.route('/error405') 
def error_405(): 
    return ''' 
<!doctype html> 
<html> 
    <body> 
        <h1>405 - Method Not Allowed</h1> 
        <p>Запрошенный метод не разрешен для этого ресурса.</p> 
    </body> 
</html> 
''', 405 

@app.route('/error418') 
def error_418(): 
    return ''' 
<!doctype html> 
<html> 
    <body> 
        <h1>418 - I'm a teapot</h1> 
        <p>Я — чайник, и я не могу заварить кофе.</p> 
    </body> 
</html> 
''', 418

@app.errorhandler(500)
def internal_server_error(err):
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Ошибка 500</title>
    </head>
    <body>
        <h1>Внутренняя ошибка сервера</h1>
        <p>На сервере произошла ошибка, в результате которой он не может успешно обработать запрос.
        Пожалуйста, попробуйте позже.</p>
        <a href="/index">Вернуться на главную</a>
    </body>
</html>
''', 500

@app.route('/trigger_500')
def trigger_500():
    abort(500)

@app.route('/an_error')
def make_an_error():
    return 1 / 0

@app.route("/")

@app.route('/index')
def index():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
        <ol>
            <li><a href="/lab1">Первая лабораторная</a></li>
            <li><a href="/lab2/">Вторая лабораторная</a></li>
        </ol>
    </body>
    <footer>
        Кушнер Екатерина Костантинл ФБИ-21, 3 Курс, 2024 год.
    </footer>
</html>
'''