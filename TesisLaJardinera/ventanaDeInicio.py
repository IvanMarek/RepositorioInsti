from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from funcionesTesis import *


def on_resize(event):
    # Adjust column and row weights to make the widgets responsive
    ventanaInicio.columnconfigure(0, weight=1)
    ventanaInicio.rowconfigure(0, weight=1)

ventanaInicio = Tk()


ancho_pantalla = int(ventanaInicio.winfo_screenwidth())
alto_pantalla = int(ventanaInicio.winfo_screenheight())

ventanaInicio.bind("<Configure>", on_resize)
ventanaInicio.geometry(f"{ancho_pantalla}x{alto_pantalla}")
"""ventanaInicio.config(bg="#010101")"""
ventanaInicio.title('La Jardinera')
"""ventanaInicio.resizable(height=False, width=False)"""


menu = ttk.Label(ventanaInicio, text='Inicio')
menu.pack(pady=50)

boton_consultar_producto = ttk.Button(ventanaInicio, text= 'Consultar productos', width=25, command= lambda: consultar_producto(ventanaInicio))
boton_consultar_producto.pack(pady=30, ipady= 5)

boton_consultar_proveedor = ttk.Button(ventanaInicio, text= 'Consultar proveedor', width=25)
boton_consultar_proveedor.pack(pady=30,ipady= 5)

boton_consultar_informes = ttk.Button(ventanaInicio, text= 'Consultar informes', width=25)
boton_consultar_informes.pack(pady=30, ipady= 5)




ventanaInicio.mainloop()