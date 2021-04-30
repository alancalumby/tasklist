from tasklist import app
from flask import render_template, redirect, url_for
from tasklist.models import TaskItem, User
from tasklist.forms import RegisterForm
from tasklist import db

@app.route('/')
@app.route('/home')
def home_page():
    tasks = TaskItem.query.all()
    return render_template('home.html', tasks = tasks)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))

    if form.errors != {}: #no errors in validations
        for err_msg in form.errors.values():
            print(f'Error: {err_msg}')

    return render_template('register.html', form=form)