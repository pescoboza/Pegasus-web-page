# Import what we'll be using from the flask framework
from flask import Flask, render_template, request


# Metaparameters
# ---------------------------------------------------
IS_DEBUG = True

INDEX_HTML_PATH = "templates/"


# ---------------------------------------------------


# Define the app
app = Flask(__name__)

# Decorator for the routing


@app.route('/')
# Function for the index page
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = IS_DEBUG
    app.run()
