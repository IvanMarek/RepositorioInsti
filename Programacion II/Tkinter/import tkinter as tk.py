import tkinter as tk

def on_button_click():
    print("¡Botón redondo fue presionado!")

# Configuración de la ventana
root = tk.Tk()
root.title("Botón Redondo")
root.geometry("300x200")

# Crear un marco para contener el botón redondo
button_frame = tk.Frame(root)
button_frame.pack(pady=50)

# Crear un botón ovalado personalizado
round_button = tk.Button(button_frame, text="Presionar", command=on_button_click, width=10, height=2, relief="flat", bg="blue", fg="white")
round_button.config(font=("Helvetica", 10, "bold"))
round_button.grid(row= 2, column= 2)

# Hacer que el botón se vea redondo
round_button.pack(padx=50, pady=20)
round_button.place(relwidth=1, relheight=1, anchor="center")

root.mainloop()