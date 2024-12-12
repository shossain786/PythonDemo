from flask import Blueprint, render_template, request, redirect, url_for, session

main = Blueprint('main', __name__)

@main.route('/')
def login():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "password":
        session['user'] = username
        return redirect(url_for('main.home'))
    return "Invalid credentials, please try again!"

@main.route('/home')
def home():
    if 'user' in session:
        return f"Welcome to the Home Page, {session['user']}!"
    return redirect(url_for('main.login'))
