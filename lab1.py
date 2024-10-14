from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1', __name__)


@lab1.route('/lab1')
def lab():
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
                <li><a href="/trigger_500">Ошибка 500</a></li>
            </ol>
        </div>
    </body>
</html>
'''


@lab1.route("/lab1/web")
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


@lab1.route("/lab1/author")
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


@lab1.route('/lab1/oak')
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

@lab1.route("/lab1/counter")
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


@lab1.route("/lab1/counter_reset")
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


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
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


@lab1.route('/lab1/new_route')
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
