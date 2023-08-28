from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("400x250")
        self.window.config(bg="#7E9271")
        self.createWidgets()
        self.window.mainloop()


    def guardarPeli(self):
        nombre= self.inputpPeli.get()
        self.listaPelis.insert(0,nombre)

    def createWidgets(self):
        self.text= ttk.Label(self.window, text=" Escribe el título de una película ", justify=CENTER)
        self.text.grid(column=1, row=1, padx=(15, 10), pady=(20,0))

        self.text2= ttk.Label(self.window, text=" Películas ", justify=CENTER)
        self.text2.grid(row=1, column=2, padx=(0,0), pady=(20,10))

        self.inputpPeli= ttk.Entry(self.window, width=25, justify=CENTER)
        self.inputpPeli.grid(row=2, column= 1, pady=(25,0), sticky=N)

        self.botonGuardar= ttk.Button(self.window, text="Añadir", )
        self.botonGuardar.grid(row=3, column= 1, padx=(0,0), pady=(0,0), sticky=N)
        self.botonGuardar.config(command= lambda: self.guardarPeli())

        self.listaPelis= Listbox(justify=CENTER, width=30)
        self.listaPelis.grid(row=2, column=2, padx=10, rowspan=2)



def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()