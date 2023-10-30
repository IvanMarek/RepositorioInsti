import customtkinter as ctk
import time
import mysql.connector
from tkinter import messagebox
import random


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ivan08012000@",
    database="juego",
    port=3305,
)


"""
def actualizar_cronometro():
    global minutos_transcurridos, segundos_transcurridos
    if cronometro_en_ejecucion:
        segundos_transcurridos += 1
        if segundos_transcurridos == 60:
            minutos_transcurridos += 1
            segundos_transcurridos = 0
        tiempo_str.set(f"{minutos_transcurridos:02d}:{segundos_transcurridos:02d}")
        ventana.after(1000, actualizar_cronometro)

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
    return(tiempo_guardado)"""

def ventana_Juego():

    ventana_JuegoOn = ctk.CTk()
    ventana_JuegoOn.title("40 'ISAUI' ")
    ventana_JuegoOn.attributes('-fullscreen', True)

    isaui_label = ctk.CTkLabel(ventana_JuegoOn, text="Trivia 40 Años Isaui", font=("Impact", 35), )
    isaui_label.pack(pady= (25,0))
    """(row=0, column=0, columnspan= 6, sticky="n", pady= (25,0), padx= (105,0))"""

    frame_pregunta = ctk.CTkFrame (ventana_JuegoOn)
    frame_pregunta.pack()

    pregunta_label = ctk.CTkLabel()

    boton_respuesta1 = ()




    ventana_JuegoOn.mainloop()

if __name__ == "__main__":
    ventana_Juego()