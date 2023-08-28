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


    def createWidgets(self):

        self.primerNum= ttk.Label(self.window, text=" Número 1")
        self.primerNum.grid(column=1, row=1, padx=(30, 10), pady=(20,10))

        self.segundoNum= ttk.Label(self.window, text=" Número 2")
        self.segundoNum.grid(column=1, row=2, padx=(30, 10))

        self.etigenerarNum= ttk.Label(self.window, text=" Número generado ")
        self.etigenerarNum.grid(column=1, row=3, padx=(30, 10), pady=(10))

        self.num1= ttk.Spinbox(self.window)
        self.num1.grid(column=2, row=1, padx=10)

        self.num2= ttk.Spinbox(self.window)
        self.num2.grid(column=2, row=2, padx=10)

def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()