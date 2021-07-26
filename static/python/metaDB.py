import os

cadenaConexion = {
    "host": "localhost",
    "user": "root",
    "passwd": "kronox",
    "db": "db1",
    "charset": 'utf8mb4'
}


def conexion():
    for var in cadenaConexion:
        if os.environ.get(var.upper()) is not None:
            cadenaConexion[var] = os.environ.get(var.upper())
    return cadenaConexion






