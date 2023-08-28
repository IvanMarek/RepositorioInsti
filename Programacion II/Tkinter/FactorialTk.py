from tkinter import *
from tkinter import ttk


class Aplicacion():

    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("500x120")
        self.createWidgets()
        self.window.mainloop()


    def siguiente(self):
        self.siguient= self.numFact.get()
        self.siguient= int(self.siguient)
        self.siguient+=1
        self.numFact.config(state=NORMAL)
        self.numFact.delete(0,END)
        self.numFact.insert(0,self.siguient)
        self.numFact.config(state="readonly")

    def factoriar(self):

        self.factor= self.numFact.get()
        self.factor= int(self.factor)
        self.anterior= self.factorial.get()
        self.anterior= int(self.anterior)
        self.resultFactorial= self.factor * self.anterior
        self.factorial.config(state=NORMAL)
        self.factorial.delete(0,END)
        self.factorial.insert(0,self.resultFactorial)
        self.factorial.config(state="readonly")



    def createWidgets(self):

        self.tetx= ttk.Label(self.window, text="n")
        self.tetx.grid(column=1, row=3, padx=(35, 10), pady=50)

        self.numFact= ttk.Entry(self.window, justify=CENTER, width=15)
        self.numFact.grid(column=2, row=3)
        self.numFact.insert(0,1)
        self.numFact.config(state="readonly")


        self.tetx2= ttk.Label(self.window, text="Factorial (n)")
        self.tetx2.grid(column=3, row=3, padx=20)

        self.factorial= ttk.Entry(self.window, justify=CENTER, width=15)
        self.factorial.grid(column=4, row=3)
        self.factorial.insert(0,1)
        self.factorial.config(state="readonly")


        self.botonS= ttk.Button(self.window, text="Siguiente", command= lambda:[self.siguiente(), self.factoriar()])
        self.botonS.grid(column=5, row=3, padx=15)





def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()