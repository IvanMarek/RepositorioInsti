from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("550x120")
        self.createWidgets()
        self.window.mainloop()

    def incremento(self):
        self.count= self.contador.get()
        self.count= int(self.count)
        self.count+=1
        self.contador.config(state=NORMAL)
        self.contador.delete(0,END)
        self.contador.insert(0, self.count)
        self.contador.config(state="readonly")

    def descuento(self):
        self.count= self.contador.get()
        self.count= int(self.count)
        self.count-=1
        self.contador.config(state=NORMAL)
        self.contador.delete(0,END)
        self.contador.insert(0, self.count)
        self.contador.config(state="readonly")
    

    def createWidgets(self):

        self.text= ttk.Label(self.window, text="Contador ").grid(row=0, column= 0,padx=(30, 10), pady=45)

        self.contador= ttk.Entry(self.window, width=22, justify=CENTER)
        self.contador.grid(row=0, column= 2,columnspan=2)
        self.contador.insert(0,0)
        self.contador.config(state="readonly")

        self.botoncountUp= ttk.Button(self.window, text=" Count Up ")
        self.botoncountUp.grid(row=0, column= 4, padx=(15,0))
        self.botoncountUp.config(command=self.incremento)

        self.botoncountDown= ttk.Button(self.window, text=" Count Down ")
        self.botoncountDown.grid(row=0, column= 5, padx=(15,0))
        self.botoncountDown.config(command=self.descuento)

        self.botonReset= ttk.Button(self.window, text= " Reset ")
        self.botonReset.grid(row=0, column=6, padx=(15,0))
        self.botonReset.config(command= lambda: [self.contador.config(state=NORMAL),self.contador.delete(0,END), self.contador.insert(0,0), self.contador.config(state="readonly")])


def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()