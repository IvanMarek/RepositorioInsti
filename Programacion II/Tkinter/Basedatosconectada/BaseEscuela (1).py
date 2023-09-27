import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ivan08012000@",
    database="ESCUELA",
    port=3305,
)


# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute(
        """SELECT Alumnos.IDALUMNO, Alumnos.NOMBRE, Alumnos.APELLIDO, Alumnos.DNI, Carreras.NOMBRE, estadoalumno.NOMBRE FROM Alumnos  JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN estadoalumno ON Alumnos.IDESTADOALUMNO = estadoalumno.IDESTADOALUMNO WHERE Alumnos.IDESTADOALUMNO != 1 and Alumnos.estadoACDS =1 """
    )
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)


# Función para obtener las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("SELECT IDCARRERA, NOMBRE FROM Carreras ORDER BY NOMBRE")
    carreras = cursor.fetchall()
    carrera_combobox["values"] = [row[1] for row in carreras]
    return carreras  # Devolver también la lista de carreras con sus IDs


def cargar_estado():
    cursor = conexion.cursor()
    cursor.execute("SELECT IDESTADOALUMNO, NOMBRE FROM estadoalumno ORDER BY NOMBRE")
    estado = cursor.fetchall()
    if estado != 1:
        estado_combobox["values"] = [row[1] for row in estado]

    return estado  # Devolver también la lista de estados con sus IDs


# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)


# función para validar DNI del alumno
def dniValido():
    dni = dni_entry.get()
    extraerDNI= traerDNI()
    if dni not in extraerDNI:
        dni = dni.replace(".", "")
        try:
            dni = int(dni)
            if len(str(dni)) == 8:
                return str(dni)
            else:
                messagebox.showerror("Error", "El DNI debe contener exactamente 8 números.")
        except:
            messagebox.showerror("Error", "El DNI no admite letras")
    else:
        messagebox.showerror("Error", "El DNI ya existe...")
def validarDNI2_0():
    dni = dni_entry.get()
    dni = dni.replace(".", "")
    try:
        dni = int(dni)
        if len(str(dni)) == 8:
            return str(dni)
        else:
            messagebox.showerror("Error", "El DNI debe contener exactamente 8 números.")
    except:
        messagebox.showerror("Error", "El DNI no admite letras")

def traerDNI():
    cursor = conexion.cursor()
    cursor.execute("SELECT DNI FROM ALUMNOS")
    dni = [val[0] for val in cursor.fetchall()]
    return dni

# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = dniValido()
    carrera_nombre = carrera_combobox.get()
    estado_alumno = 2  # Valor predeterminado para IDESTADOALUMNO
    estadoACTIV_INACTIV= 1 # Valor predeterminado para estadoACDS
    if nombre and apellido and dni and carrera_nombre:
        # Obtener el ID de la carrera seleccionada
        carreras = cargar_carreras()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break

        cursor = conexion.cursor()
        # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO
        cursor.execute(
            "INSERT INTO Alumnos (NOMBRE, APELLIDO, DNI, IDCARRERA, IDESTADOALUMNO, estadoACDS) VALUES (%s, %s, %s, %s, %s, %s)",
            (nombre, apellido, dni, carrera_id, estado_alumno, estadoACTIV_INACTIV),
        )
        conexion.commit()
        cargar_datos()  # Actualizar la vista
        # Limpiar los campos después de insertar
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")


def modificar_alumno():
    
    selectGrilla = tree.item(tree.selection())
    if len(selectGrilla["values"]) != 0:
        selectGrilla = selectGrilla["values"]
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
        estado_combobox.set("")  # Limpiar la selección del combobox
        idAlumno = selectGrilla[0]
        nombreAlum = selectGrilla[1]
        apellidoAlum = selectGrilla[2]
        dniAlum = selectGrilla[3]
        carreraAlum = selectGrilla[4]
        estadoAlum = selectGrilla[5]
        carrera_combobox.set(carreraAlum)
        estado_combobox.set(estadoAlum)
        nombre_entry.insert(0, nombreAlum)
        apellido_entry.insert(0, apellidoAlum)
        dni_entry.insert(0, dniAlum)

        guardar_button.config(text="GUARDAR CAMBIOS",command=lambda: guardarCambios(idAlumno))


def guardarCambios(idAlumno):
    cursor = conexion.cursor()
    nombreAlum = nombre_entry.get().upper()
    apellidoAlum = apellido_entry.get().upper()
    dniAlum = validarDNI2_0()
    carrera_nombre = carrera_combobox.get()
    estadoAlum = estado_combobox.get()

    if nombreAlum and apellidoAlum and dniAlum and carrera_nombre:
        # Obtener el ID de la carrera seleccionada
        selectGrilla=tree.item(tree.selection())
        selectGrilla=selectGrilla["values"]
        print (selectGrilla)
        carreras = cargar_carreras()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break
        estados= cargar_estado()
        estado_Id= None
        for estado in estados:
            if estado[1]== estadoAlum:
                estado_Id = estado[0]
                break

        cursor = conexion.cursor()
        cursor.execute( "UPDATE alumnos set Nombre=%s, Apellido=%s, DNI=%s, IDCARRERA=%s, IDESTADOALUMNO=%s WHERE IDALUMNO =%s",(nombreAlum, apellidoAlum, dniAlum, carrera_id, estado_Id, idAlumno),)
        conexion.commit()
        cargar_datos()
        messagebox.showinfo("Exito!","Cambios guardados con exito!")
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")
        estado_combobox.set("") 
        guardar_button.config(text="Guardar",command=guardar_alumno)
        estado_combobox.config(state="disabled")

    
def Eliminar_datos():
    selectGrilla=tree.item(tree.selection())
    selectGrilla=selectGrilla["values"]
    idAlumno = selectGrilla[0]
    cursor = conexion.cursor()
    cursor.execute("UPDATE Alumnos SET estadoACDS = 0 where IDALUMNO =%s", (idAlumno,))
    conexion.commit()
    cargar_datos()


# Crear ventana
root = tk.Tk()
root.title("Consulta de Alumnos")

# Crear un frame con un borde visible para el formulario de inscripción
formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.grid(padx=10, pady=10)

# Título del formulario
titulo_label = tk.Label(
    formulario_frame, text="Formulario Inscripción", font=("Helvetica", 14)
)
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada para nombre, apellido y DNI con el mismo ancho que el ComboBox
nombre_label = tk.Label(formulario_frame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para la carrera
carrera_label = tk.Label(formulario_frame, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame, state="readonly")  # Configurar el ComboBox como de solo lectura
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Cargar las carreras al inicio de la aplicación y obtener la lista de carreras con sus IDs
carreras = cargar_carreras()

# Combo box para el estado de alumno
estado_label = tk.Label(formulario_frame, text="Estado:")
estado_label.grid(row=5, column=0)
estado_combobox = ttk.Combobox(formulario_frame)  # Configurar el ComboBox como de solo lectura
estado_combobox.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")
estado_combobox.config(state="disable")

# cargar los estados al inicio de la aplicación y obtener una lista de estados con sus IDs
estados = cargar_estado()

# Botón para guardar un nuevo registro de alumno
guardar_button = tk.Button(formulario_frame, text="Guardar", command=guardar_alumno)
guardar_button.grid(row=6, columnspan=2, pady=10, sticky="ew")



# Botón modificar...........


# Crear Treeview para mostrar la información
tree = ttk.Treeview(
    root,
    columns=(
        "Codigo Alumno",
        "Nombre",
        "Apellido",
        "DNI",
        "Carrera",
        "Estado del alumno",
    ),
)
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Apellido")
tree.heading("#4", text="DNI")
tree.heading("#5", text="Carrera")
tree.heading("#6", text="Estado del alumno")
tree.heading("#1", text="Código Alumno")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos

tree.grid(padx=10, pady=10)

tree.column("#2", anchor=tk.CENTER)  # Centrar datos en la columna 'Nombre'
tree.column("#3", anchor=tk.CENTER)  # Centrar datos en la columna 'Apellido'
tree.column("#4", anchor=tk.CENTER)  # Centrar datos en la columna 'DNI'
tree.column("#5", anchor=tk.CENTER)  # Centrar datos en la columna 'Carrera'
tree.column("#6", anchor=tk.CENTER)  # Centrar datos en la columna 'Estado De alumno'
tree.column("#1", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.grid(padx=10, pady=10)


# Botón para cargar datos
cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.grid(pady=5, row=7)

# Botón para modificar un alumno
modificar_button = tk.Button(root, text="Modificar datos", command = lambda: [modificar_alumno(), estado_combobox.config(state="readonly")])
modificar_button.grid(pady=5, padx=(350, 0), row=7, sticky="W")

# Botón para ELIMINAR un alumno

eliminar_button= tk.Button(root, text="Eliminar datos", command= lambda: Eliminar_datos())
eliminar_button.grid(pady=5, padx=(0,350), row=7, sticky="E")


# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()

