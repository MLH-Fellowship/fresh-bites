import os
from flask import Flask, render_template, send_from_directory, request, redirect
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

load_dotenv()
app = Flask(__name__)
app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.frm")


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


@app.route("/health")
def health():
    return "Hello, This is a Health Check and also a workflow check"
