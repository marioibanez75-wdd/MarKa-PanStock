
#Saca hago la xonexion con mysql

import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    """Establece una conexión con la base de datos PanStock."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            database="panstock",
            user="panstock_app",
            password="Programacion_2026!"
        )

        if conexion.is_connected():
            return conexion

        raise Error("No se pudo establecer la conexión con MySQL.")

    except Error as error:
        raise Error(f"Error de conexión con MySQL: {error}") from error

