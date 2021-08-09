import os 
from flask import Flask, render_template, send_from_directory, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

import psycopg2, pgdb #pg

load_dotenv()
app = Flask(__name__)
app.secret_key = "secret key"
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


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/cart")
def view_cart():
    return render_template("cart.html")

@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    cursor = None
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        #validate the received values
        if _quantity and _code and request.method == "POST":
            conn = pgdb.connect()
            cursor = conn.cursor(pgdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM product WHERE code=%s", _code)
            row = cursor.fetchone()

            itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity': _quantity, 'price': row['price'], 'image': row['image'], 'total_price': _quantity * row['price']}}

            all_total_price = 0
            all_total_quantity = 0

            session.modified = True
            if 'cart_item' in session:
                if row['code'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row['code'] == key:
                            #session.modified = True
                            #if session ['cart_item'][key]['quantity'] is not None:
                            #   session['cart_item][key]['quantity'] = 0
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['price']
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)

                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                    session['cart_item'] = itemArray
                    all_total_quantity = all_total_quantity + _quantity
                    all_total_price = all_total_price + _quantity * row['price']
            
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

            return redirect(url_for('.products'))
        
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)
    
    finally:
            cursor.close()
            conn.close()
    return render_template("cart.html")

@app.route("/empty", methods=["DELETE"])
def empty_cart(item_id):
    try:
        session.clear()
        return redirect(url_for('.products'))
    except Exception as e:
        print(e)
    return render_template("home.html")
    
@app.route("/delete/<string:code>", methods=["POST, PUT, DELETE"])
def delete_item(code):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True

        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

            if all_total_quantity == 0:
                session.clear()
            else:
                session['all_total_quantity'] = all_total_quantity
                session['all_total_price'] = all_total_price

            # return redirect('/')
            return redirect(url_for('.products'))
    
    except Exception as e:
        print(e)
    return render_template("cart.html")

def array_merge( first_array, second_array ):
    if isinstance( first_array , list) and isinstance( second_array , list):
        return first_array + second_array
    elif isinstance( first_array , dict) and isinstance( second_array , dict):
        return dict( list( first_array.items() ) + list( second_array.items() ) )    
    elif isinstance( first_array , set) and isinstance( second_array , set):
        return first_array.union( second_array )
    return False

# if __name__ == "__main__":
#     app.run()

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")


@app.route("/health")
def health():
    return "Hello, This is a Health Check and also a workflow check"
