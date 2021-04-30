from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasklist.db'
app.config['SECRET_KEY'] = 'f8742364ff5fc47c83ca01ee'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from tasklist import routes