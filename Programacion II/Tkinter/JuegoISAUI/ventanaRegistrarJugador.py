from tkinter import *
from tkinter import ttk as ttk
import customtkinter as ctk
from tkinter import filedialog
import mysql.connector
from tkinter import messagebox
import pruebaPreguntas

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ivan08012000@",
    database="juego",
    port=3305,
)



def ventana_Inicio():

    def registar_jugador():
        lista_jugador = []
        nombre = nombre_entry.get().upper()
        telefono = tel_entry.get()
        insta= instagram_entry.get()
        if nombre and telefono and insta:
            lista_jugador.append(nombre)
            lista_jugador.append(telefono)
            lista_jugador.append(insta)
            print(lista_jugador)
            pruebaPreguntas.ventana_juego()
        else:
            messagebox.showerror('Error','Tienes que ingresar tus datos')


    ventana = ctk.CTk()
    ventana.title("40 'ISAUI' ")
    """ ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")"""
    ventana.attributes('-fullscreen', True)
  



    isaui_label = ctk.CTkLabel(ventana, text="Trivia 40 Años Isaui", font=("Impact", 35), )
    isaui_label.grid(row=0, column=0, columnspan= 6, sticky="n", pady= (25,0), padx= (105,0))
    """isaui_label.pack()"""


    formulario_frame = ctk.CTkFrame(ventana)
    formulario_frame.grid(row= 2, column= 0, columnspan= 3, padx=20, pady=20)

    participante_label = ctk.CTkLabel(formulario_frame, text="Ingrese sus datos", font=("Impact", 20))
    participante_label.grid(row=1, column=0, padx= 20, pady=15)


    nombre_label = ctk.CTkLabel(formulario_frame, text="Nombre", font=("Impact", 20))
    nombre_label.grid(row=2, column=0, padx= (10,5))
    nombre_entry = ctk.CTkEntry(formulario_frame, border_width= 3, width=155)
    nombre_entry.grid(row=2, column=2, pady= 5, columnspan=2, padx=(0,15))
    #nombre_entry.insert(0, "Ingrese su nombre")
    #nombre_entry.bind("<Button-1>", lambda x: nombre_entry.delete(0, ctk.END))


    tel_label = ctk.CTkLabel(formulario_frame, text="Teléfono", font=("Impact", 20))
    tel_label.grid(row=4, column=0, padx= (10,5))
    tel_entry = ctk.CTkEntry(formulario_frame, border_width= 3, width=155)
    tel_entry.grid(row=4, column=2, pady= 5, columnspan=2, padx=(0,15))
    #tel_entry.insert(0, "Ingrese número")
    #tel_entry.bind("<Button-1>", lambda x: tel_entry.delete(0, ctk.END))

    instagram_label = ctk.CTkLabel(formulario_frame, text="Instagram", font=("Impact", 20))
    instagram_label.grid(row=5, column=0, padx= (10,5))
    instagram_entry = ctk.CTkEntry(formulario_frame, border_width= 3, width=155)
    instagram_entry.grid(row=5, column=2, pady= 5, columnspan=2, padx=(0,15))
    #instagram_entry.insert(0, "Ingrese su Instagram")
    #instagram_entry.bind("<Button-1>", lambda x: instagram_entry.delete(0, ctk.END))

    
    boton_jugarr = ctk.CTkButton(formulario_frame, text= " Comenzar a jugar ", font=("Impact", 20), command= lambda: registar_jugador())
    boton_jugarr.grid(row= 6, column= 2, pady= (25, 10), padx=(0,15))

    frame2 = ctk.CTkFrame(ventana)
    frame2.grid(row= 2, column= 5, padx=20, pady=(135,0))

    tituloJugadores_label = ctk.CTkLabel(frame2, text="Tabla de jugadores", font=("Impact", 20))
    tituloJugadores_label.grid(row=2, column= 4)
                                         
    
    style = ttk.Style()
    style.configure("Treeview", rowheight=30)
    fuente = ("Impact", 16)


    jugadores_treeview = ttk.Treeview(frame2, columns=("Nombre", "Puntaje","Tiempo", "Teléfono"), style='Treeview')
    jugadores_treeview.column("#0", width=0, stretch=NO)
    jugadores_treeview.heading("#1", text='Nombre',anchor=CENTER) 
    jugadores_treeview.heading("#2", text="Puntaje", anchor=CENTER)  
    jugadores_treeview.heading("#3", text="Tiempo", anchor=CENTER)
    jugadores_treeview.heading("#4", text="Teléfono", anchor=CENTER)

    for i in range(1,4):  
        jugadores_treeview.column(f"#{i}", anchor=CENTER)

    cursor = conexion.cursor()

    cursor.execute( """SELECT * FROM jugador ORDER BY puntaje DESC;""")

    jugadores = cursor.fetchall()

    for resultado in jugadores:
        codjugador, nombre, puntaje, tiempo, teléfono  = resultado

        jugadores_treeview.insert('','end', values=[nombre, puntaje, tiempo, teléfono], tags=("fuente_personalizada",))
        jugadores_treeview.tag_configure("fuente_personalizada", font=fuente)

    jugadores_treeview.grid(row=3, column=4, pady=10, sticky="nsew")

    ventana.mainloop()

if __name__ == "__main__":
    ventana_Inicio()

