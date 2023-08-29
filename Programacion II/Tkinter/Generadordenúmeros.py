from tkinter import *
from tkinter import ttk
import random

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("400x180")
        self.window.config(bg="#A8C0C2")
        self.createWidgets()
        self.window.mainloop()

    def azar(self):
        self.primerNum= self.num1.get()
        self.segundoNum= self.num2.get()
        self.primerNum= int(self.primerNum)
        self.segundoNum= int(self.segundoNum)

        self.numeroRandom= random.randint(self.primerNum,self.segundoNum)
        self.generador.config(state=NORMAL)
        self.generador.delete(0,END)
        self.generador.insert(0,self.numeroRandom)
        self.generador.config(state="readonly")


    def createWidgets(self):

        self.primerNum= ttk.Label(self.window, text=" Número 1")
        self.primerNum.grid(column=1, row=1, padx=(30, 10), pady=(20,10))

        self.segundoNum= ttk.Label(self.window, text=" Número 2")
        self.segundoNum.grid(column=1, row=2, padx=(30, 10))

        self.etigenerarNum= ttk.Label(self.window, text=" Número generado ")
        self.etigenerarNum.grid(column=1, row=3, padx=(30, 10), pady=(10))

        self.num1= ttk.Spinbox(self.window, from_=-100, to=50, justify=CENTER, width=20)
        self.num1.grid(column=2, row=1, padx=10, pady=(11,0))
        self.num1.insert(0,1)
        self.num1.config(state="readonly")

        self.num2= ttk.Spinbox(self.window, from_= 50, to=100, justify=CENTER, width=20)
        self.num2.grid(column=2, row=2, padx=10)
        self.num2.insert(0,50)
        self.num2.config(state="readonly")

        self.generador= ttk.Entry(self.window, justify=CENTER, width=22)
        self.generador.grid(column=2, row=3)
        self.generador.insert(0,0)
        self.generador.config(state="readonly")

        self.botonGenerar= ttk.Button(self.window, text="Generar" )
        self.botonGenerar.grid(row=4, column=2)
        self.botonGenerar.config(command= lambda: self.azar())
        
def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()