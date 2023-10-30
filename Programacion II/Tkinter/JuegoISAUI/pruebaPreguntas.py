import tkinter as tk
import customtkinter as ctk
from tkinter import ttk as ttk
import mysql.connector
import random
import time


ctk.set_default_color_theme("blue")

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ivan08012000@",
    database="juego",
    port=3305,
)
preguntas_respondidas = []
contador_correctas = 0
contador_incorrectas = 0
minutos_transcurridos = 0
segundos_transcurridos = 0
cronometro_en_ejecucion = False




def ventana_juego():

    def actualizar_cronometro():
        global minutos_transcurridos, segundos_transcurridos
        if cronometro_en_ejecucion:
            segundos_transcurridos += 1
            if segundos_transcurridos == 60:
                minutos_transcurridos += 1
                segundos_transcurridos = 0
            tiempo_str.set(f"{minutos_transcurridos:02d}:{segundos_transcurridos:02d}")
            preguntas_frame.after(1000, actualizar_cronometro)

    def iniciar_cronometro():
        global cronometro_en_ejecucion
        cronometro_en_ejecucion = True
        actualizar_cronometro()

    def detener_cronometro():
        global cronometro_en_ejecucion
        cronometro_en_ejecucion = False

    def guardar_tiempo():
        global minutos_transcurridos, segundos_transcurridos
        tiempo_guardado = (minutos_transcurridos, segundos_transcurridos)
        print(tiempo_guardado)
        return(tiempo_guardado)

    def obtener_pregunta_aleatoria():
        cursor = conexion.cursor()
        cursor.execute("SELECT codpreguntas, preguntas, respuestas, respuestaErronea_uno, respuestaErronea_dos,respuestaErronea_tres FROM preguntas")
        preguntas = cursor.fetchall()

        preguntas_no_respondidas = [pregunta for pregunta in preguntas if pregunta not in preguntas_respondidas]

        if not preguntas_no_respondidas:
            return None
        
        pregunta = random.choice(preguntas_no_respondidas)
        preguntas_respondidas.append(pregunta)
        return pregunta

    def mostrar_pregunta():
        pregunta = obtener_pregunta_aleatoria()
        if pregunta:
            label_pregunta.configure(text=pregunta[1])  # pregunta[1] contiene el texto de la pregunta
            respuestas = [pregunta[2], pregunta[3], pregunta[4], pregunta[5]]
            random.shuffle(respuestas)

            for i in range(4):
                botones_respuestas[i].configure(text=respuestas[i], command=lambda i=i: verificar_respuesta(pregunta, respuestas[i]))
        else:
            label_pregunta.configure(text="¡Has respondido todas las preguntas!")
            for boton in botones_respuestas:
                boton.configure(state="disabled")

    def verificar_respuesta(pregunta, respuesta):
        global contador_correctas, contador_incorrectas
        if respuesta == pregunta[2]:  # pregunta[2] contiene la respuesta correcta
            resultado_label.configure(text="¡Correcto!")
            contador_correctas += 1
            label_correctas.configure(text=f"Respuestas Correctas: {contador_correctas}")
        else:
            resultado_label.configure(text="Incorrecto")
            contador_incorrectas += 1
            label_incorrectas.configure(text=f"Respuestas Incorrectas: {contador_incorrectas}")
        mostrar_pregunta()

    ventana_JuegoOn = ctk.CTk()
    ventana_JuegoOn.title("Juego de Preguntas")
    ventana_JuegoOn.attributes('-fullscreen', True)

    tiempo_str = tk.StringVar()
    tiempo_str.set("00:00")


    isaui_label = ctk.CTkLabel(ventana_JuegoOn, text="Trivia 40 Años Isaui", font=("Impact", 35), )
    isaui_label.pack(pady= (25,0))

    preguntas_frame = ctk.CTkFrame(ventana_JuegoOn)
    preguntas_frame.pack(pady= 50)



    label_pregunta = ctk.CTkLabel(preguntas_frame, text="", font=("Impact", 20))
    label_pregunta.grid(row= 0, column=0, pady=20)

    botones_respuestas = []
    contador = 1
    for i in range(4):
        boton = ctk.CTkButton(preguntas_frame, text="")
        botones_respuestas.append(boton)
        boton.grid(row= contador // 1, column= 0, pady=(15,0))
        contador += 1

    resultado_label = ctk.CTkLabel(preguntas_frame, text="", font=("Impact", 20))
    resultado_label.grid(row= 5, column=0, pady=20)

    label_correctas = ctk.CTkLabel(preguntas_frame, text="Respuestas Correctas: 0", font=("Impact", 20))
    label_correctas.grid(row= 6, column=0)

    label_incorrectas = ctk.CTkLabel(preguntas_frame, text="Respuestas Incorrectas: 0", font=("Impact", 20))
    label_incorrectas.grid(row= 7, column=0)

    etiqueta_tiempo = ctk.CTkLabel(preguntas_frame, text=tiempo_str.get(), font=("Impact", 20))
    etiqueta_tiempo.grid(row= 7, column=1, pady=20, padx= 10)

    mostrar_pregunta()

    ventana_JuegoOn.mainloop()


if __name__ == "__main__":
    ventana_juego()