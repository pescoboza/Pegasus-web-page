from flask import render_template, request
from ..models.user import User
from .. import app, db
from ..forms.login_form import LoginForm

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

    form = LoginForm()

    # Check for a POST request
    if request.method == "POST" and form.validate_on_submit():
        username = form.username
        password = form.password
        
        # Query for the user with that username
        user =  db.session.query(User).filter(User.username == username)[0]:
        # Check the password
        if user and user.password == password:
            # TODO: Keep track of the logged in user in the current session
            # TODO: Add logout option
            return render_template("index.html", username=username)

        return render_template("login.html", message="Invalid credentials. Please try again.")
        

    return render_template("login.html", form=form)


# ---------------------------------------------------
# Profile page
# ---------------------------------------------------
@app.route("/user/<username>")
def profile(username):
    return render_template("profile.html")


# ---------------------------------------------------
# Testing development page
# ---------------------------------------------------
@app.route("/dev-all-members")
def all_members():
    page = str()
    line =  "<h1>{}</h1><br>"
    for i in range(10):
        page += line.format(i)
    return page