from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

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
''', 418, {'Content-Type': 'text/plain'}

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

@app.route('/lab1/trigger_500')
def trigger_500():
    abort(500)

@app.route('/lab1/an_error')
def make_an_error():
    return 1 / 0


@app.route("/")

@app.route('/lab1')
def lab1():
    return'''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Flask</h1>
        <p>
        Flask — фреймворк для создания веб-приложений на языке программирования Python,
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится
        к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений,
        сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <a href="/index">Назад на главную</a>
        <div class="first">
        <p>Список роутов и ошибок:</p>
            <ol>
                <li><a href="/index">Index</a></li>
                <li><a href="/lab1/web">Web</a></li>
                <li><a href="/lab1/info">Info</a></li>
                <li><a href="/lab1/oak">Дуб</a></li>
                <li><a href="/lab1/counter">Counter</a></li>
                <li><a href="/lab1/created">Created</a></li>
                <li><a href="/lab1/new_route">New route</a></li>
                <li><a href="/error400">Ошибка 400</a></li>
                <li><a href="/error401">Ошибка 401</a></li>
                <li><a href="/error403">Ошибка 403</a></li>
                <li><a href="/error404">Ошибка 404</a></li>
                <li><a href="/error405">Ошибка 405</a></li>
                <li><a href="/error418">Ошибка 418</a></li>
                <li><a href="/lab1/trigger_500">Ошибка 500</a></li>
            </ol>
        </div>
    </body>
</html>
'''

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
        </ol>
    </body>
    <footer>
        Кушнер Екатерина Костантинл ФБИ-21, 3 Курс, 2024 год.
    </footer>
</html>
'''

@app.route("/lab1/web")
def web() :
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1> 
               <a href="/lab1/author">author</a>
           </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/html; charset=utf-8'
        }

@app.route("/lab1/author")
def author() :
    name = "Кушнер Екатерина Константиновна"
    group = "ФБИ-21"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>""" 

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    style = url_for('static', filename='lab1.css')
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route("/lab1/counter")
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <br>
        <a href="/lab1/counter_reset">Сбросить счётчик</a>
    </body>
</html>
'''

@app.route("/lab1/counter_reset")
def reset_counter():
    global count
    count = 0  
    return '''
<!doctype html>
<html>
    <body>
        Счётчик успешно сброшен. 
        <br>
        <a href="/lab1/counter">Назад к счётчику</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано..</i></div>
    <body>
</html>
''', 201

@app.route('/lab1/new_route')
def new_route():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='new.css') + '''">
        <title>The Richest Man In Babylon</title>
    </head>
    <body>
        <h1>George S. Clason</h1>
        <p>
        Our prosperity as a nation depends upon the personal financial prosperity of each of us as individuals.
        </p>
        <p>
        This book deals with the personal successes of each of us. Success means accomplishments as the result of our own efforts
        and abilities. Proper preparation is the key to our success. Our acts can be no wiser than our thoughts.
        Our thinking can be no wiser than our understanding.
        </p>
        <p>
        This book of cures for lean purses has been termed a guide to financial understanding.
        That, indeed, is its purpose: to offer those who are ambitious for financial success an insight which will aid them
        to acquire money, to keep money and to make their surpluses earn more money.
        </p>
        <div class="image_container" style='position: absolute; right: 50px; top: 10%'>
            <img src="''' + url_for('static', filename='book.jpg') + '''" style='margin-top: 10px'>
        </div>
        <div>
        <a href="/lab1">Back to the lab page</a>
        </div>
    </body>
    <footer>Кушнер Екатерина Константиновна, ФБИ-21, 3 Курс, 2024 год.</footer>
</html>
''', 200, {
    'Content-Language': 'en',
    'X-Nerd': '42',
    'X-Student': 'Kushner Ekaterina'
}

@app.route("/lab2/a/")
def a():
    return "ok"

@app.route("/lab2/a")
def a2():
    return "ok"

flower_list = ['роза' , 'тюльпан' , 'ромашка', 'незабудка']

@app.route("/lab2/flowers/<int:flower_id>")
def flowers (flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f''' 
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example ():
    name = 'Кушнер Екатерина'
    return render_template('example.html', name=name)