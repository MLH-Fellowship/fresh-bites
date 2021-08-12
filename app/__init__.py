import os
from flask import (
    Flask,
    render_template,
    send_from_directory,
    request,
    redirect,
    jsonify,
)

"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
"""
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

load_dotenv()
app = Flask(__name__)
app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.frm")
"""
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    user=os.getenv("POSTGRES_USER"),
    passwd=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    table=os.getenv("POSTGRES_DB"),
)

db.init_app(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
"""


# create class model for login/signup and cart


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
