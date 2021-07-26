from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
from datetime import datetime
from refresh import refreshMsg
from static.python.functionsdb import *


app = Flask(__name__)
posts = []


@app.route("/recibir", methods=["GET", "POST"])
def ajax():
    if request.method in ["GET", "POST"]:
        return refreshMsg()


def createJson(user, text):
    time = getTime()
    jsonData = {
        "user": user,
        "time": time,
        "text": text
    }
    return jsonData


def getUserIdOrCreateIt(name):
    user = User()
    if not user.search(name):
        user.new(name)

    userId = user.getId(name)
    if __debug__:
        pass
    return userId


def saveMesage(text, userId):
    ahora = datetime.now()
    msg = Msg()
    msg.new(text, ahora, userId)


@app.route("/")
def index():
    print("/")
    return render_template("public/index.html")


@app.route("/enviar", methods=["GET", "POST"])
def enviar():
    print("enviar")

    def validateName(name):
        return not (len(name) > 50 or len(name) == 0)

    def validateMsg(msg):
        return not (len(msg) > 65535 or len(msg) == 0)

    if request.method == 'POST':
        name = request.form.to_dict()["fname"].lower()
        #  name = (requestFormated['user']).lower()
        text = request.form.to_dict()["ftext"]
        if not (validateName(name) and validateMsg(text)):
            return Flask.response_class(status='*')
            # return render_template("public/index.html")

        userId = getUserIdOrCreateIt(name)
        saveMesage(text, userId)

        # jsonData = createJson(name, msg)  # Guardamos el mensaje en un diccionario
        # posts.append(jsonData)  # Añadimos el diccionario a una tabla

        next = request.args.get('next', None)
        if next:
            return redirect(next)

        return Flask.response_class(status=200)
    return Flask.response_class(status='*')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
