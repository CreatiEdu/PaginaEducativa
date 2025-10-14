# db_connection.py
import mysql.connector
from mysql.connector import Error

# Función para establecer la conexión

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="testback"
        )
        if conexion.is_connected():
            print("✅ Conexión establecida con la base de datos")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

# Función para cerrar la conexión
def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("🔒 Conexión cerrada correctamente")
