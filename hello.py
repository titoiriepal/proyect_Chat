from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
import time
import datetime

app = Flask(__name__)
posts = []


def getTime():
    now = (time.time()//1)
    return now


def createJson(user, text):
    print(len(text))
    time = getTime()
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
        if not validate(name, msg):
            return render_template("signup_form.html")
        jsonData = createJson(name, msg) #Guardamos el mensaje en un diccionario
        posts.append(jsonData) # Añadimos el diccionario a una tabla
        print(posts)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return render_template("signup_form.html", posts=posts)
    return render_template("signup_form.html", posts=posts)


def validate(name, msg):
    
    if len(name) > 50 or len(name) == 0:
        return False
    
    if len(msg) > 65535 or len(msg) == 0:
        return False
    return True





@app.route('/')
def index():
    return render_template("index.html", posts=posts)