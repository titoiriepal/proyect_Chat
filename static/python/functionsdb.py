#!/usr/bin/python

import pymysql


def introUser(name):
    conn = pymysql.connect(
        host="localhost", user="root",
        passwd="krono", db="db1")
    try:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO usuarios (nombre) values ("%s")', (name))

    finally:
        conn.commit()
        conn.close()


def searchUser(name):
    conn = pymysql.connect(
        host="localhost", user="root",
        passwd="krono", db="db1")
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT id_usr FROM usuarios where nombre = %s', ("Fran"))
            rows = cur.fetchall()
            return rows[0]
    finally:
        conn.close()


def introMsg(text, date, idUser):
    conn = pymysql.connect(
        host="localhost", user="root",
        passwd="krono", db="db1")
    try:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO mensajes (texto, fecha, usuario) values (%s, %s, %s)', (text, date, idUser))

    finally:
        conn.commit()
        conn.close()


def returnMensages():
    conn = pymysql.connect(
        host= "localhost", user="root",
        passwd="krono", db="db1")
    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM
            (SELECT u.nombre, m.fecha, m.texto
            FROM usuarios AS u
            JOIN mensajes AS m ON u.id_usr = m.usuario
            ORDER BY m.fecha DESC
            LIMIT 100
            ) AS t
            ORDER BY t.fecha ASC;""")     
            rows = cur. fetchall()
            return rows
    finally:
        conn.close()