from flask import render_template
from .. import app

@app.errorhandler(404)
def error_404():
    render_template("404.html")

@app.errorhandler(403)
def error_403():
    render_template("403.html")

@app.errorhandler(500)
def error_500():
    render_template("500.html")