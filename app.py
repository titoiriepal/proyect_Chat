from datetime import datetime
import operator
import json
from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import cross_origin
from static.python.functionsdb import Msg, User

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
posts = []
@app.route("/borrar", methods=["POST", "GET"])
@cross_origin()
def borrar():
    if request.method == 'POST':
        if not request.is_json or "id_msg" not in request.json:
            return Flask.response_class(status=405)
        id_msg = request.json["id_msg"]

    if request.method == "GET":
        if not request.args.get('id_msg'):
            return Flask.response_class(status=405)
        id_msg = request.args.get('id_msg')
    msg = Msg()
    msg.delete(id_msg)
    return Flask.response_class(status=200)

@app.route("/modificar", methods=["POST", "GET"])
@cross_origin()
def modificar():
    if request.method == 'POST':
        if not request.is_json \
                or "id_msg" not in request.json or "txtChange" not in request.json:
            return Flask.response_class(status=405)
        id_msg = request.json["id_msg"]
        txt = request.json["txtChange"]

    if request.method == "GET":
        if not request.args.get('id_msg') or not request.args.get('txtChange'):
            return Flask.response_class(status=405)
        id_msg = request.args.get('id_msg')
        txt = request.args.get('txtChange')
    msg = Msg()
    msg.modify(txt, id_msg)
    return Flask.response_class(status=200)



@app.route("/recibir", methods=["GET", "POST"])
@cross_origin()
def ajax():
    if request.method == "POST":
        if not request.is_json or "id_msg" not in request.json:
            return Flask.response_class(status=405)
        id_msg = request.json["id_msg"]

    if request.method == "GET":
        if not request.args.get('id_msg'):
            return Flask.response_class(status=405)
        id_msg = request.args.get('id_msg')

        #  if not request.is_json or "id_msg" not in request.json:
        #  return Flask.response_class(status=405)

    return refreshMsg(id_msg)


def refreshMsg(id_msg):
    #  peticion a BBDD
    response = Msg.read(Msg(), id_msg)

    #  generar JSON desde el response de BDD
    response.sort(key=operator.itemgetter('fecha'))

    mensajes = {"mensajes": []}
    for row in response:
        linea = {}
        for item in row:
            if (item == "nombre"):
                linea["user"] = row["nombre"]
            elif (item == "fecha"):
                linea["datetime"] = str(row["fecha"])
            elif (item == "texto"):
                linea["txt"] = row["texto"]
            elif (item == "id_msg"):
                linea["id_msg"] = row["id_msg"]

        mensajes["mensajes"].append(linea)

    response = jsonify(mensajes)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"

    return response


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

@app.route("/enviar", methods=["GET", "POST"])
@cross_origin()
def enviar():

    def validateName(name):
        return not (len(name) > 50 or len(name) == 0)

    def validateMsg(msg):
        return not (len(msg) > 65535 or len(msg) == 0)

    # if not(request.headers["Content-Type"] == "application/json; charset=utf-8"):
    #     return "error"
    if request.method == "POST":
        if not request.is_json or "user" not in request.json or "txt" not in request.json:
            return Flask.response_class(status=405)
        name = request.json["user"].lower()
        text = request.json["txt"]

    if request.method == "GET":
        if not request.args.get('user') or not request.args.get('text'):
            return Flask.response_class(status=405)
        name = request.args.get('user')
        text = request.args.get('text')

    if not (validateName(name) and validateMsg(text)):
        return Flask.response_class(status=400)

    userId = getUserIdOrCreateIt(name)
    saveMesage(text, userId)

    next = request.args.get('next', None)
    if next:
        return redirect(next)

    return Flask.response_class(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
