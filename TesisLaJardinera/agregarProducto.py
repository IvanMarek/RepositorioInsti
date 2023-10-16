from tkinter import *
import sqlite3
from tkinter import filedialog
from tkinter import messagebox
import os

base_datos = sqlite3.connect('LaJardinera.bd')
cursor = base_datos.cursor()

cursor.execute('SELECT * FROM producto')
product = cursor.fetchall()
print(product)

def seleccionar_imagen():
    global imagen_bytes, proveedor_opciones, categoria_opciones
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        nombre_archivo = os.path.basename(ruta_imagen)
        nombre_archivo_var = nombre_archivo
        with open(ruta_imagen, 'rb') as archivo_imagen:
            imagen_bytes = archivo_imagen.read()

    nombre_imagen_label.config(text = nombre_archivo_var)

def guardar_producto():
    nombre = producto_nombre_entry.get()
    precio = producto_precio_entry.get()
    cantidad = producto_cantidad_entry.get()
    proveedor = proveedor_seleccionada.get()
    categoria = categoria_seleccionada.get()
    imagen = imagen_bytes
    
    cursor.execute('SELECT id_proveedor FROM proveedor WHERE razon_social = ?', (proveedor, ))
    id_proveedor = cursor.fetchone()

    cursor.execute('SELECT id_categoria FROM categoria WHERE nombre = ?', (categoria, ))
    id_categoria = cursor.fetchone()

    cursor.execute('INSERT INTO producto (nombre, precio, cantidad, id_proveedor, id_categoria, imagen) VALUES (?,?,?,?,?,?)',
                   (nombre, precio, cantidad, id_proveedor[0], id_categoria[0], imagen))
    base_datos.commit()

    messagebox.showinfo('Completado','El producto ha sido guardado con éxito.')

    cursor.execute('SELECT * FROM producto')
    product = cursor.fetchall()
    print(product)
    producto_nombre_entry.delete(0, 'end')
    producto_precio_entry.delete(0, 'end')
    producto_cantidad_entry.delete(0, 'end')
    proveedor_seleccionada.set('Seleccionar Proveedor')
    categoria_seleccionada.set('Seleccionar Categoria')
    nombre_imagen_label.config(text='')

def agregar_proveedor(a):
    ventana_agregar_proveedor = Toplevel(a)
    ventana_agregar_proveedor.title('Agregar Proveedor')

    agregar_proveedor_label = Label(ventana_agregar_proveedor, text='Agregar Proveedor')
    agregar_proveedor_label.grid(row=0, column=0, columnspan=2)

    proveedor_razon_social_label = Label(ventana_agregar_proveedor, text='Razon Social: ')
    proveedor_razon_social_label.grid(row=1, column=0)

    proveedor_razon_social_entry = Entry(ventana_agregar_proveedor)
    proveedor_razon_social_entry.grid(row=1, column=1)

    proveedor_cuit_label = Label(ventana_agregar_proveedor, text='CUIT: ')
    proveedor_cuit_label.grid(row=2, column=0)

    proveedor_cuit_entry = Entry(ventana_agregar_proveedor)
    proveedor_cuit_entry.grid(row=2, column=1)

    proveedor_domicilio_label = Label(ventana_agregar_proveedor, text='Domicilio: ')
    proveedor_domicilio_label.grid(row=3, column=0)

    proveedor_domicilio_entry = Entry(ventana_agregar_proveedor)
    proveedor_domicilio_entry.grid(row=3, column=1)

    proveedor_telefono_label = Label(ventana_agregar_proveedor, text='Telefono: ')
    proveedor_telefono_label.grid(row=4, column=0)

    proveedor_telefono_entry = Entry(ventana_agregar_proveedor)
    proveedor_telefono_entry.grid(row=4, column=1)

    proveedor_email_label = Label(ventana_agregar_proveedor, text='Email: ')
    proveedor_email_label.grid(row=5, column=0)

    proveedor_email_entry = Entry(ventana_agregar_proveedor)
    proveedor_email_entry.grid(row=5, column=1)

    def guardar_proveedor():
        razon_social = proveedor_razon_social_entry.get()
        cuit = proveedor_cuit_entry.get()
        domicilio = proveedor_domicilio_entry.get()
        numeroTelefono = proveedor_telefono_entry.get()
        email = proveedor_email_entry.get()

        cursor.execute('INSERT INTO proveedor (razon_social, cuit, domicilio, numero_telefono, email) VALUES (?,?,?,?,?)',
               (razon_social, cuit, domicilio, numeroTelefono, email))
        base_datos.commit()
        
        messagebox.showinfo('Completado','El proveedor ha sido guardado con éxito.')
        ventana_agregar_proveedor.destroy()

    boton_guardar_proveedor = Button(ventana_agregar_proveedor, text='Guardar', command=guardar_proveedor)
    boton_guardar_proveedor.grid(row=6, column=0, columnspan=2)

def consultar_proveedores():
    cursor.execute("SELECT razon_social FROM proveedor")
    proveedores = cursor.fetchall()
    base_datos.commit()
    print(proveedores)
    return ['Seleccionar Proveedor'] + [nombre[0] for nombre in proveedores]

def agregar_categoria(a):
    ventana_agregar_categoria = Toplevel(a)
    ventana_agregar_categoria.title('Agregar Categoria')

    agregar_categoria_label = Label(ventana_agregar_categoria, text='Agregar Categoria')
    agregar_categoria_label.grid(row=0, column=0, columnspan=2)

    categoria_nombre_label = Label(ventana_agregar_categoria, text='Nombre: ')
    categoria_nombre_label.grid(row=1, column=0)

    categoria_nombre_entry = Entry(ventana_agregar_categoria)
    categoria_nombre_entry.grid(row=1, column=1)

    def guardar_categoria():
        nombre = categoria_nombre_entry.get()

        cursor.execute('INSERT INTO categoria (nombre) VALUES (?)',
               (nombre,))
        base_datos.commit()
        
        messagebox.showinfo('Completado','La categoria ha sido guardada con éxito.')
        ventana_agregar_categoria.destroy()

    boton_guardar_proveedor = Button(ventana_agregar_categoria, text='Guardar', command=guardar_categoria)
    boton_guardar_proveedor.grid(row=6, column=0, columnspan=2)

def consultar_categorias():
    cursor.execute("SELECT nombre FROM categoria")
    categoria = cursor.fetchall()
    base_datos.commit()
    return ['Seleccionar Categoria'] + [nombre[0] for nombre in categoria]

ventana_agregar_producto = Tk()

ventana_agregar_producto.title('Agregar Producto')
ventana_agregar_producto.resizable(height=False, width=False)

agregar_producto_titulo = Label(ventana_agregar_producto, text='Agregar Productos')
agregar_producto_titulo.grid(row=0, column=0, columnspan=3)

producto_nombre_label = Label(ventana_agregar_producto, text='Nombre: ')
producto_nombre_label.grid(row=1, column=0)

producto_nombre_entry= Entry(ventana_agregar_producto)
producto_nombre_entry.grid(row=1, column=1)

producto_precio_label = Label(ventana_agregar_producto, text='Precio: ')
producto_precio_label.grid(row=2, column=0)

producto_precio_entry = Entry(ventana_agregar_producto)
producto_precio_entry.grid(row=2, column=1)

producto_cantidad_label = Label(ventana_agregar_producto, text='Cantidad: ')
producto_cantidad_label.grid(row=3, column=0)

producto_cantidad_entry = Entry(ventana_agregar_producto)
producto_cantidad_entry.grid(row=3, column=1)

producto_proveedor_label = Label(ventana_agregar_producto, text='Proveedor: ')
producto_proveedor_label.grid(row=4, column=0)

proveedor_opciones = consultar_proveedores()
proveedor_seleccionada = StringVar()
proveedor_seleccionada.set(proveedor_opciones[0])

producto_proveedor_opciones = OptionMenu(ventana_agregar_producto, proveedor_seleccionada, *proveedor_opciones )
producto_proveedor_opciones.grid(row=4, column=1)

boton_agregar_proveedor = Button(ventana_agregar_producto, text='+', command=lambda:agregar_proveedor(ventana_agregar_producto))
boton_agregar_proveedor.grid(row=4, column=2)

producto_categoria_label = Label(ventana_agregar_producto, text='Categoria: ')
producto_categoria_label.grid(row=5, column=0)

categoria_opciones = consultar_categorias()
categoria_seleccionada = StringVar()
categoria_seleccionada.set(categoria_opciones[0])

producto_categoria_opciones = OptionMenu(ventana_agregar_producto, categoria_seleccionada, *categoria_opciones)
producto_categoria_opciones.grid(row=5, column=1)

boton_agregar_categoria = Button(ventana_agregar_producto, text='+', command=lambda:agregar_categoria(ventana_agregar_producto))
boton_agregar_categoria.grid(row=5, column=2)

boton_agregar_imagen = Button(ventana_agregar_producto, text='Agregar Imagen', command=seleccionar_imagen)
boton_agregar_imagen.grid(row=6, column=0, columnspan=3)

nombre_imagen_label = Label(ventana_agregar_producto, text='')
nombre_imagen_label.grid(row=7, column=0, columnspan=3)

boton_agregar_producto = Button(ventana_agregar_producto, text='Agregar Prodcuto', command=guardar_producto)
boton_agregar_producto.grid(row=8, column=0, columnspan=3)

ventana_agregar_producto.mainloop()




