# Importar módulos
import sqlite3
from colorama import init, Fore, Back, Style
import os

os.system("clear")
# Iniciar colorama
init(autoreset=True)

# Inicialización de la conexión a base de datos
def conectar(database):
    conexion = sqlite3.connect(database)
    return conexion

"""
Funciones del sistema
"""

# UNIQUE
def crear_tabla():
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL, 
        nombre TEXT NOT NULL,
        descripcion TEXT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL, 
        categoria TEXT NULL)
        """
    )
    # Confirmar
    conn.commit()
    # Cerrar la conexión
    conn.close()

# Llamar a la función para crear la tabla
crear_tabla()

# Validar entrada entera
def validar_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        print(f"{Fore.RED}Por favor, ingrese un número válido.")

# Insertar
def insertar_producto():
    codigo = input("Ingrese código del producto: ")
    nombre = input("Ingrese nombre del producto: ")
    descripcion = input("Ingrese descripción del producto: ")
    categoria = input("Ingrese categoría del producto: ")
    cantidad = validar_entero("Ingrese cantidad del producto: ")
    precio = float(input("Ingrese precio del producto: "))

    # Llamar a la conexión
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (codigo, nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?,?)",
        (codigo, nombre, descripcion, cantidad, precio, categoria),
    )
    conn.commit()
    print(f"{Fore.GREEN}\nProducto registrado exitosamente.\n")
    conn.close()

# Mostrar
def mostrar_productos():
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    respuesta = cursor.fetchall()  # Lista
    if len(respuesta) > 0:
        for item in respuesta:
            print(
                f"{Fore.MAGENTA}ID: {item[0]} | CODIGO: {item[1]} | NOMBRE: {item[2]} | DESC: {item[3]} | CANTIDAD: {item[4]} | PRECIO: ${item[5]} | CATEGORÍA: {item[6]}"
            )
    else:
        print(f"{Fore.YELLOW}No hay datos disponibles en el inventario.")
    conn.close()

# Buscar
def buscar_producto():
    codigo = input("Ingrese código del producto a buscar: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
    respuesta = cursor.fetchone()
    if respuesta:
        print(
            f"{Fore.CYAN}ID: {respuesta[0]} | CODIGO: {respuesta[1]} | NOMBRE: {respuesta[2]} | DESC: {respuesta[3]} | CANTIDAD: {respuesta[4]} | PRECIO: ${respuesta[5]} | CATEGORÍA: {respuesta[6]}"
        )
    else:
        print(f"{Fore.RED}No se encontró un producto con el código especificado.")
    conn.close()

# Actualizar
def actualizar_cantidad():
    id_producto = validar_entero("Ingrese el ID del producto a actualizar: ")
    nueva_cantidad = validar_entero("Ingrese la nueva cantidad: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"{Fore.GREEN}\nLa cantidad se actualizó correctamente.\n")
    else:
        print(f"{Fore.RED}\nNo se encontró un producto con el ID especificado.\n")
    conn.close()

# Eliminar
def eliminar_producto():
    id_producto = validar_entero("Ingrese el ID del producto a eliminar: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"{Fore.GREEN}\nProducto eliminado correctamente.\n")
    else:
        print(f"{Fore.RED}\nNo se encontró un producto con el ID especificado.\n")
    conn.close()

# Reporte de bajo stock
def reporte_bajo_stock():
    limite = validar_entero("Ingrese el límite de cantidad para el reporte: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    respuesta = cursor.fetchall()
    if len(respuesta) > 0:
        print(f"{Fore.YELLOW}\nProductos con bajo stock:\n")
        for item in respuesta:
            print(
                f"{Fore.MAGENTA}ID: {item[0]} | CODIGO: {item[1]} | NOMBRE: {item[2]} | CANTIDAD: {item[4]}"
            )
    else:
        print(f"{Fore.GREEN}No hay productos con bajo stock.")
    conn.close()

# Menú principal
def mostrar_menu():
    while True:
        print(
            f"{Back.BLUE}{Fore.RED} {Style.BRIGHT}Seleccione una opción para comenzar a operar el sistema:"
        )
        print(
            Fore.GREEN
            + """

    1-Ingresar producto
    2-Mostrar productos
    3-Buscar producto
    4-Actualizar cantidad
    5-Eliminar producto
    6-Reporte bajo stock
    7-Salir
            """
        )
        opcion = input(f"{Fore.YELLOW}Opción: {Style.RESET_ALL}")

        if opcion == "1":
            insertar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(f"{Fore.CYAN}Saliendo del sistema...\n")
            break
        else:
            print(f"{Fore.RED}Opción no válida. Intente nuevamente.\n")

"""
Programa principal
"""

mostrar_menu()
