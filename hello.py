from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
import time
from refresh import refreshMsg
import static/python/functionsdb


app = Flask(__name__)
posts = []


@app.route("/ajax", methods=["GET", "POST"])
def ajax():
    if request.method == "POST":
        return refreshMsg()
    if request.method == "GET":
        return refreshMsg()


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
    return jsonData


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = (request.form['user']).lower()
        msg = request.form['text']
        if not validate(name, msg):
            return render_template("public/index.html")
        jsonData = createJson(name, msg)  # Guardamos el mensaje en un diccionario
        posts.append(jsonData)  # Añadimos el diccionario a una tabla
        print(posts)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return render_template("public/index.html", posts=posts)
    return render_template("public/index.html", posts=posts)


def validate(name, msg):

    if len(name) > 50 or len(name) == 0:
        return False

    if len(msg) > 65535 or len(msg) == 0:
        return False
    return True
