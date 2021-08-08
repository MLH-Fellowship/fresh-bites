from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/confirm")
def confirm():
    return render_template("confirm.html")
