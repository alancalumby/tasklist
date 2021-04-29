from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasklist.db'
db = SQLAlchemy(app)

class TaskItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(length=50), nullable = False, unique=True)
    status = db.Column(db.String(length=10), nullable = False)

    def __repr__(self):
        #return f'Task: {self.description}'
        return f'{self.description}'

@app.route('/')
@app.route('/home')
def home_page():
    tasks = TaskItem.query.all()
    return render_template('home.html', tasks = tasks)

@app.route('/about')
def about_page():
    return render_template('about.html')