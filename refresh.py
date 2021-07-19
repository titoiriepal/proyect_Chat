import json

# __debug__ = True
# ddbbDebug = __debug__
# noLoop = True

# infiniteLoop = True

# while infiniteLoop:
#     infiniteLoop = not noLoop


def refreshMsg():
    # TODO peticion a BBDD

    response = None

    # TODO mockear el response

    data = None
    mensajes = []
    with open("refreshMocker.json") as jsonFile:
        data = json.load(jsonFile)

    for element in data["mensajes"]:
        mensaje = [
            element["user"],
            element["timestamp"],
            element["txt"]
            ]
        mensajes.append(mensaje)

    # print(mensajes)
    response = mensajes

    # TODO generar JSON desde el response de BDD

    jsonToFront = json.dumps(response, indent=4)

    print(jsonToFront)

    # TODO enviar JSON a FRONT

    return jsonToFront

    # TODO esperar 1 segundo
