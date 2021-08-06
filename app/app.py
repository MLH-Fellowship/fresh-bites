from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home</p>"

@app.route("/shop", methods=("GET","POST","PUT","DELETE"))
def shop():
    return "<p>Shopping cart</p>"

@app.route("/confirm")
def confirm():
    return "<p>Confirm</p>"

@app.route("/reminder")
def food_info():
    return "<p>Remind them to drink water</p>"