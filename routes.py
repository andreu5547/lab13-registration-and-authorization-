from app import app, db
from flask import render_template, request, redirect, url_for
from models import User
from validate import valid_email, valid_login, valid_password


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    result = 'Пользователь не создан'
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not valid_login(username):
            result = 'Некорректный логин'
        elif not valid_email(email):
            result = 'Некорректный email'
        elif not valid_password(password):
            result = 'Некорректный пароль'
        elif password != confirm_password:
            result = 'Пароли не совпадают'
        else:
            user = User(
                username=username,
                email=email,
                password=password)
            user_test = User.query.filter_by(username=user.username).first()
            if user_test is None:
                db.session.add(user)
                db.session.commit()
                result = 'Пользователь создан'
            else:
                result = 'Пользователь уже существует'
    return render_template('/register.html', result=result)


@app.route('/login', methods=['GET', 'POST'])
def login():
    result = 'Пользователь не введен'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_test = User.query.filter_by(username=username).first()
        if user_test is None:
            result = 'Пользователь не существует'
        elif user_test.password != password:
            result = 'Неверный пароль'
        else:
            result = 'Пользователь вошел'
    if result == 'Пользователь вошел':
        return redirect(url_for('confirm'))
    return render_template('/login.html', result=result)


@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    return render_template('/confirm.html')
