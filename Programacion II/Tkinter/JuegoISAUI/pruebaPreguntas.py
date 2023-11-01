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

lista_jugador = []

preguntas_respondidas = []
contador_correctas = 0
contador_incorrectas = 0
global tiempo_total


def ventana_juego(inicio):
    def obtener_pregunta_aleatoria():
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id_pregunta, pregunta, respuesta, respuesta_erronea_uno, respuesta_erronea_dos, respuesta_erronea_tres FROM preguntas"
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

    def mostrar_pregunta():
        pregunta = obtener_pregunta_aleatoria()
        if pregunta:
            label_pregunta.configure(
                text=pregunta[1]
            )  # pregunta[1] contiene el texto de la pregunta
            respuestas = [pregunta[2], pregunta[3], pregunta[4], pregunta[5]]
            random.shuffle(respuestas)

            for i in range(4):
                botones_respuestas[i].configure(
                    text=respuestas[i],
                    command=lambda i=i: verificar_respuesta(pregunta, respuestas[i]),
                )
        else:
            label_pregunta.configure(text="¡Has respondido todas las preguntas!")

            tiempo_transcurrido = (time.time() - inicio) * 1000
            print("Tiempo transcurrido:", tiempo_transcurrido)
            minutos, segundos = divmod(tiempo_transcurrido / 1000, 60)
            segundos, milisegundos = divmod(segundos, 1)
            global tiempo_total
            tiempo_total = f"tiempo transcurrido: {int(minutos)}, {int(segundos)}, {int(milisegundos)*1000}"
            etiqueta_tiempo.configure(text=f" {tiempo_total}")

            lista_jugador.append(tiempo_total)
            print(lista_jugador)
            for boton in botones_respuestas:
                boton.configure(state="disabled")

    def verificar_respuesta(pregunta, respuesta):
        global contador_correctas, contador_incorrectas
        if respuesta == pregunta[2]:  # pregunta[2] contiene la respuesta correcta
            resultado_label.configure(text="¡Correcto!")
            contador_correctas += 1
            label_correctas.configure(
                text=f"Respuestas Correctas: {contador_correctas}"
            )
            return contador_correctas
        else:
            resultado_label.configure(text="Incorrecto")
            contador_incorrectas += 1
            label_incorrectas.configure(
                text=f"Respuestas Incorrectas: {contador_incorrectas}"
            )
        mostrar_pregunta()

    ventana_JuegoOn = ctk.CTk()
    ventana_JuegoOn.title("Juego de Preguntas")
    ventana_JuegoOn.attributes("-fullscreen", True)

    tiempo_str = tk.StringVar()
    tiempo_str.set("00:00")

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

    etiqueta_tiempo = ctk.CTkLabel(preguntas_frame, text="00:00", font=("Impact", 20))
    etiqueta_tiempo.grid(row=7, column=1, pady=20, padx=10)

    mostrar_pregunta()

    ventana_JuegoOn.mainloop()


if __name__ == "__main__":
    ventana_juego()
