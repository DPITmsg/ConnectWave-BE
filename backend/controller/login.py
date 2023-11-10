from flask import render_template, request, redirect, url_for, session
from config import app
# from repository.user_repo import get_account_by_username_and_password, get_account_by_username
from services.user_service import UserService
from models.user import User
import random
import string

source = string.ascii_letters + string.digits


@app.route('/login2', methods=['GET', 'POST'])
def login():
    service = UserService()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = service.login(username, password)
        if account:
            session['loggedin'] = True
            session['username'] = account.username
            session['token'] = ''.join((random.choice(source) for i in range(8)))
            msg = 'Logged in successfully! Token:' + session['token']
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    service = UserService()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = service.regiser(username)
        if account:
            msg = 'Account already exists!'
        elif not username or not password:
            msg = 'Please fill out the form!'
        else:
            service_add_user(User(username=username, password=password))
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)
