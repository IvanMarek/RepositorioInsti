import tkinter as tk
import customtkinter as ctk
import mysql.connector
import random

ctk.set_default_color_theme("blue")

class VentanaJuego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego de Preguntas")
        self.ventana.attributes('-fullscreen', True)

        self.minutos_transcurridos = 0
        self.segundos_transcurridos = 0
        self.cronometro_en_ejecucion = False

        self.tiempo_str = tk.StringVar()
        self.tiempo_str.set("00:00")

        self.preguntas_respondidas = []
        self.contador_correctas = 0
        self.contador_incorrectas = 0

        isaui_label = ctk.CTkLabel(self.ventana, text="Trivia 40 Años Isaui", font=("Impact", 35))
        isaui_label.pack(pady=(25, 0))

        preguntas_frame = ctk.CTkFrame(self.ventana)
        preguntas_frame.pack(pady=50)

        self.label_pregunta = ctk.CTkLabel(preguntas_frame, text="", font=("Impact", 20))
        self.label_pregunta.grid(row=0, column=0, pady=20)

        self.botones_respuestas = []
        contador = 1
        for i in range(4):
            boton = ctk.CTkButton(preguntas_frame, text="")
            self.botones_respuestas.append(boton)
            boton.grid(row=contador // 1, column=0, pady=(15, 0))
            contador += 1

        self.resultado_label = ctk.CTkLabel(preguntas_frame, text="", font=("Impact", 20))
        self.resultado_label.grid(row=5, column=0, pady=20)

        self.label_correctas = ctk.CTkLabel(preguntas_frame, text="Respuestas Correctas: 0", font=("Impact", 20))
        self.label_correctas.grid(row=6, column=0)

        self.label_incorrectas = ctk.CTkLabel(preguntas_frame, text="Respuestas Incorrectas: 0", font=("Impact", 20))
        self.label_incorrectas.grid(row=7, column=0)

        etiqueta_tiempo = ctk.CTkLabel(preguntas_frame, textvariable=self.tiempo_str, font=("Impact", 20))
        etiqueta_tiempo.grid(row=7, column=1, pady=20, padx=10)

        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ivan08012000@",
            database="juego",
            port=3305,
        )
        self.mostrar_pregunta()

    def actualizar_cronometro(self):
        if self.cronometro_en_ejecucion:
            self.segundos_transcurridos += 1
            if self.segundos_transcurridos == 60:
                self.minutos_transcurridos += 1
                self.segundos_transcurridos = 0
            self.tiempo_str.set(f"{self.minutos_transcurridos:02d}:{self.segundos_transcurridos:02d}")
            self.ventana.after(1000, self.actualizar_cronometro)

    def iniciar_cronometro(self):
        self.cronometro_en_ejecucion = True
        self.actualizar_cronometro()

    def detener_cronometro(self):
        self.cronometro_en_ejecucion = False

    def obtener_pregunta_aleatoria(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT codpreguntas, preguntas, respuestas, respuestaErronea_uno, respuestaErronea_dos, respuestaErronea_tres FROM preguntas")
        preguntas = cursor.fetchall()

        preguntas_no_respondidas = [pregunta for pregunta in preguntas if pregunta not in self.preguntas_respondidas]

        if not preguntas_no_respondidas:
            return None

        pregunta = random.choice(preguntas_no_respondidas)
        self.preguntas_respondidas.append(pregunta)
        return pregunta

    def mostrar_pregunta(self):
        pregunta = self.obtener_pregunta_aleatoria()
        if pregunta:
            self.label_pregunta.configure(text=pregunta[1])  # pregunta[1] contiene el texto de la pregunta
            respuestas = [pregunta[2], pregunta[3], pregunta[4], pregunta[5]]
            random.shuffle(respuestas)

            for i in range(4):
                self.botones_respuestas[i].configure(text=respuestas[i], command=lambda i=i: self.verificar_respuesta(pregunta, respuestas[i]))
        else:
            self.label_pregunta.configure(text="¡Has respondido todas las preguntas!")
            for boton in self.botones_respuestas:
                boton.configure(state="disabled")

    def verificar_respuesta(self, pregunta, respuesta):
        if respuesta == pregunta[2]:  # pregunta[2] contiene la respuesta correcta
            self.resultado_label.configure(text="¡Correcto!")
            self.contador_correctas += 1
            self.label_correctas.configure(text=f"Respuestas Correctas: {self.contador_correctas}")
        else:
            self.resultado_label.configure(text="Incorrecto")
            self.contador_incorrectas += 1
            self.label_incorrectas.configure(text=f"Respuestas Incorrectas: {self.contador_incorrectas}")

        if self.preguntas_respondidas:
            self.mostrar_pregunta()
        else:
            self.label_pregunta.configure(text="¡Has respondido todas las preguntas!")
            for boton in self.botones_respuestas:
                boton.configure(state="disabled")

if __name__ == "__main__":
    ventana = ctk.CTk()
    juego = VentanaJuego(ventana)
    ventana.mainloop()