import json
import static.python.functionsdb as db


def refreshMsg():
    #  peticion a BBDD

    response = db.returnMensages()

    #  generar JSON desde el response de BDD

    arrayRespuesta = []
    linea = []
    elemento = ""
    for row in response:
        linea.clear
        for item in row:
            elemento = str(item)
            linea.append(elemento)
            print(elemento)
        arrayRespuesta.append(linea)

    jsonToFront = json.dumps(arrayRespuesta, indent=4)

    # enviar JSON a FRONT

    return jsonToFront
