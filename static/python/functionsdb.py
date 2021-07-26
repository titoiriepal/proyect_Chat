#!/usr/bin/python

import pymysql
from .metaDB import conexion


class DdbbObj:
    cadenaConexion = conexion()
    connection = pymysql.connect(
        host=cadenaConexion["APP_HOST"],
        user=cadenaConexion["APP_USER"],
        passwd=cadenaConexion["APP_PASSWD"],
        db=cadenaConexion["APP_DB"],
        charset=cadenaConexion["APP_CHARSET"],
        cursorclass=pymysql.cursors.DictCursor
    )


class User(DdbbObj):

    

    def new(self, name):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO usuarios (nombre) values (%s)"
            cursor.execute(sql, (name))

        # self.connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()

    def search(self, name):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE nombre = %s"
            cursor.execute(sql, name)
            rows = cursor.fetchall()

            found = len(rows) >= 1
            # if __debug__:
            #     print('============================================')
            #     print(type(rows))
            #     print(rows)

            #     for user in rows:
            #         print(type(user))
            #         print(user['nombre'])
                
            #     print('Nombre encontrado' if found else 'Nombre no encontrado')

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
            sql = 'INSERT INTO mensajes (texto, fecha, usuario) values (%s, %s, %s)'
            cursor.execute(sql, (text, date, idUser))
            self.connection.commit()

    def read(self):
        with self.connection.cursor() as cursor:
            sql = """SELECT * FROM
                    (
                        SELECT u.nombre, m.fecha, m.texto
                        FROM usuarios AS u
                        JOIN mensajes AS m ON u.id_usr = m.usuario
                        ORDER BY m.fecha DESC
                        LIMIT 100
                    ) AS t
                    ORDER BY t.fecha ASC;"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            # if __debug__:
            #     print(f"{type(rows)}")
            #     print(rows)
            return rows
