from tkinter import *
from tkinter import ttk


class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("400x220")
        self.window.config(bg="#A8C0C2")
        self.createWidgets()
        self.window.mainloop()

    def calcular(self):
        calculara= self.primerNum.get() + self.operacion[0] + self.segundoNum.get()
        self.numero1= self.primerNum.get()
        self.numero2= self.segundoNum.get()
        try:
            self.numero1= int(self.numero1)
            self.numero2= int(self.numero2)
            resolver= eval(calculara)
            self.resultado.config(state=NORMAL)
            self.resultado.delete(0,END)
            self.resultado.insert(0,resolver)
            self.resultado.config(state="readonly")
        except:
            self.resultado.config(state=NORMAL)
            self.resultado.delete(0,END)
            self.resultado.insert(0," Error de sintaxis ")
            self.resultado.config(state="readonly")




    def createWidgets(self):
        
        self.operacion=[]
        self.valor1= ttk.Label(self.window, text=" Valor 1")
        self.valor1.grid(column=1, row=2, padx=(30, 10), pady=(10,10))

        self.valor2= ttk.Label(self.window, text=" Valor 2")
        self.valor2.grid(column=1, row=3, padx=(30, 10), pady=(0,10))

        self.etiresultado= ttk.Label(self.window, text=" Resultado ")
        self.etiresultado.grid(column=1, row=4, padx=(30, 10), pady=(0,10))

        self.operaciones= ttk.Label(self.window, text=" Operaciones ")
        self.operaciones.grid(column=4, row=1, padx=(10, 10), pady=(10,10))

        self.primerNum= ttk.Entry(self.window, width=20, justify=CENTER)
        self.primerNum.grid(row=2, column= 2, pady=(10,10), sticky=N)

        self.segundoNum= ttk.Entry(self.window, width=20, justify=CENTER)
        self.segundoNum.grid(row=3, column= 2, pady=(0,10), sticky=N)

        self.resultado= ttk.Entry(self.window, width=20, justify=CENTER)
        self.resultado.grid(row=4, column= 2, pady=(0,10), sticky=N)
        self.resultado.config(state="readonly")

        self.botoncalcular= ttk.Button(self.window, text=" Calcular ", command= lambda: self.calcular())
        self.botoncalcular.grid(row=5, column=2)

        self.botonSuma= ttk.Radiobutton(self.window, text=" Suma ", value=1,command= lambda: self.operacion.insert(0, "+") )
        self.botonSuma.grid(row=2, column=4, sticky=W+E, padx=10)

        self.botonRestar= ttk.Radiobutton(self.window, text=" Restar ", value=2,command= lambda: self.operacion.insert(0, "-"))
        self.botonRestar.grid(row=3, column=4, sticky=W+E, padx=10)

        self.botonMulti= ttk.Radiobutton(self.window, text=" Multiplicar ", value=3,command= lambda: self.operacion.insert(0, "*"))
        self.botonMulti.grid(row=4, column=4, sticky=W+E, padx=10)

        self.botonDividir= ttk.Radiobutton(self.window, text=" Dividir ", value=4,command= lambda: self.operacion.insert(0, "/"))
        self.botonDividir.grid(row=5, column=4, sticky=W+E, padx=10)


def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()