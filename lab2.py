from flask import Blueprint, render_template, redirect, url_for
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/a/")
def a():
    return "с палочкой"


@lab2.route("/lab2/a")
def a2():
    return "без палочки"


flower_list =  [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 80},
    {'name': 'Незабудка', 'price': 50},
    {'name': 'Ромашка', 'price': 30}
]


#Меню всех цветов
@lab2.route('/lab2/all_flowers/')
def all_flowers():
    flowers = flower_list
    flowers_num = len(flower_list)
    return render_template('lab2/flowers.html', flower_list=flowers, flowers_num=flowers_num)
  

@lab2.route('/lab2/add_flower/')
def add_flowers():
    name = request.args.get('name')
    price = request.args.get('price')
    style = url_for("static", filename="main.css")
    if name and price:
        flower_list.lab2end({'name': name, 'price': int(price)})
        flower_id = len(flower_list) - 1
        return render_template('lab2/add_flower.html', flower_id=flower_id, name=name, price=price)
    else:    
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Поле не заполнено!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 400


#Цветок по ID
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    style = url_for("static", filename="main.css")
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Такого цветка нет!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 404
    else:
        flower = flower_list[flower_id]
    return render_template('lab2/flower_id.html', flower=flower, flower_id=flower_id)
#Не задан ID цветка


@lab2.route('/lab2/flowers/')
def err_flowers():
    style = url_for("static", filename="main.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Вы не задали ID цветка!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 400
    

#Очистить весь список цветов
@lab2.route('/lab2/delete_flowers/')
def delete_flowers():
    flower_list.clear()  
    return redirect('/lab2/all_flowers/')


#Удалить цветок по ID
@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    style = url_for("static", filename="main.css")
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + style + '''">
    </head>
    <body>
        <h1>Цветов больше нет!</h1>
        <a href="/lab2/all_flowers/">Вернуться к списку цветов</a>
    </body>
</html>
''', 404
    else:
        del flower_list[flower_id]
        return redirect('/lab2/all_flowers/')


@lab2.route('/lab2/example')
def example ():
    name, number, group, course = 'Кушнер Екатерина', 2, 'ФБИ-21', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('lab2/example.html', 
                            name=name, number=number, group=group,
                            course=course, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase=phrase) 


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    num_a = a
    num_b = b
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Деление на ноль"
    power = a ** b
    return render_template('lab2/calc.html', a=num_a, b=num_b, addition=addition, subtraction=subtraction,
                           multiplication=multiplication, division=division, power=power)


@lab2.route('/lab2/calc/')
def red_calc():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def redi_calc(a):
    return redirect(f'/lab2/calc/{a}/1')


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
@lab2.route("/lab2/books")
def books_page():
    return render_template("lab2/books.html", books=books)

cars = [
    {
        "name": "Rolls-Royce Phantom",
        "image": "lab2/Rolls-Royce Phantom.jpg",
        "description": "Флагманская модель британского бренда. Воплощение роскоши и комфорта."
    },
    {
        "name": "Bentley Continental GT",
        "image": "lab2/Bentley Continental GT.jpg",
        "description": "Элегантное купе с мощным двигателем и динамичными характеристиками."
    },
    {
        "name": "Aston Martin DB11",
        "image": "lab2/Aston Martin DB11.jpg",
        "description": "Стильный и современный спортивный автомобиль с фирменным дизайном Aston Martin."
    },
    {
        "name": "Mercedes-Benz S-Class",
        "image": "lab2/Mercedes-Benz S-Class.jpg",
        "description": "Флагманский седан Mercedes-Benz, воплощение роскоши и технологичности."
    },
    {
        "name": "Maserati Ghibli",
        "image": "lab2/Maserati Ghibli.jpg",
        "description": "Итальянский седан с мощным двигателем и стильным дизайном."
    }
]


@lab2.route('/lab2/cars')
def cars_page():
    return render_template('lab2/cars.html', cars=cars)