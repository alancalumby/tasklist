from tasklist import app, db, login_mgr
from flask import render_template, redirect, url_for, flash, request
from tasklist.models import TaskItem, User
from tasklist.forms import RegisterForm, LoginForm, AddTaskItemForm, DeleteTaskItemForm, ChangeStatusTaskItemForm
from flask_login import login_user, logout_user, login_required, current_user

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
                              name=form.name.data,
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Success! You are logged in as {user_to_create}', category='success')
        
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
            return redirect(url_for('tasks_page'))
        else:
            flash('Incorrect login/password. Try again!',category='danger')
    
    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'You have benn logged out. See you soon', category='info')
    return redirect(url_for('home_page'))

@app.route('/tasks', methods=['GET','POST'])
@login_required
def tasks_page():
    deletetask_form = DeleteTaskItemForm()
    changestatustask_form = ChangeStatusTaskItemForm()
    if request.method == 'POST':
        deleted_task = request.form.get('deleted_task')
        changedstatus_task = request.form.get('changedstatus_task')
        if deleted_task:
            task = TaskItem.query.filter_by(id=deleted_task).first()
            db.session.delete(task)
            db.session.commit()
            flash(f'Task "{task.description}" has been deleted.', category='success')
        if changedstatus_task:
            task = TaskItem.query.filter_by(id=changedstatus_task).first()
            if task.status == 'NotStarted':
                task.status = 'InProgress'
            else:
                if task.status == 'InProgress':
                    task.status = 'Done'
            #db.session.update(task)
            db.session.commit()
            flash(f'The Status of the Task "{task.description}" has been changed.', category='success')
    tasks = TaskItem.query.filter_by(owner = current_user.id)
    return render_template('tasks.html', tasks = tasks, deletetask_form=deletetask_form, changestatustask_form=changestatustask_form)

@app.route('/addtask', methods=['GET','POST'])
@login_required
def addtask_page():
    form = AddTaskItemForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            task_to_create = TaskItem(description=form.description.data, owner=current_user.id,status='NotStarted')
            db.session.add(task_to_create)
            db.session.commit()
            flash(f"Task created successfully for user {current_user.name}", category='success')
            return redirect(url_for('tasks_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error while addind this task: {err_msg}', category='danger')

    return render_template('addtask.html', form=form)