import tkinter as tk
import tkinter as ttk
from tkinter import filedialog


def crear_ventana():
    ventana = tk.Tk()
    ventana.title("40 'ISAUI' ")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
    ventana.config(bg="#010101")

    isaui_label = ttk.Label(
        ventana, text="Trivia 40 Años Isaui", font=("Helvetica", 14)
    )
    isaui_label.grid(row=0, column=0, columnspan=6)

    formulario_frame = tk.Frame(ventana, bd=2, relief=tk.SOLID)
    formulario_frame.grid(padx=10, pady=10)

    participante_label = ttk.Label(formulario_frame, text="Ingrese sus datos")
    participante_label.grid(row=1, column=0)

    nombre_label = ttk.Label(formulario_frame, text="Nombre")
    nombre_label.grid(row=2, column=0)
    nombre_entry = ttk.Entry(formulario_frame)
    nombre_entry.grid(row=2, column=2, columnspan=2)

    apellido_label = ttk.Label(formulario_frame, text="Apellido")
    apellido_label.grid(row=3, column=0)
    apellido_entry = ttk.Entry(formulario_frame)
    apellido_entry.grid(row=3, column=2, columnspan=2)

    tel_label = ttk.Label(formulario_frame, text="Teléfono")
    tel_label.grid(row=4, column=0)
    tel_entry = ttk.Entry(formulario_frame)
    tel_entry.grid(row=4, column=2, columnspan=2)

    instagram_label = ttk.Label(formulario_frame, text="Instagram")
    instagram_label.grid(row=5, column=0)
    instagram_entry = ttk.Entry(formulario_frame)
    instagram_entry.grid(row=5, column=2, columnspan=2)


crear_ventana()
tk.mainloop()
