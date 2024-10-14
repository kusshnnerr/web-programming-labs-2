from flask import Blueprint, url_for, redirect, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/a/")
def a():
    return "с палочкой"


@lab2.route("/lab2/a")
def a2():
    return "без палочки"

flower_list = ['роза', 'тюльпан', 'ромашка', 'незабудка']


@lab2.route("/lab2/flowers/<int:flower_id>")
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return render_template('404.html'), 404
    else:
        return render_template('flower.html', flower=flower_list[flower_id])


@lab2.route('/lab2/add_flower/', defaults={'name': None})


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    if name is None:
        return "вы не задали имя цветка", 400
    flower_list.lab2end(name)
    return render_template('add_flower.html', name=name, total=len(flower_list), flowers=flower_list)


@lab2.route('/lab2/all_flowers')
def all_flowers():
    return render_template('all_flowers.html', flowers=flower_list, total=len(flower_list))


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('all_flowers'))


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
    return render_template('example.html', 
                            name=name, number=number, group=group,
                            course=course, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase) 


@lab2.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc_with_one_number(a):
    return redirect(url_for('calc', a=a, b=1))


@lab2.route('/lab2/calc/<int:a>/<int:b>')
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
@lab2.route("/lab2/books")
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


@lab2.route('/lab2/cars')
def cars_page():
    return render_template('cars.html', cars=cars)