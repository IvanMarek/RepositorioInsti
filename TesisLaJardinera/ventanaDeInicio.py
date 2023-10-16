from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
from funcionesTesis import *


ventanaInicio = Tk()

ventanaInicio.geometry("800x600")
ventanaInicio.config(bg="#A8C0C2")
ventanaInicio.title('La Jardinera')
ventanaInicio.resizable(height=False, width=False)

menu = Label(ventanaInicio, text='Inicio')
menu.grid(row=0, column=0, columnspan=5, pady= 30, padx=400)

boton_consultar_producto = Button(ventanaInicio, text= 'Consultar productos', width=25, height=2, command= lambda: consultar_producto(ventanaInicio))
boton_consultar_producto.grid(row=2, column=2, pady= (100,40),sticky="nsew")

boton_consultar_proveedor = Button(ventanaInicio, text= 'Consultar proveedor', width=25, height=2)
boton_consultar_proveedor.grid(row=3, column=2,sticky="nsew")

boton_consultar_informes = Button(ventanaInicio, text= 'Consultar informes', width=25, height=2)
boton_consultar_informes.grid(row=4, column=2, pady= (40,100),sticky="nsew")




ventanaInicio.mainloop()