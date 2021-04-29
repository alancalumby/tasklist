from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    tasks = [
        {'id': 1, 'description' : 'Drink water','status': 'InProgress'},
        {'id': 2, 'description' : 'Eat','status': 'InProgress'},
        {'id': 3, 'description' : 'Go home','status': 'NotStarted'},
        {'id': 4, 'description' : 'Study Flask','status': 'Done'}
    ]
    return render_template('home.html', tasks = tasks)

@app.route('/about')
def about_page():
    return render_template('about.html')