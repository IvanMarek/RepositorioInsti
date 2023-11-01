import tkinter as tk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
import time

conexion = mysql.connector.connect(host="localhost", user="root", password="estudiantes2020", database="JUEGO", port=3305)

cursor = conexion.cursor()
pregunta_actual = 0

global puntuacion
puntuacion = 0


root = None
ventana = None

global inicio
global jugadores_data
jugadores_data = []


def crear_ventana():

    def iniciar_juego():

        global jugadores_data

        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        telefono = telefono_entry.get()

        # Verificar si todos los campos están llenos
        if nombre and apellido and telefono:
            jugadores_data= [nombre, apellido, telefono]
            print(jugadores_data)
            ventana.destroy()
            global inicio
            inicio=time.time()
            abrir_juego()
            
        else:
            messagebox.showerror("Error", "Los campos son obligatorios. Debes completarlos.")

    def salir_pantalla_princial():
        ventana.destroy()
        root.destroy()

    ventana = tk.Tk()
    ventana.title("Jugadores")
    ventana.attributes('-fullscreen', True)
    ventana.configure(bg="#630551")

    # Crear un frame con un borde visible para el formulario de inscripción
    formulario_frame = tk.Frame(ventana, bd=2, relief=tk.SOLID, bg="#F3C7AA")
    formulario_frame.grid(padx=10, pady=10)

    # Título del formulario
    titulo_label = tk.Label(formulario_frame, text="Jugador", bg="#F3C7AA", font=("Arial", 20, 'bold'))
    titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Campos de entrada para nombre, apellido y teléfono con el mismo ancho que el ComboBox
    nombre_label = tk.Label(formulario_frame, text="Nombre:", bg="#F3C7AA", font=("Arial", 15))
    nombre_label.grid(row=1, column=0)
    nombre_entry = tk.Entry(formulario_frame)
    nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

    apellido_label = tk.Label(formulario_frame, text="Apellido:", bg="#F3C7AA", font=("Arial", 15))
    apellido_label.grid(row=2, column=0)
    apellido_entry = tk.Entry(formulario_frame)
    apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

    telefono_label = tk.Label(formulario_frame, text="Teléfono:", bg="#F3C7AA", font=("Arial", 15))
    telefono_label.grid(row=3, column=0)
    telefono_entry = tk.Entry(formulario_frame)
    telefono_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

    jugar_button = tk.Button(formulario_frame, text="JUGAR", bg="#9E5B00", font=("Arial", 8, 'bold'), command=lambda:iniciar_juego())
    jugar_button.grid(row=6, columnspan=2, pady=1, sticky="ew")

    jugar_button = tk.Button(formulario_frame, text="SALIR", bg="#9E5B00", font=("Arial", 8, 'bold'), command=lambda:salir_pantalla_princial())
    jugar_button.grid(row=7, columnspan=3, pady=5, sticky="ew")

    titulo2_label = tk.Label(ventana, text="Tabla de Jugadores", font=("Arial", 35, 'bold'), bg="#630551", fg="white")
    titulo2_label.grid(row=4, column=0, columnspan=5, padx=250, pady=15)

    # Crear Treeview para mostrar la información
    tree = ttk.Treeview(ventana, columns=("idjugador", "Nombre", "Apellido", "telefono", "Puntaje", "Tiempo"))
    tree.heading("#2", text="Nombre")
    tree.heading("#3", text="Apellido")
    tree.heading("#4", text="Teléfono")
    tree.heading("#5", text="Puntaje")
    tree.heading("#6", text="Tiempo")
    tree.heading("#1", text="idjugador")
    tree.column("#1", width=0, stretch=tk.NO)
    tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
    tree.column("#2", width=230)  # Aumenta el ancho del Treeview
    tree.config(height=23)  # Aumentar la altura del Treeview
    tree.grid(row=5, column=0, padx=250, pady=0)


    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor.execute("select codjugador, nombre, apellido, telefono, puntaje, tiempo from jugador order by puntaje DESC")
    for row in cursor.fetchall():
        print(row)
        tree.insert("", "end", values=row)


crear_ventana()

root = tk.Tk()
root.title("Juego de Preguntas y Respuestas")
root.attributes("-fullscreen", True)
root.configure(bg="#630551")

label_pregunta = tk.Label(root, text="", font=("Helvetica", 20, 'bold'), bg="#630551", fg="white")
label_pregunta.pack(pady=90)

frame_respuestas = tk.Frame(root, bg="#630551")
frame_respuestas.pack()
botones_respuesta = []

def abrir_juego():
    

    def obtener_preguntas():
        cursor.execute("SELECT preguntas, respuestas, respuestaErronea_uno, respuestaErronea_dos, respuestaErronea_tres FROM Preguntas")
        preguntas_respuestas = cursor.fetchall()
        random.shuffle(preguntas_respuestas)  # Mezclar las preguntas para que aparezcan en orden aleatorio
        return preguntas_respuestas

    preguntas_respuestas = obtener_preguntas()

    def mostrar_pregunta():
        global pregunta_actual
        if pregunta_actual < len(preguntas_respuestas):
            pregunta, respuesta_correcta, respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3 = preguntas_respuestas[pregunta_actual]
            label_pregunta.config(text=pregunta)
            opciones = [respuesta_correcta, respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3]
            random.shuffle(opciones)  # Mezclar las opciones de respuesta
            for i, opcion in enumerate(opciones):
                botones_respuesta[i].config(text=opcion)
        else:
            label_pregunta.config(text="Fin del juego. Puntuación: " + str(puntuacion))
            for boton in botones_respuesta:
                boton.config(state=tk.DISABLED)

    def verificar_respuesta(opcion):
        global pregunta_actual
        global puntuacion
        global jugadores_data

        pregunta, respuesta_correcta, _, _, _ = preguntas_respuestas[pregunta_actual]
        if opcion == respuesta_correcta:
            puntuacion += 100
            mensaje = "¡Correcto!"
        else:
            mensaje = f"Incorrecto. La respuesta correcta es: {respuesta_correcta}"

        pregunta_actual += 1
        mostrar_pregunta()
        if pregunta_actual < len(preguntas_respuestas):
            messagebox.showinfo("Resultado", mensaje)
        else:
            

            global puntuacion_total
            global tiempo_total_bd
            puntuacion_total = puntuacion
            print(jugadores_data)
            tiempo_transcurrido=(time.time()-inicio) * 1000
            print('Tiempo transcurrido:', tiempo_transcurrido)
            minutos, segundos= divmod(tiempo_transcurrido/1000,60)
            segundos, milisegundos = divmod(segundos,1)
            print(f"tiempo transcurrido: {int(minutos)}, {int(segundos)}, {int(milisegundos)}")
            tiempo_total=(f"tiempo transcurrido: {int(minutos)}:{int(segundos)}")
            tiempo_total_bd = (f"{int(minutos)}:{int(segundos)}")

            messagebox.showinfo("Fin del juego", "¡Juego terminado! Tu puntuación: " + str(puntuacion_total)+ "\n tu tiempo fue:" + tiempo_total)
            

            
            
    for i in range(4):
        frame_grupo = tk.Frame(frame_respuestas, bg="#630551")
        frame_grupo.pack(pady=30)
        boton = tk.Button(frame_grupo, text="", font=("Helvetica", 17), command=lambda i=i: verificar_respuesta(botones_respuesta[i]['text']))
        boton.pack(pady=10)

        botones_respuesta.append(boton)
    mostrar_pregunta()
    button_salir = tk.Button(root, text="SALIR",  font=("Helvetica", 20), bg="red", fg="white", command=lambda: cerrar_juego(frame_grupo))
    button_salir.pack(pady=12)

   #quiero una funcion que me permita apretar el boton salir de la ventana root y se vuelva a la ventana principal

    

def cerrar_juego(ventana):
    cursor.execute("INSERT INTO JUGADOR (NOMBRE, APELLIDO, TELEFONO, PUNTAJE, TIEMPO) values (%s,%s,%s,%s,%s)", (jugadores_data[0], jugadores_data[1], jugadores_data[2], puntuacion_total, tiempo_total_bd))
    conexion.commit()
    ventana.destroy()
    crear_ventana()
root.mainloop()




