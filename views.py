from app import app
from flask import render_template
from refresh import refreshMsg
from flask import request


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/ajax", methods=["GET", "POST"])
def ajax():
    if request.method == "POST":
        return refreshMsg()
    if request.method == "GET":
        return refreshMsg()


@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """
