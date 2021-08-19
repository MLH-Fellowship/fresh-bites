# Bring in Auth0 to make the user database

`oauth = OAuth(app)

app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.frm")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`

# The auth0 register object - handles user access tokens, id number, secret keys, and authorization

`auth0 = oauth.register(
    "auth0",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url="https://aviiii.us.auth0.com",
    access_token_url="https://aviiii.us.auth0.com/oauth/token",
    authorize_url="https://aviiii.us.auth0.com/authorize",
    client_kwargs={
        "scope": "openid profile email",
    },
)`

# this creates the login page. Handles the info from the auth0 object, 
# plus the userinfo and profile. The profile is an object that includes user id and username

`@app.route("/callback")
def callback_handling():
    auth0.authorize_access_token()
    resp = auth0.get("userinfo")
    userinfo = resp.json()
    print(userinfo)
    session["jwt_payload"] = userinfo
    session["profile"] = {
        "user_id": userinfo["sub"],
        "name": userinfo["name"],
        "picture": userinfo["picture"],
        "username": userinfo["nickname"],
    }
    return redirect("/")`

# login route, returns the auth0 object via the callback route

`@app.route("/login")
def login():
    return auth0.authorize_redirect(redirect_uri="https://fresh-bites.tech/callback")`

# This object makes sure that a user is logged in to their account
# if not in session, user is redirected to the login page

`def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "profile" not in session:
            # Redirect to Login page here
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated


@app.route("/")
def dashboard():
    print(session.get("profile"))
    return render_template(
        "index.html",
        userinfo=session.get("profile"),
    )
`
# This route handles logging out

`@app.route("/logout")
@requires_auth
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {
        "returnTo": "https://fresh-bites.tech/",
        "client_id": os.getenv("CLIENT_ID"),
    }
    return redirect(auth0.api_base_url + "/v2/logout?" + urlencode(params))`

# This route handles the shopping page, where a user makes their purchase(s)

`@app.route("/shop", methods=["GET", "POST"])
@requires_auth
def shop():
    # brings in the recipes section of the spoonacular API
    # that allows people to search for recipes
    url1 = (
        "https://api.spoonacular.com/recipes/complexSearch?"
        + "apiKey=fb792615575548c5ae4a59c9df46183d"
    )
    # recipes search query object with some default attributes
    querystring1 = {
        "query": "salad",
        "offset": "0",
        "number": "50",
        "minCalories": "0",
        "maxCalories": "500",
        "minProtein": "0",
        "maxProtein": "100",
        "minFat": "0",
        "maxFat": "100",
        "minCarbs": "0",
        "maxCarbs": "50",
    }
    # brings in a secret key that allows the app to handle 
    # requests
    headers1 = {
        "apiKey": "fb792615575548c5ae4a59c9df46183d",
    }
    # This the ingredients search function
    res1 = requests.request("GET", url1, params=querystring1)
    # print(res.json())
    result1 = res1.json().get("results")
    # This is the API call for the ingredients search
    url2 = (
        "https://api.spoonacular.com/food/ingredients/search?"
        + "apiKey=fb792615575548c5ae4a59c9df46183d"
    )
    # This is the search query object for the ingredients search
    querystring2 = {
        "query": "apple",
        "offset": "0",
        "number": "50",
        "addChildren": "true",
    }

    res = requests.request("GET", url2, params=querystring2)
    #print(res.json())
    result2 = res.json().get("results")

    return render_template(
        "shop.html", res=result1, res2=result2, userinfo=session.get("profile")
    )`

# The route for the food information

`@app.route("/foodinfo", methods=["GET", "POST"])
def foodinfo():
    render_template("foodinfo.html")`

# This route handles the shopping cart. It requires the user
# to be logged in to view cart

`@app.route("/cart")
@requires_auth
def cart():
    return render_template("cart.html", userinfo=session.get("profile"))`

# The confirmation page after the order is confirmed, which
# also requires the user to be logged in to confirm order. 

`@app.route("/confirm")
@requires_auth
def confirm():
    return render_template(
        "confirm.html",
        userinfo=session.get("profile"),
    )`

# This route is the health and workflow check

`@app.route("/health")
def health():
    return "Hello, This is a Health Check and also a workflow check"`
