import tkinter
from tkinter import *
import customtkinter as ctk
from tkinter import ttk as ttk
import mysql.connector
import random
import time
from tkinter import messagebox

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ivan08012000@",
    database="juego",
    port=3305,
)
cursor = conexion.cursor()

lista_jugador = []

preguntas_respondidas = []
contador_correctas = 0
contador_incorrectas = 0

global tiempo_total
global inicio

global jugadores_treeview
global tel_entry

def actualizar_tree(jugadores_treeview):
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=30)
        fuente = ("Impact", 16)

        jugadores_treeview.delete(*jugadores_treeview.get_children())
        cursor.execute("""SELECT nombre, telefono, instagram, puntaje, tiempo FROM Jugador ORDER BY puntaje DESC;""")

        jugadores = cursor.fetchall()

        for resultado in jugadores:

            jugadores_treeview.insert("", "end", values=resultado)
            jugadores_treeview.tag_configure("fuente_personalizada", font=fuente)

def validarTel():
    global tel_entry
    telefono = tel_entry.get()
    try:
        telefono = int(telefono)
        if len(str(telefono)) == 10:
            return str(telefono)
        else:
            messagebox.showerror("Error", "El número de teléfono esta incompleto.")
    except:
        messagebox.showerror("Error", "El número de teléfono no admite letras")



def ventana_Inicio():

    ventana = ctk.CTk()
    ventana.title("40 'ISAUI' ")
    ventana.attributes('-fullscreen', True)
    
    global tel_entry

    isaui_label = ctk.CTkLabel(
        ventana,
        text="Trivia 40 Años Isaui",
        font=("Impact", 35),
    )
    isaui_label.pack(pady=(25, 0), padx=(105, 0))
    """isaui_label.pack()"""

    formulario_frame = ctk.CTkFrame(ventana)
    formulario_frame.pack(side="left", padx=(10, 0))

    participante_label = ctk.CTkLabel(
        formulario_frame, text="Ingrese sus datos", font=("Impact", 20)
    )
    participante_label.grid(row=1, column=0, padx=20, pady=15)

    nombre_label = ctk.CTkLabel(formulario_frame, text="Nombre", font=("Impact", 20))
    nombre_label.grid(row=2, column=0, padx=(10, 5))
    nombre_entry = ctk.CTkEntry(formulario_frame, border_width=3, width=155)
    nombre_entry.grid(row=2, column=2, pady=5, columnspan=2, padx=(0, 15))
    # nombre_entry.insert(0, "Ingrese su nombre")
    nombre_entry.bind("<Button-1>", lambda x: nombre_entry.delete(0, ctk.END))

    tel_label = ctk.CTkLabel(formulario_frame, text="Teléfono", font=("Impact", 20))
    tel_label.grid(row=4, column=0, padx=(10, 5))
    tel_entry = ctk.CTkEntry(formulario_frame, border_width=3, width=155)
    tel_entry.grid(row=4, column=2, pady=5, columnspan=2, padx=(0, 15))
    # tel_entry.insert(0, "Ingrese número")
    tel_entry.bind("<Button-1>", lambda x: tel_entry.delete(0, ctk.END))

    instagram_label = ctk.CTkLabel(formulario_frame, text="Instagram", font=("Impact", 20))
    instagram_label.grid(row=5, column=0, padx=(10, 5))
    instagram_entry = ctk.CTkEntry(formulario_frame, border_width=3, width=155)
    instagram_entry.grid(row=5, column=2, pady=5, columnspan=2, padx=(0, 15))
    # instagram_entry.insert(0, "Ingrese su Instagram")
    instagram_entry.bind("<Button-1>", lambda x: instagram_entry.delete(0, ctk.END))

    boton_jugarr = ctk.CTkButton(
        formulario_frame,
        text=" Comenzar a jugar ",
        font=("Impact", 20),
        command=lambda: registar_jugador(  nombre_entry.get().upper()  ,   tel_entry.get()    ,  instagram_entry.get()  ),
    )
    boton_jugarr.grid(row=6, column=2, pady=(25, 10), padx=(0, 15))

    frame2 = ctk.CTkFrame(ventana)
    frame2.pack(side="right", padx=(10, 10))

    tituloJugadores_label = ctk.CTkLabel(
        frame2, text="Tabla de jugadores", font=("Impact", 20)
    )
    tituloJugadores_label.grid(row=2, column=4)

    

    global jugadores_treeview

    

    jugadores_treeview = ttk.Treeview(
        frame2, columns=("Id","Nombre", "Teléfono", "Instagram" "Puntaje", "Tiempo",), style="Treeview"
    )
    jugadores_treeview.column("#0", width=0, stretch=NO)
    jugadores_treeview.heading("#1", text="Nombre", anchor=CENTER)
    jugadores_treeview.heading("#2", text="Teléfono", anchor=CENTER)
    jugadores_treeview.heading("#3", text="Instagram", anchor=CENTER)
    jugadores_treeview.heading("#4", text="Puntaje", anchor=CENTER)
    jugadores_treeview.heading("#5", text="Tiempo", anchor=CENTER)

    for i in range(1, 5):
        jugadores_treeview.column(f"#{i}", anchor=CENTER)

    jugadores_treeview.grid(row=3, column=4, pady=10, sticky="nsew")

    actualizar_tree(jugadores_treeview)

    ventana.mainloop()



def registar_jugador(nombre,telefono,insta):
        global inicio
        global lista_jugador
        telefono = validarTel()
        if nombre and telefono and insta:
            lista_jugador.append(nombre)
            lista_jugador.append(telefono)
            lista_jugador.append(insta)

            inicio = time.time()

            ventana_juego()

        else:
            messagebox.showerror("Error", "Tienes que ingresar tus datos")




def ventana_juego():

    ventana_JuegoOn = ctk.CTkToplevel()
    ventana_JuegoOn.title("Juego de Preguntas")

    ventana_JuegoOn.attributes('-topmost', True)
    ventana_JuegoOn.attributes("-fullscreen", True)

    isaui_label = ctk.CTkLabel(
        ventana_JuegoOn,
        text="Trivia 40 Años Isaui",
        font=("Impact", 35),
    )
    isaui_label.pack(pady=(25, 0))

    preguntas_frame = ctk.CTkFrame(ventana_JuegoOn)
    preguntas_frame.pack(pady=50)

    label_pregunta = ctk.CTkLabel(preguntas_frame, text="", font=("Impact", 20))
    label_pregunta.grid(row=0, column=0, pady=20)

    botones_respuestas = []

    contador = 1
    for i in range(4):
        boton = ctk.CTkButton(preguntas_frame, text="")
        botones_respuestas.append(boton)
        boton.grid(row=contador // 1, column=0, pady=(15, 0))
        contador += 1

    resultado_label = ctk.CTkLabel(preguntas_frame, text="", font=("Impact", 20))
    resultado_label.grid(row=5, column=0, pady=20)

    label_correctas = ctk.CTkLabel(
        preguntas_frame, text="Respuestas Correctas: 0", font=("Impact", 20)
    )
    label_correctas.grid(row=6, column=0)

    label_incorrectas = ctk.CTkLabel(
        preguntas_frame, text="Respuestas Incorrectas: 0", font=("Impact", 20)
    )
    label_incorrectas.grid(row=7, column=0)

    mostrar_pregunta(label_pregunta,botones_respuestas,resultado_label,label_correctas,label_incorrectas,ventana_JuegoOn, preguntas_frame)

    ventana_JuegoOn.mainloop()


###################################################
##### IMPRIME LOS LABELS Y BOTONES. VERIFICA ######
###################################################


def mostrar_pregunta(label_pregunta,botones_respuestas,resultado_label,label_correctas,label_incorrectas, ventana_JuegoOn, preguntas_frame):
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
                    command=lambda i=i: verificar_respuesta(respuesta_real, respuestas[i],resultado_label,label_correctas,label_incorrectas,label_pregunta,botones_respuestas, ventana_JuegoOn, preguntas_frame),
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
            
            fin_Juego(ventana_JuegoOn, preguntas_frame)



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
def verificar_respuesta(respuesta_real, respuesta,resultado_label,label_correctas,label_incorrectas,label_pregunta,botones_respuestas,  ventana_JuegoOn, preguntas_frame):
    global contador_correctas, contador_incorrectas

    if respuesta == respuesta_real:  # pregunta[2] contiene la respuesta correcta
        resultado_label.configure(text="¡Correcto!")
        contador_correctas += 1
        label_correctas.configure(
            text=f"Respuestas Correctas: {contador_correctas}"
        )
        
    else:
        resultado_label.configure(text="Incorrecto")
        contador_incorrectas += 1
        label_incorrectas.configure(
            text=f"Respuestas Incorrectas: {contador_incorrectas}"
        )
    mostrar_pregunta(label_pregunta,botones_respuestas,resultado_label,label_correctas,label_incorrectas, ventana_JuegoOn, preguntas_frame)

def cerrar_ventana(ventana_JuegoOn):
    actualizar_tree(jugadores_treeview)
    ventana_JuegoOn.destroy()
    



def fin_Juego(ventana_JuegoOn, pregunta_frame):
    global preguntas_respondidas
    global contador_correctas
    global contador_incorrectas
    global tiempo_total
    global lista_jugador
    global jugadores_treeview
    
    pregunta_frame.destroy()

    frame_Fin = ctk.CTkFrame(ventana_JuegoOn)
    frame_Fin.pack(pady=50)

    agradecimiento_Label = ctk.CTkLabel(frame_Fin, text="Muchas gracias por participar")
    agradecimiento_Label.pack()

    label_1 = ctk.CTkLabel(frame_Fin, text=f"Tiempo total: {tiempo_total}")
    label_1.pack()

    label_2 = ctk.CTkLabel(frame_Fin, text=f"Puntaje obtenido: {contador_correctas*100}")
    label_2.pack()

    label_3 = ctk.CTkLabel(frame_Fin, text=f"Respuestas correctas: {contador_correctas}")
    label_3.pack()

    label_4 = ctk.CTkLabel(frame_Fin, text=f"Respuestas Incorrectas: {contador_incorrectas}")
    label_4.pack()

    cursor.execute("INSERT INTO Jugador (nombre, telefono, instagram, puntaje, tiempo) values (%s,%s,%s,%s,%s)", (lista_jugador[0], lista_jugador[1], lista_jugador[2], contador_correctas*100, tiempo_total))
    conexion.commit()

    lista_jugador = []
    preguntas_respondidas= []
    contador_correctas = 0
    contador_incorrectas = 0

    boton_volver = ctk.CTkButton(frame_Fin, text= "Volver a la pantalla de inicio", command = lambda: [cerrar_ventana(ventana_JuegoOn)])
    boton_volver.pack()

    

if __name__ == "__main__":
    ventana_juego()