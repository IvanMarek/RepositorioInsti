import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(host="localhost",user="root",password="",database="almacen")

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children()) # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    consulta_sql = """
        SELECT producto.Nombre, producto.precio, producto.stock, marca.Nombre, categoria.Nombre
        FROM producto
        INNER JOIN marca ON producto.CodMarca = marca.CodMarca
        INNER JOIN categoria ON producto.CodCategoria = categoria.CodCategoria
    """
    cursor.execute(consulta_sql)
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Crear ventana
root = tk.Tk()
root.title("Consultar productos")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("Nombre", "Precio", "stock",  "Marca", "Categoria"))
tree.heading("#1", text="Nombre", anchor=tk.CENTER)  # Centrar el encabezado 'Nombre'
tree.heading("#2", text="Precio", anchor=tk.CENTER)  # Centrar el encabezado 'Precio'
tree.heading("#3", text="Stock", anchor=tk.CENTER)   # centrar el encabezado 'stock'
tree.heading("#4", text="Marca", anchor=tk.CENTER)   # Centrar el encabezado 'Marca'
tree.heading("#5", text="Categoria", anchor=tk.CENTER)  # Centrar el encabezado 'Categoria'
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.pack(padx=10, pady=10)

tree.column("#1", anchor=tk.CENTER)  # Centrar datos en la columna 'Nombre'
tree.column("#2", anchor=tk.CENTER)  # Centrar datos en la columna 'Precio'
tree.column("#3", anchor=tk.CENTER)  # Centrar datos en la columna 'stock'
tree.column("#4", anchor=tk.CENTER)  # Centrar datos en la columna 'Marca'
tree.column("#5", anchor=tk.CENTER)  # Centrar datos en la columna 'Categoria'
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.pack(padx=10, pady=10)

# Botón para cargar datos
cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()

