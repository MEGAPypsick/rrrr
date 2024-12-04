from  flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('hello')

@app.route("/login")
def login():
    return render_template('login')

@app.route("/register")
def register():
    return render_template('register')

app.run()