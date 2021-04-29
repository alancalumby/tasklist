from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasklist.db'
app.config['SECRET_KEY'] = 'f8742364ff5fc47c83ca01ee'
db = SQLAlchemy(app)

from tasklist import routes