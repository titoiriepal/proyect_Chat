from datetime import datetime
import json
from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin
from static.python.refresh import refreshMsg
from static.python.functionsdb import Msg, User

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

posts = []


@app.route("/recibir", methods=["GET", "POST"])
@cross_origin()
def ajax():
    if request.method in ["GET", "POST"]:
        return refreshMsg()


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

    def validateName(name):
        return not (len(name) > 50 or len(name) == 0)

    def validateMsg(msg):
        return not (len(msg) > 65535 or len(msg) == 0)

    if request.method == 'POST':
        diccionarioRequest = request.form.to_dict()
        valores = json.loads(diccionarioRequest["jsonString"])
        name = valores["user"].lower()
        text = valores["txt"]

        if not (validateName(name) and validateMsg(text)):
            return Flask.response_class(status='*')

        userId = getUserIdOrCreateIt(name)
        saveMesage(text, userId)

        next = request.args.get('next', None)
        if next:
            return redirect(next)

        return Flask.response_class(status=200)
    return Flask.response_class(status='*')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
