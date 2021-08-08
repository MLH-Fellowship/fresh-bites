import os
from flask import Flask, render_template, send_from_directory, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    user=os.getenv("POSTGRES_USER"),
    passwd=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    table=os.getenv("POSTGRES_DB"),
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# create class model for login/signup and cart


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shop", methods=("GET","POST","PUT","DELETE"))
def shop():
    if "shopcart" not in session:
        flash("Your cart is empty")
    else:
        items = session["shopcart"]
        dict_of_items = {}

        total = 0
        for item in items:
            item = item.get_item_by_id(item)
            total += item.price
            if item.id in dict_of_items:
                dict_of_items[item.id]["qty"] += 1
            else:
                dict_of_items[item.id] = {"qty":1, "name": item.common_name, "price": item.price}
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
