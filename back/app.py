import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """Crea una conexión a la base de datos MySQL."""
    try:
        # Reemplaza con tus propios datos de conexión
        conexion = mysql.connector.connect(
            host='192.168.100.8',
            user='root',  # Tu usuario de MySQL (comúnmente 'root')
            password='12345', # La contraseña que estableciste para MySQL
            database='testback'
        )
        if conexion.is_connected():
            print("Conexión a la base de datos MySQL exitosa.")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def verificar_credenciales(username, password):
    """Verifica las credenciales del usuario en la base de datos."""
    conexion = crear_conexion()
    if conexion is None:
        return None

    cursor = None
    try:
        cursor = conexion.cursor(dictionary=True)
        # Consulta parametrizada para evitar inyección SQL
        query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(query, (username, password))
        usuario = cursor.fetchone()
        return usuario # Devuelve los datos del usuario o None si no se encuentra
            
    except Error as e:
        print(f"Error al realizar la consulta: {e}")
        return None
    finally:
        # Asegurarse de cerrar el cursor y la conexión
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()
            print("Conexión a MySQL cerrada.")

def main():
    """Función principal para ejecutar el login de consola."""
    print("--- Sistema de Login con Base de Datos ---")
    
    # Solicitar credenciales al usuario
    username_ingresado = input("Nombre de usuario: ")
    password_ingresado = input("Contraseña: ")

    usuario_logueado = verificar_credenciales(username_ingresado, password_ingresado)

    if usuario_logueado:
        print(f"\n¡Login exitoso! Bienvenido, {usuario_logueado['usuario']}.")
        # Aquí podrías usar otros datos, por ejemplo: print(f"Tu rol es: {usuario_logueado['rol']}")
    else:
        print("\nNombre de usuario o contraseña incorrectos.")


if __name__ == "__main__":
    main()
