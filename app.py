from datetime import datetime
import json
from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin
from static.python.refresh import refreshMsg
from static.python.functionsdb import Msg, User

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

posts = []
@app.route("/borrar", methods=["POST"])
@cross_origin()
def borrar():
    if request.is_json and "id_msg" in request.json:
        id_msg = request.json["id_msg"]
        msg = Msg()
        msg.delete(id_msg)

        return Flask.response_class(status=200)

    return Flask.response_class(status=405)


@app.route("/modificar", methods=["POST"])
@cross_origin()
def modificar():
    if request.is_json and "id_msg" in request.json and "txtChange" in request.json:
        id_msg = request.json["id_msg"]
        txt = request.json["txtChange"]
        msg = Msg()
        msg.modify(txt, id_msg)

        return Flask.response_class(status=200)

    return Flask.response_class(status=405)


@app.route("/recibir", methods=["GET", "POST"])
@cross_origin()
def ajax():
    if request.method == 'POST' and request.is_json \
            and "id_msg" in request.json:

        id_msg = request.json["id_msg"]
        return refreshMsg(id_msg)
    return Flask.response_class(status=405)


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


# @app.route("/")
# def index():
#     print("/")
#     return render_template("public/index.html")


@app.route("/enviar", methods=["GET", "POST"])
@cross_origin()
def enviar():

    def validateName(name):
        return not (len(name) > 50 or len(name) == 0)

    def validateMsg(msg):
        return not (len(msg) > 65535 or len(msg) == 0)

    # if not(request.headers["Content-Type"] == "application/json; charset=utf-8"):
    #     return "error"
    if request.method == 'POST' and request.is_json \
            and "user" in request.json and "txt" in request.json:

        name = request.json["user"].lower()
        text = request.json["txt"]

        if not (validateName(name) and validateMsg(text)):
            return Flask.response_class(status=400)

        userId = getUserIdOrCreateIt(name)
        saveMesage(text, userId)

        next = request.args.get('next', None)
        if next:
            return redirect(next)

        return Flask.response_class(status=200)
    return Flask.response_class(status=405)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
