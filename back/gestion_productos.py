
import mysql.connector
from mysql.connector import Error

# ...existing code...

if __name__ == "__main__":
    print("--- Prueba CRUD de productos ---")
    # Crear producto
    crear_producto("Cuaderno de comunicados", 1500.00, 100)
    crear_producto("Uniforme escolar", 5000.00, 50)
    crear_producto("Libro escolar", 2500.00, 30)
    # Listar productos
    listar_productos()
    # Modificar producto (ejemplo: cambiar precio y stock del producto 1)
    modificar_producto(1, nuevo_precio=1600.00, nuevo_stock=90)
    # Listar productos para ver cambios
    listar_productos()
    # Eliminar producto (ejemplo: eliminar producto 2)
    eliminar_producto(2)
    # Listar productos para ver cambios
    listar_productos()


import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """
    Crea una conexión a la base de datos MySQL.
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='testback'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None


def crear_producto(nombre, precio, stock):
    """
    Crea un nuevo producto y lo agrega a la base de datos.
    """
    conexion = crear_conexion()
    if conexion is None:
        return
    cursor = None
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, precio, stock))
        conexion.commit()
        print(f"✅ Producto '{nombre}' creado correctamente.")
    except Error as e:
        print(f"Error al crear el producto: {e}")
        conexion.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()



def listar_productos():
    """
    Muestra la lista completa de productos desde la base de datos.
    """
    conexion = crear_conexion()
    if conexion is None:
        return
    cursor = None
    try:
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT id_producto, nombre, precio, stock FROM productos"
        cursor.execute(query)
        productos = cursor.fetchall()
        if not productos:
            print("📭 No hay productos cargados.")
            return
        print("\n📋 Lista de productos:")
        for p in productos:
            print(f"ID: {p['id_producto']} | Nombre: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")
    except Error as e:
        print(f"Error al listar productos: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()



def modificar_producto(id_producto, nuevo_nombre=None, nuevo_precio=None, nuevo_stock=None):
    """
    Modifica los datos de un producto existente en la base de datos según su ID.
    """
    conexion = crear_conexion()
    if conexion is None:
        return
    cursor = None
    try:
        cursor = conexion.cursor()
        campos = []
        valores = []
        if nuevo_nombre is not None:
            campos.append("nombre = %s")
            valores.append(nuevo_nombre)
        if nuevo_precio is not None:
            campos.append("precio = %s")
            valores.append(nuevo_precio)
        if nuevo_stock is not None:
            campos.append("stock = %s")
            valores.append(nuevo_stock)
        if not campos:
            print("No se proporcionaron datos para modificar.")
            return
        valores.append(id_producto)
        query = f"UPDATE productos SET {', '.join(campos)} WHERE id_producto = %s"
        cursor.execute(query, tuple(valores))
        conexion.commit()
        if cursor.rowcount == 0:
            print(f"❌ No se encontró el producto con ID {id_producto}.")
        else:
            print(f"✏️ Producto con ID {id_producto} modificado correctamente.")
    except Error as e:
        print(f"Error al modificar el producto: {e}")
        conexion.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()



def eliminar_producto(id_producto):
    """
    Elimina un producto de la base de datos por su ID.
    """
    conexion = crear_conexion()
    if conexion is None:
        return
    cursor = None
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id_producto = %s"
        cursor.execute(query, (id_producto,))
        conexion.commit()
        if cursor.rowcount == 0:
            print(f"❌ No se encontró el producto con ID {id_producto}.")
        else:
            print(f"🗑️ Producto con ID {id_producto} eliminado correctamente.")
    except Error as e:
        print(f"Error al eliminar el producto: {e}")
        conexion.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()
