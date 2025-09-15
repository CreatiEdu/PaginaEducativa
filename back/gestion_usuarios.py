import mysql.connector
from mysql.connector import Error
import getpass

def crear_conexion():
    """
    Crea una conexión a la base de datos MySQL.
    Es idéntica a la de app.py, podría moverse a un módulo compartido.
    """
    try:
        # Reemplaza con tus propios datos de conexión si son diferentes
        conexion = mysql.connector.connect(
            host='192.168.100.8',
            user='root',
            password='12345',
            database='testback'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def agregar_usuario(username, password, rol):
    """Agrega un nuevo usuario a la base de datos."""
    conexion = crear_conexion()
    if conexion is None:
        return

    cursor = None
    try:
        cursor = conexion.cursor()
        # Asumiendo que la tabla 'usuarios' tiene las columnas: id (autoincrement), usuario, password, rol
        query = "INSERT INTO usuarios (usuario, password, rol) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, rol))
        conexion.commit()
        print(f"Usuario '{username}' agregado exitosamente.")
    except Error as e:
        print(f"Error al agregar el usuario: {e}")
        conexion.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def listar_usuarios():
    """Lista todos los usuarios de la base de datos."""
    conexion = crear_conexion()
    if conexion is None:
        return

    cursor = None
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT id_usuario, usuario FROM usuarios" # No seleccionamos la contraseña por seguridad
        cursor.execute(query)
        usuarios = cursor.fetchall()
        
        if not usuarios:
            print("No se encontraron usuarios.")
            return

        print("\n--- Lista de Usuarios ---")
        for usuario in usuarios:
            print(f"ID: {usuario['id_usuario']}, Usuario: {usuario['usuario']}")
        print("-------------------------\n")

    except Error as e:
        print(f"Error al listar los usuarios: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def modificar_usuario(user_id, nuevo_username, nuevo_rol):
    """Modifica el nombre de usuario y/o el rol de un usuario existente."""
    conexion = crear_conexion()
    if conexion is None:
        return

    cursor = None
    try:
        cursor = conexion.cursor()
        query = "UPDATE usuarios SET usuario = %s, rol = %s WHERE id_usuario = %s"
        cursor.execute(query, (nuevo_username, nuevo_rol, user_id))
        conexion.commit()
        if cursor.rowcount == 0:
            print(f"No se encontró ningún usuario con el ID {user_id}.")
        else:
            print(f"Usuario con ID {user_id} actualizado exitosamente.")
    except Error as e:
        print(f"Error al modificar el usuario: {e}")
        conexion.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def eliminar_usuario(user_id):
    """Elimina un usuario de la base de datos por su ID."""
    conexion = crear_conexion()
    if conexion is None:
        return

    cursor = None
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        cursor.execute(query, (user_id,))
        conexion.commit()
        if cursor.rowcount == 0:
            print(f"No se encontró ningún usuario con el ID {user_id}.")
        else:
            print(f"Usuario con ID {user_id} eliminado exitosamente.")
    except Error as e:
        print(f"Error al eliminar el usuario: {e}")
        conexion.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Gestión de Usuarios ---")
    print("1. Listar usuarios")
    print("2. Agregar usuario")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    """Función principal para ejecutar el gestor de usuarios."""
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            listar_usuarios()
        elif opcion == '2':
            username = input("Ingrese el nombre de usuario: ")
            password = getpass.getpass("Ingrese la contraseña: ")
            rol = input("Ingrese el rol (e.g., admin, profesor, estudiante): ")
            agregar_usuario(username, password, rol)
        elif opcion == '3':
            listar_usuarios()
            try:
                user_id = int(input("Ingrese el ID del usuario a modificar: "))
                nuevo_username = input("Ingrese el nuevo nombre de usuario: ")
                nuevo_rol = input("Ingrese el nuevo rol: ")
                modificar_usuario(user_id, nuevo_username, nuevo_rol)
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")
        elif opcion == '4':
            listar_usuarios()
            try:
                user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                # Confirmación antes de borrar
                confirmacion = input(f"¿Está seguro de que desea eliminar al usuario con ID {user_id}? (s/n): ").lower()
                if confirmacion == 's':
                    eliminar_usuario(user_id)
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()