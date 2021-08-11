DROP TABLE IF EXISTS shoppingcart;

CREATE TABLE shoppingcart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mealName TEXT,
    calories INTEGER,
    price FLOAT
)