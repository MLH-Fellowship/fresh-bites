from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home</p>"

@app.route("/shop")
def shop():
    return "<p>Shopping cart</p>"

@app.route("/confirm")
def confirm():
    return "<p>Confirm</p>"

@app.route("/Food")
def food_info():
    return "<p>Food page maybe</p>"