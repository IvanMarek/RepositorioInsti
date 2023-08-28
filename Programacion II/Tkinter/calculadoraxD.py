from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("280x200")
        self.createWidgets()
        self.window.mainloop()

    def validarNum(self):
        while True:
            try:
                self.numero1 = int(self.num1.get())
                self.numero2 = int(self.num2.get())

            except:
                self.resultado.config(state=NORMAL)
                self.resultado.delete(0,END)
                self.resultado.insert(" Error de sintaxis ")
                self.resultado.config(state="readonly")




    def createWidgets(self):
        self.primerNum= ttk.Label(self.window, text="Primer número")
        self.primerNum.grid(column=1, row=1, padx=(30, 10), pady=(20,10))

        self.segundoNum= ttk.Label(self.window, text="Segundo número")
        self.segundoNum.grid(column=1, row=2, padx=(30, 10))

        self.etiResultado= ttk.Label(self.window, text="Resultado")
        self.etiResultado.grid(column=1, row=3, padx=(30, 10), pady=(10))

        self.num1= ttk.Entry(self.window, width=17)
        self.num1.grid(column=2, row=1, pady=(20,10), padx=(10,0), sticky=W+E)

        self.num2= ttk.Entry(self.window, width=17)
        self.num2.grid(column=2, row=2, padx=(10,0), sticky=W+E)

        self.resultado= ttk.Entry(self.window, width=17)
        self.resultado.grid(column=2, row=3, pady=(10), padx=(10,0), sticky=W+E)
        self.resultado.config(state="readonly")

        self.botonSum= ttk.Button(self.window, text=" + ")
        self.botonSum.grid(column=1, row= 4, sticky=W+E, padx=(25,0))
        self.botonSum.config(command= lambda: ())

        self.botonResta= ttk.Button(self.window, text=" - ")
        self.botonResta.grid(column=2, row= 4, sticky=W+E, padx=(10,0))

        self.botonMultiplicacion= ttk.Button(self.window, text=" * ")
        self.botonMultiplicacion.grid(column=1, row= 5, sticky=W+E, padx=(25,0))

        self.botonDivision= ttk.Button(self.window, text=" / ")
        self.botonDivision.grid(column=2, row= 5, sticky=W+E, padx=(10,0))

        self.botonPorcen= ttk.Button(self.window, text=" % ")
        self.botonPorcen.grid(column=1, row= 6, sticky=W+E, padx=(25,0))

        self.botonClear= ttk.Button(self.window, text=" CLEAR ")
        self.botonClear.grid(column=2, row= 6, sticky=W+E, padx=(10,0))
        self.botonClear.config(command= lambda: [self.contador.config(state=NORMAL),self.contador.delete(0,END), self.contador.insert(0,0), self.contador.config(state="readonly")])


def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()