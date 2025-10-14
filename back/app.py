
from db_connection import crear_conexion, cerrar_conexion



def verificar_credenciales(username, password):
    """Verifica las credenciales del usuario en la base de datos."""
    conexion = crear_conexion()
    if conexion is None:
        return None

    cursor = None
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(query, (username, password))
        usuario = cursor.fetchone()
        return usuario 
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)
        print("Conexión a MySQL cerrada.")

def main():
    """Función principal para ejecutar el login de consola."""
    print("--- Sistema de Login con Base de Datos ---")
    
    username_ingresado = input("Nombre de usuario: ")
    password_ingresado = input("Contraseña: ")

    usuario_logueado = verificar_credenciales(username_ingresado, password_ingresado)

    if usuario_logueado:
        print(f"\n¡Login exitoso! Bienvenido, {usuario_logueado['usuario']}.")
    else:
        print("\nNombre de usuario o contraseña incorrectos.")


if __name__ == "__main__":
    main()
