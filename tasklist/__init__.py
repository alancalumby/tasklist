from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasklist.db'
app.config['SECRET_KEY'] = 'f8742364ff5fc47c83ca01ee'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_mgr = LoginManager(app)
login_mgr.login_view = "login_page"
login_mgr.login_message_category = "info"

from tasklist import routes