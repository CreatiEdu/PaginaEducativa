# pedidos.py
from db_connection import crear_conexion, cerrar_conexion

def consultar_pedidos_completos():
    """
    Consulta los pedidos con información del producto, usuario y rol.
    """
    conexion = crear_conexion()
    resultados = []

    if conexion:
        cursor = None
        try:
            cursor = conexion.cursor(dictionary=True)
            query = """
            SELECT 
                pedido.id_pedido,
                pedido.nombre_producto,
                productos.precio AS precio_unitario,
                pedido.total,
                pedido.fecha_pedido,
                usuarios.nombre AS nombre_usuario,
                usuarios.apellido AS apellido_usuario,
                roles.rol AS nombre_rol
            FROM pedido
            INNER JOIN productos ON pedido.id_producto = productos.id_producto
            INNER JOIN usuarios ON pedido.id_usuario = usuarios.id_usuario
            INNER JOIN roles ON usuarios.rol = roles.id_rol
            ORDER BY pedido.id_pedido ASC;
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
        except Exception as e:
            print(f" Error al ejecutar la consulta: {e}")
        finally:
            if cursor:
                cursor.close()
            cerrar_conexion(conexion)  

    return resultados


def main():
    pedidos = consultar_pedidos_completos()

    if pedidos:
        print("--- Pedidos Completos ---")
        for p in pedidos:
            print(f"""
Pedido ID: {p['id_pedido']}
Producto: {p['nombre_producto']}
Precio Unitario: ${p['precio_unitario']}
Usuario: {p['nombre_usuario']} {p['apellido_usuario']} ({p['nombre_rol']})
Fecha Pedido: {p['fecha_pedido']}
Total: ${p['total']}
----------------------------------------
""")
    else:
        print("No se encontraron pedidos o hubo un error en la conexión/consulta.")


if __name__ == "__main__":
    main()
