from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------------------------------------------------
# Developmen parameters
# ---------------------------------------------------
# Have different database for development and deployment
ENV = "dev"
if ENV == "dev":
    from get_localhost import get_localhost
    URI = get_localhost()
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = URI
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = ""

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# TODO: Add safer secret key
app.config["SECRET_KEY"] = "pegasus-dev-team"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(32))


# ---------------------------------------------------
# Index page
# ---------------------------------------------------
@app.route('/')
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

# ---------------------------------------------------
# Login page
# ---------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    user = {
        "username": "lolo23jhon",
        "password": "pegasus"
    }

    # TODO: Connect validation to database
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == user["username"] and password == user["password"]:
            # TODO: Change redirection after succesful login
            return redirect(url_for("index"))
        else:
            error = "Invalid Credentials. Please ty again."

    return render_template("login.html", error=error)


# ---------------------------------------------------
# Profile page
# ---------------------------------------------------
@app.route("/user/<username>")
def profile(username):
    return render_template("profile.html")


if __name__ == "__main__":
    app.run()
