import os

cadenaConexion = {
    "APP_HOST": "localhost",
    "APP_USER": "root",
    "APP_PASSWD": "krono",
    "APP_DB": "db1",
    "APP_CHARSET": 'utf8mb4'
}


def conexion():
    for var in cadenaConexion:
        if os.environ.get(var.upper()) is not None:
            cadenaConexion[var] = os.environ.get(var.upper())
    return cadenaConexion






