from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("400x120")
        self.createWidgets()
        self.window.mainloop()

    def incremento(self):
        self.count= self.contador.get()
        self.count= int(self.count)
        self.count-=1
        self.contador.config(state=NORMAL)
        self.contador.delete(0,END)
        self.contador.insert(0, self.count)
        self.contador.config(state="readonly")



    def createWidgets(self):

        self.text= ttk.Label(self.window, text="Contador ").grid(row=0, column= 0,padx= 30, pady=45)

        self.contador= ttk.Entry(self.window, width=22, justify=CENTER)
        self.contador.grid(row=0, column= 2,columnspan=2)
        self.contador.insert(0,88)
        self.contador.config(state="readonly")

        self.botoncount= ttk.Button(self.window, text=" - ")
        self.botoncount.grid(row=0, column= 4, padx= 20)
        self.botoncount.config(command=self.incremento)



def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()