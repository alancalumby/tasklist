from tasklist import app
from flask import render_template
from tasklist.models import TaskItem
from tasklist.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    tasks = TaskItem.query.all()
    return render_template('home.html', tasks = tasks)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)