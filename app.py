from flask import Flask, url_for, redirect, render_template
from lab1 import lab1 

app = Flask(__name__)
app.register_blueprint(lab1)

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

@app.route("/lab2/a/")
def a():
    return "с палочкой"

@app.route("/lab2/a")
def a2():
    return "без палочки"

flower_list = ['роза', 'тюльпан', 'ромашка', 'незабудка']

@app.route("/lab2/flowers/<int:flower_id>")
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return render_template('404.html'), 404
    else:
        return render_template('flower.html', flower=flower_list[flower_id])

@app.route('/lab2/add_flower/', defaults={'name': None})
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    if name is None:
        return "вы не задали имя цветка", 400
    flower_list.append(name)
    return render_template('add_flower.html', name=name, total=len(flower_list), flowers=flower_list)


@app.route('/lab2/all_flowers')
def all_flowers():
    return render_template('all_flowers.html', flowers=flower_list, total=len(flower_list))

@app.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('all_flowers'))

@app.route('/lab2/example')
def example ():
    name, number, group, course = 'Кушнер Екатерина', 2, 'ФБИ-21', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', 
                            name=name, number=number, group=group,
                            course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase) 

@app.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('calc', a=1, b=1))

@app.route('/lab2/calc/<int:a>')
def calc_with_one_number(a):
    return redirect(url_for('calc', a=a, b=1))

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    if b != 0:
        divide = a / b
    else:
        divide = "Деление на ноль невозможно"
    power = a ** b

    return render_template('calculator.html', a=a, b=b, add=add, subtract=subtract, multiply=multiply, divide=divide, power=power)

books = [
    {
        "author": "Джордж Оруэлл",
        "title": "1984",
        "genre": "Антиутопия",
        "pages": 328
    },
    {
        "author": "Джон Р.Р. Толкин",
        "title": "Властелин колец",
        "genre": "Фэнтези",
        "pages": 1178
    },
    {
        "author": "Стивен Кинг",
        "title": "Оно",
        "genre": "Ужасы",
        "pages": 1138
    },
    {
        "author": "Агата Кристи",
        "title": "Убийство в Восточном экспрессе",
        "genre": "Детектив",
        "pages": 256
    },
    {
        "author": "Харпер Ли",
        "title": "Убить пересмешника",
        "genre": "Драма",
        "pages": 281
    },
    {
        "author": "Рэй Брэдбери",
        "title": "451 градус по Фаренгейту",
        "genre": "Антиутопия",
        "pages": 208
    },
    {
        "author": "Александр Дюма",
        "title": "Три мушкетера",
        "genre": "Приключения",
        "pages": 656
    },
    {
        "author": "Джек Лондон",
        "title": "Зов предков",
        "genre": "Приключения",
        "pages": 192
    },
    {
        "author": "Ремарк Эрих Мария",
        "title": "На Западном фронте без перемен",
        "genre": "Военная проза",
        "pages": 224
    },
    {
        "author": "Эрнест Хемингуэй",
        "title": "Старик и море",
        "genre": "Повесть",
        "pages": 127
    }
]
@app.route("/lab2/books")
def books_page():
    return render_template("books.html", books=books)

cars = [
    {
        "name": "Rolls-Royce Phantom",
        "image": "Rolls-Royce Phantom.jpg",
        "description": "Флагманская модель британского бренда. Воплощение роскоши и комфорта."
    },
    {
        "name": "Bentley Continental GT",
        "image": "Bentley Continental GT.jpg",
        "description": "Элегантное купе с мощным двигателем и динамичными характеристиками."
    },
    {
        "name": "Aston Martin DB11",
        "image": "Aston Martin DB11.jpg",
        "description": "Стильный и современный спортивный автомобиль с фирменным дизайном Aston Martin."
    },
    {
        "name": "Mercedes-Benz S-Class",
        "image": "Mercedes-Benz S-Class.jpg",
        "description": "Флагманский седан Mercedes-Benz, воплощение роскоши и технологичности."
    },
    {
        "name": "Maserati Ghibli",
        "image": "Maserati Ghibli.jpg",
        "description": "Итальянский седан с мощным двигателем и стильным дизайном."
    }
]


@app.route('/lab2/cars')
def cars_page():
    return render_template('cars.html', cars=cars)