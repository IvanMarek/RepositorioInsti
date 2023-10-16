import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ejemplo de Navegación de Ventanas")
    
    label = tk.Label(ventana, text="")
    label.pack(pady=20)
    
    def mostrar_mensaje(mensaje):
        label.config(text=mensaje)
    
    def siguiente():
        if label.cget("text") == "":
            mostrar_mensaje("Hola")
        elif label.cget("text") == "Hola":
            mostrar_mensaje("Soy un bot")
        elif label.cget("text") == "Soy un bot":
            mostrar_mensaje("Y estoy programado para destruir tu PC")
        elif label.cget("text") == "Y estoy programado para destruir tu PC":
            mostrar_mensaje("ERA MENTIRA, espero no te hayas asustado")
            siguiente_btn.config(text="Finalizar")  # Cambiar el texto del botón
        else:
            ventana.destroy()
    
    mostrar_mensaje("Hola")  # Iniciar con el mensaje "Hola"
    
    siguiente_btn = tk.Button(ventana, text="Siguiente", command=siguiente)
    siguiente_btn.pack()

# Crear la ventana inicial
crear_ventana()

# Iniciar el bucle principal de tkinter
tk.mainloop()