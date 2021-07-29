import operator
from flask import jsonify
import static.python.functionsdb as db


def refreshMsg(id_msg):
    #  peticion a BBDD
    response = db.Msg.read(db.Msg(), id_msg)

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
