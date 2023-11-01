import tkinter as tk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
import time

conexion = mysql.connector.connect(host="localhost", user="root", password="Ivan08012000@", database="JUEGO2", port=3305)

cursor = conexion.cursor()
pregunta_actual = 0

global puntuacion
puntuacion = 0


root = None
ventana = None

global inicio
global jugadores_data
jugadores_data = []
global nombre_entry
global apellido_entry
global telefono_entry
preguntas_respondidas = []
global contador_correctas
contador_correctas = 0
global contador_incorrectas
conrador_incorrectas = 0



def iniciar_juego(ventana):
    global jugadores_data
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    telefono = telefono_entry.get()

    # Verificar si todos los campos están llenos
    if nombre and apellido and telefono:
        jugadores_data= [nombre, apellido, telefono]
        print(jugadores_data)
        global inicio
        inicio=time.time()
        abrir_juego()
        
    else:
        messagebox.showerror("Error", "Los campos son obligatorios. Debes completarlos.")

def salir_pantalla_princial(ventana, root):
    ventana.destroy()


def crear_ventana():
    global nombre_entry 
    global apellido_entry
    global telefono_entry


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

    jugar_button = tk.Button(formulario_frame, text="JUGAR", bg="#9E5B00", font=("Arial", 8, 'bold'), command=lambda:iniciar_juego(ventana))
    jugar_button.grid(row=6, columnspan=2, pady=1, sticky="ew")

    jugar_button = tk.Button(formulario_frame, text="SALIR", bg="#9E5B00", font=("Arial", 8, 'bold'), command=lambda:salir_pantalla_princial(ventana))
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

    ventana.mainloop()



###################################################
##### IMPRIME LOS LABELS Y BOTONES. VERIFICA ######
###################################################


def mostrar_pregunta(label_pregunta,botones_respuestas, root, preguntas_frame):
        pregunta = obtener_pregunta_aleatoria()
        if pregunta:
            label_pregunta.configure(
                text=pregunta[1]
            )  # pregunta[1] contiene el texto de la pregunta
            respuestas = [pregunta[2], pregunta[3], pregunta[4], pregunta[5]]
            random.shuffle(respuestas)

            respuesta_real = pregunta[2]

            for i in range(4):
                botones_respuestas[i].configure(
                    text=respuestas[i],                 ## RESPUESTA CORRECTA ##
                    command=lambda i=i: verificar_respuesta(respuesta_real, respuestas[i],label_pregunta,botones_respuestas, root, preguntas_frame),
                )
        else:
            label_pregunta.configure(text="¡Has respondido todas las preguntas!")

            tiempo_transcurrido = (time.time() - inicio) * 1000
            minutos, segundos = divmod(tiempo_transcurrido / 1000, 60)
            segundos, milisegundos = divmod(segundos, 1)
            global tiempo_total
            tiempo_total = f"{int(minutos)} m : {int(segundos)} s : {int(milisegundos)*1000} ms"
           

            lista_jugador.append(tiempo_total)
 


            for boton in botones_respuestas:
                boton.configure(state="disabled")
            
            fin_Juego(root, preguntas_frame)



###################################################
###################################################
###################################################



def obtener_pregunta_aleatoria():
    
    cursor.execute(
        "SELECT codpreguntas, preguntas, respuestas, respuestaErronea_uno , respuestaErronea_dos , respuestaErronea_tres  FROM preguntas"
    )
    preguntas = cursor.fetchall()

    preguntas_no_respondidas = [
        pregunta for pregunta in preguntas if pregunta not in preguntas_respondidas
    ]

    if not preguntas_no_respondidas:
        return None

    pregunta = random.choice(preguntas_no_respondidas)
    preguntas_respondidas.append(pregunta)
    return pregunta



###################################################
######### VERIFICA SI ESTA CORRECTA O NO ##########
###################################################


                    ## RESPUESTA ## RESPUESTA_INDICE 
def verificar_respuesta(respuesta_real, respuesta,resultado_label,label_correctas,label_incorrectas,label_pregunta,botones_respuestas,  root, preguntas_frame):
    global contador_correctas, contador_incorrectas

    if respuesta == respuesta_real:  # pregunta[2] contiene la respuesta correcta
        resultado_label.configure(text="¡Correcto!")
        contador_correctas += 1
        """label_correctas.configure(
            text=f"Respuestas Correctas: {contador_correctas}"
        )"""
        
    else:
        resultado_label.configure(text="Incorrecto")
        contador_incorrectas += 1
        label_incorrectas.configure(
            text=f"Respuestas Incorrectas: {contador_incorrectas}"
        )
    mostrar_pregunta(label_pregunta,botones_respuestas,resultado_label,label_correctas,label_incorrectas, root, preguntas_frame)







def abrir_juego():
    root = tk.Toplevel()
    root.title("Juego de Preguntas y Respuestas")
    root.attributes("-fullscreen", True)
    root.configure(bg="#630551")

    label_pregunta = tk.Label(root, text="", font=("Helvetica", 20, 'bold'), bg="#630551", fg="white")
    label_pregunta.pack(pady=90)

    frame_respuestas = tk.Frame(root, bg="#630551")
    frame_respuestas.pack()
    botones_respuesta = []
    for i in range(4):
        frame_grupo = tk.Frame(frame_respuestas, bg="#630551")
        frame_grupo.pack(pady=30)
    boton = tk.Button(frame_grupo, text="", font=("Helvetica", 17), command=lambda i=i: verificar_respuesta(botones_respuesta[i]['text']))
    boton.pack(pady=10)

    botones_respuesta.append(boton)
    mostrar_pregunta(label_pregunta)
    button_salir = tk.Button(root, text="SALIR",  font=("Helvetica", 20), bg="red", fg="white", command=lambda: cerrar_juego(frame_grupo))
    button_salir.pack(pady=12)
    root.mainloop()

    

    

   

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
            

            
            


   #quiero una funcion que me permita apretar el boton salir de la ventana root y se vuelva a la ventana principal

    

def cerrar_juego(ventana):
    cursor.execute("INSERT INTO JUGADOR (NOMBRE, APELLIDO, TELEFONO, PUNTAJE, TIEMPO) values (%s,%s,%s,%s,%s)", (jugadores_data[0], jugadores_data[1], jugadores_data[2], puntuacion_total, tiempo_total_bd))
    conexion.commit()
    ventana.destroy()
    crear_ventana()





