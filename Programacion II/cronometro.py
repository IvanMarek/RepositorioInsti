import tkinter as tk
import time

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
    # Aquí puedes guardar 'tiempo_guardado' en tu base de datos o en un archivo

ventana = tk.Tk()
ventana.title("Cronómetro")

minutos_transcurridos = 0
segundos_transcurridos = 0
cronometro_en_ejecucion = False

tiempo_str = tk.StringVar()
tiempo_str.set("00:00")

etiqueta_tiempo = tk.Label(ventana, textvariable=tiempo_str, font=("Arial", 24))
etiqueta_tiempo.pack(pady=20)

boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar_cronometro)
boton_iniciar.pack()

boton_detener = tk.Button(ventana, text="Detener", command= lambda: [guardar_tiempo(), detener_cronometro()])
boton_detener.pack()


ventana.mainloop()