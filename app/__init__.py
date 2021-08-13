import os
from flask import Flask, render_template, send_from_directory, request, redirect, jsonify, session, url_for
from dotenv import load_dotenv, find_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from . import db
from functools import wraps
import json
from os import environ as env
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode


load_dotenv()
app = Flask(__name__)

oauth = OAuth(app)

app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.frm")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

auth0 = oauth.register(
    'auth0',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url='https://aviiii.us.auth0.com',
    access_token_url='https://aviiii.us.auth0.com/oauth/token',
    authorize_url='https://aviiii.us.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


@app.route('/callback')
def callback_handling():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    print(userinfo)
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture'],
        'username': userinfo['nickname'],
    }
    return redirect('/')


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='https://fresh-bites.tech/callback')


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            # Redirect to Login page here
            return redirect('/login')
        return f(*args, **kwargs)

    return decorated

# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route('/')
def dashboard():
    print(session.get('profile')    )
    return render_template('index.html',
                           userinfo=session.get('profile'),)


@app.route('/logout')
@requires_auth
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': 'https://fresh-bites.tech/', 'client_id': os.getenv('CLIENT_ID')}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))


@app.route("/shop")
@requires_auth
def shop():
    return render_template("shop.html")


@app.route("/cart")
@requires_auth
def cart():
    return render_template("cart.html")


@app.route("/confirm")
@requires_auth
def confirm():
    return render_template("confirm.html")


@app.route("/health")
def health():
    return "Hello, This is a Health Check and also a workflow check"
