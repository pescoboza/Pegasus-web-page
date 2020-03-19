from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

# TODO: Add safer secret key
app.config["SECRET_KEY"] = "pegasus-dev-team"


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
    app.debug = True  # Remember to change debug mode
    app.run()
