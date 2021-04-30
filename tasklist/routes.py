from tasklist import app,db,login_mgr
from flask import render_template, redirect, url_for, flash
from tasklist.models import TaskItem, User
from tasklist.forms import RegisterForm, LoginForm
from flask_login import login_user,logout_user

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
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))

    if form.errors != {}: #no errors in validations
        for err_msg in form.errors.values():
            flash(f'Error: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.validate_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect login/password. Try again!',category='danger')
    
    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'You have benn logged out. See you soon', category='info')
    return redirect(url_for('home_page'))

@app.route('/tasks')
def tasks_page():
    tasks = TaskItem.query.all()
    return render_template('tasks.html', tasks = tasks)