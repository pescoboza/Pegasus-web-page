# Import what we'll be using from the flask framework
from flask import Flask, render_template, redirect, request


# Metaparameters
# ---------------------------------------------------
IS_DEBUG = True
# ---------------------------------------------------


# Define the app
app = Flask(__name__)

# ---------------------------------------------------
# Index page
# ---------------------------------------------------
@app.route('/')
@app.route("/index")
@app.route("/home")
def index():

    user_A = {"username": "Peggy"}

    user_B = {"username": "Lolo"}

    posts = [
        {
            "author": user_A,
            "body": "Hello I am Peggy."
        },
        {
            "author": user_B,
            "body": "Hello I am user Lolo."
        }
    ]

    return render_template("index.html",
                           username=user_A["username"],
                           posts=posts)

# ---------------------------------------------------
# Login page
# ---------------------------------------------------
@app.route("/login")
def login():
    return render_template("login.html")

# ---------------------------------------------------
# Login request page
# ---------------------------------------------------
@app.route("/login_success", methods=["GET", "POST"])
def login_submit():
    # POST: login user
    if request.method == "POST":
        # Get for fields
        username = request.form.get("username")
        password = request.form.get("password")
        remember_me = request.form.get("checked")

        # TODO: Query for valid user
        valid_credentials = True
        if not valid_credentials:
            # TODO: Add failed login message
            return render_template("login.html", failed_login=True)

        print(username, password, remember_me)

    return render_template("login_success.html")


# ---------------------------------------------------
# Profile page
# ---------------------------------------------------
@app.route("/user/<username>")
def profile(username):
    return render_template("profile.html")


if __name__ == "__main__":
    app.debug = True  # Remember to change debug mode
    app.run()
