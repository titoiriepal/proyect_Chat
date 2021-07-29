import pymysql
from .metaDB import conexion


class DdbbObj:
    cadenaConexion = conexion()

    def __init__(self):
        self.connection = pymysql.connect(
            host=self.cadenaConexion["APP_HOST"],
            user=self.cadenaConexion["APP_USER"],
            passwd=self.cadenaConexion["APP_PASSWD"],
            db=self.cadenaConexion["APP_DB"],
            charset=self.cadenaConexion["APP_CHARSET"],
            cursorclass=pymysql.cursors.DictCursor
        )


class User(DdbbObj):

    def new(self, name):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO usuarios (nombre) values (%s)"
            cursor.execute(sql, (name))
        self.connection.commit()

    def search(self, name):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE nombre = %s"
            cursor.execute(sql, name)
            rows = cursor.fetchall()

            found = len(rows) >= 1
            return found

    def getId(self, name):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT id_usr FROM usuarios where nombre = %s"
            cursor.execute(sql, name)
            result = cursor.fetchone()

            # if __debug__:
            #     print(f"{type(result)} - {result}")

            return result['id_usr']


class Msg(DdbbObj):

    def new(self, text, date, idUser):
        with self.connection.cursor() as cursor:
            sql = 'INSERT INTO mensajes (texto, usuario) values (%s, %s)'
            cursor.execute(sql, (text, idUser))
            self.connection.commit()

    def read(self, id_msg):
        with self.connection.cursor() as cursor:
            sql = (f"""
                        SELECT u.nombre, m.fecha, m.texto, m.id_msg
                        FROM usuarios AS u
                        JOIN mensajes AS m ON u.id_usr = m.usuario
                        WHERE m.id_msg > {id_msg}
                        ORDER BY m.fecha DESC
                        LIMIT 100
                    """)
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
