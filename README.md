# TalentoTechPythonProyectoIntegrado
Esta es una aplicación de línea de comandos desarrollada en Python para gestionar el inventario de una pequeña tienda


# Descipcion
Proyecto Final de Inventario - Tienda


1. **Registrar productos**: Agregar nuevos productos al inventario especificando su código, nombre, descripción, categoría, cantidad y precio.
2. **Mostrar productos**: Listar todos los productos almacenados en la base de datos, mostrando su ID, código, nombre, descripción, cantidad, precio y categoría.
3. **Buscar productos**: Buscar productos específicos por su código y mostrar sus datos.
4. **Actualizar cantidad**: Modificar la cantidad disponible de un producto utilizando su ID.
5. **Eliminar productos**: Eliminar un producto del inventario utilizando su ID.
6. **Generar reporte de bajo stock**: Listar productos cuya cantidad es igual o inferior a un límite especificado.

El programa utiliza una base de datos SQLite (`inventario.db`) para almacenar los datos de los productos y la librería `colorama` para mejorar la experiencia visual en la terminal.

---

## Requisitos
1. Python 3.7 o superior.
2. Biblioteca `colorama` instalada.
3. Sistema operativo compatible con SQLite (Windows, Linux, macOS).

---

## Instalación
1. Clonar o descargar el repositorio con el código fuente del proyecto.
2. Abrir una terminal y navegar hasta el directorio donde se encuentra el archivo `inventario_gestion.py`.


```bash
python -m venv venv
source venv/bin/activate # En Linux/macOS
venv\Scripts\activate   # En Windows
```

4. Instalar las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

---

## Uso del programa
1. Ejecutar el archivo principal desde la terminal:

```bash
python inventario_gestion.py
```

2. Se mostrará un menú principal con opciones:

```
1-Ingresar producto
2-Mostrar productos
3-Buscar producto
4-Actualizar cantidad
5-Eliminar producto
6-Reporte bajo stock
7-Salir
```

3. Ingresar la opción deseada y seguir las instrucciones en pantalla.

4. Para salir del programa, elegir la opción 7.

---

## Alcance
- **Gestión de inventario**: Permite registrar, actualizar, eliminar y consultar productos de manera eficiente.
- **Bajo stock**: Identifica productos que necesitan reposición.
- **Validación de entradas**: Asegura que los datos ingresados sean correctos, mejorando la integridad de la base de datos.

---

## Notas importantes
- La base de datos SQLite (`inventario.db`) se genera automáticamente al ejecutar el programa por primera vez.
- Se recomienda realizar pruebas iniciales para familiarizarse con el flujo del programa.

---

¡Gracias por usar este programa! 
