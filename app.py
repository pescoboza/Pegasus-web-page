# Import what we'll be using from the flask framework
from flask import Flask, render_template, request


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
# Function for the index page
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
# Profile page
# ---------------------------------------------------
@app.route("user/<username>")
def profile(username):
    return render_template("profile.html")


if __name__ == "__main__":
    app.debug = IS_DEBUG
    app.run()
