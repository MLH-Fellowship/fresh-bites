from flask import Flask, render_template, session, flash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

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
    return render_template('shop.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/confirm")
def confirm():
    return render_template('confirm.html')