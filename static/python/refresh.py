import static.python.functionsdb as db
from flask import jsonify


def refreshMsg():
    #  peticion a BBDD

    response = db.Msg.read(db.Msg())

    #  generar JSON desde el response de BDD

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

        mensajes["mensajes"].append(linea)

    response = jsonify(mensajes)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"

    return response
