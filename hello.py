from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
import time
import datetime

app = Flask(__name__)
posts = []


def dataMoment():
    now = (time.time()//1)
    print(datetime.datetime.fromtimestamp(now).isoformat())
    return now


def createJson(user, text):
    print(len(text))
    time = dataMoment()
    jsonData = {
        "user": user,
        "time": time,
        "text": text
    }
    print(f'{jsonData}')
    return jsonData


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)


@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = (request.form['user']).lower()
        msg = request.form['text']
        jsonData = createJson(name, msg)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html")


@app.route('/')
def index():
    return render_template("index.html", num_posts=len(posts))
