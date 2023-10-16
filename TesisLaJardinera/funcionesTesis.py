from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
import os


base_datos = sqlite3.connect('LaJardinera.bd')
cursor = base_datos.cursor()

cursor.execute('SELECT * FROM producto')
product = cursor.fetchall()
print(product)



def consultar_producto(a):
    ventana_consultar_producto = Toplevel(a)
    ventana_consultar_producto.title('Consultar productos')

    tipo_filtro = Label(ventana_consultar_producto, text= 'Filtro')
    tipo_filtro.grid(row=0, column=0, pady=(25,20), padx=(55,0), sticky=W)
    """Completar tema flitro"""


    buscar_nombre = Label(ventana_consultar_producto, text= "Buscar por nombre: ")
    buscar_nombre.grid(row=1, column=0, padx=(55,0),sticky=W)
    busqueda = Entry (ventana_consultar_producto)
    busqueda.grid(row=1, column=1, sticky="nsew") 


    ventana_consultar_producto = ttk.Treeview( ventana_consultar_producto, columns=("Clave primaria" ,"Código producto", "Imagen" ,"Nombre", "Cantidad", "Precio por metro"),)
    
    ventana_consultar_producto.heading("#2", text="Código producto")
    ventana_consultar_producto.heading("#3", text="")
    ventana_consultar_producto.heading("#4", text="Nombre")
    ventana_consultar_producto.heading("#5", text="Cantidad")
    ventana_consultar_producto.heading("#6", text="Precio por metro")
    ventana_consultar_producto.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos

    ventana_consultar_producto.grid(column=0, columnspan=12, padx=10, pady=20)

    ventana_consultar_producto.column("#2", anchor=tk.CENTER)  
    ventana_consultar_producto.column("#3", anchor=tk.CENTER) 
    ventana_consultar_producto.column("#4", anchor=tk.CENTER)  
    ventana_consultar_producto.column("#5", anchor=tk.CENTER) 
    ventana_consultar_producto.column("#6", anchor=tk.CENTER) 
    ventana_consultar_producto.column("#1", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
    ventana_consultar_producto.grid(padx=10, pady=10)


"""    nuevo_button = tk.Button(ventana_consultar_producto, text="Nuevo",)
    nuevo_button.grid(pady=15, row=10)

    editar_button = tk.Button(ventana_consultar_producto, text="Editar")
    editar_button.grid(pady=15, padx=(350, 0), row=10, sticky="W")


    eliminar_button= tk.Button(ventana_consultar_producto, text="Eliminar")
    eliminar_button.grid(pady=15, padx=(0,350), row=10, sticky="E")
"""

