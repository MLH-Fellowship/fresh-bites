from flask import Flask, request, session, render_template, g, redirect, url_for, flash 

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home</p>"

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
    return "<p>Shopping cart</p>"

@app.route("/confirm")
def confirm():
    return "<p>Confirm</p>"

@app.route("/reminder")
def food_info():
    return "<p>Remind them to drink water</p>"