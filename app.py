from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return 'This is the home page!'

@app.route('/about')
def about_page():
    return 'This is the about page'