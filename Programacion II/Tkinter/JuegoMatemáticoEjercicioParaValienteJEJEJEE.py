from tkinter import *
from tkinter import ttk
import random


class Aplicacion():

    def __init__(self):
        self.window = Tk()
        self.window.title("Contador")
        self.window.resizable(0,0)
        self.window.geometry("600x400")
        self.window.config(bg="#A8C0C2")
        self.createWidgets()
        self.window.mainloop()


    def dificultas(self):
        self.dificultad= self.dificult[0]
        if self.dificultad == 1:
            self.valorDificultad= 10
        elif self.dificultad == 2:
            self.valorDificultad = 100
        elif self.dificultad == 3:
            self.valorDificultad = 1000

        
    def numerosAlazar(self):

        self.num1= random.randint(0,self.valorDificultad)
        self.num2= random.randint(0,self.valorDificultad)

        self.primerNum.config(state=NORMAL)
        self.primerNum.insert(0,self.num1)
        self.primerNum.config(state="readonly")

        self.segundoNum.config(state=NORMAL)
        self.segundoNum.insert(0,self.num2)
        self.segundoNum.config(state="readonly")


    def signosAlAzar(self):
        self.operaciones=["+","-","*","/"]
        self.signoEs= random.choice(self.operaciones)
        self.signoAzar.config(text=self.signoEs)

    def calcular(self):
        self.numero1= str(self.num1)
        self.numero2= str(self.num2)
        calculara= self.numero1 + self.signoEs + self.numero2
        userResultado= self.EtiqResultado.get()
        userResultado= float(userResultado)
        try:
            resolver= eval(calculara)
            if resolver == userResultado:
                self.contjuegos+=1
                self.contJuegosBuenos+=1
                self.cantJuegos.config(text=f"{self.contjuegos}")
                self.cantJuegosBuenos.config(text=f"{self.contJuegosBuenos}")
            else:
                self.contJuegosMalos+=1
                self.cantJuegosMalos.config(text=f"{self.contJuegosMalos}")
        except:
            self.EtiqResultado.insert(0," Error de sintaxis ")


    def createWidgets(self):
        self.contador= 0
        self.dificult= []

        self.primerNum= ttk.Entry(self.window, width=17, justify=CENTER)
        self.primerNum.grid(row=2, column= 1, padx=(20,10), pady=(20,10), sticky=N)
        self.primerNum.config(state="readonly")

        self.signoAzar= ttk.Label(self.window, text="?")
        self.signoAzar.grid(row=2, column=2, pady=(20,10))

        self.segundoNum= ttk.Entry(self.window, width=17, justify=CENTER)
        self.segundoNum.grid(row=2, column= 3, padx=(10,20),  pady=(20,10), sticky=N)
        self.segundoNum.config(state="readonly")

        self.botonNuevoJuego= ttk.Button(self.window, text= " Nuevo juego ", command= lambda: [self.primerNum.config(state=NORMAL) ,self.primerNum.delete(0,END), self.primerNum.config(state="readonly"), self.segundoNum.config(state=NORMAL) , self.segundoNum.delete(0,END), self.segundoNum.config(state="readonly"),self.numerosAlazar(), self.signosAlAzar(), self.segundoNum.delete(0,END), self.EtiqResultado.delete(0,END),self.EtiqResultado.config(state=NORMAL)])
        self.botonNuevoJuego.grid(row=3, column=4, sticky=N)


        self.botonSuma= ttk.Radiobutton(self.window, text=" Suma ")
        self.botonSuma.grid(row=3, column=1, sticky=W+E, padx=(20,0), pady=(25,0))
        self.botonSuma.config(state=DISABLED)

        self.botonRestar= ttk.Radiobutton(self.window, text=" Restar ")
        self.botonRestar.grid(row=4, column=1, sticky=W+E, padx=(20,0), pady=(3,0))
        self.botonRestar.config(state=DISABLED)

        self.botonMulti= ttk.Radiobutton(self.window, text=" Multiplicar ")
        self.botonMulti.grid(row=5, column=1, sticky=W+E, padx=(20,0), pady=(3,0))
        self.botonMulti.config(state=DISABLED)

        self.botonDividir= ttk.Radiobutton(self.window, text=" Dividir ")
        self.botonDividir.grid(row=6, column=1, sticky=W+E, padx=(20,0), pady=(3,0))
        self.botonDividir.config(state=DISABLED)

        self.EtiqResultado= ttk.Entry(self.window, width=17, justify=CENTER)
        self.EtiqResultado.grid(row=5, column=4)

        self.botonResultado= ttk.Button(self.window, text=" Resultado ", command= lambda: [self.calcular(), self.EtiqResultado.delete(0,END), self.EtiqResultado.config(state="readonly")])
        self.botonResultado.grid(row=7, column=4, sticky=W+E)

        self.contjuegos=0
        self.contJuegosBuenos=0
        self.contJuegosMalos=0

        self.juegos= ttk.Label(self.window, text=" Juegos: ", justify=RIGHT)
        self.juegos.grid(row=9, column=3, sticky=E, padx=(0,5), pady=(30,5))

        self.cantJuegos= ttk.Label(self.window, text="0", justify=RIGHT)
        self.cantJuegos.grid(row=9, column=4, padx=(5,5), pady=(26,0), sticky=W)

        self.juegosBuenos= ttk.Label(self.window, text=" Buenos: ", justify=RIGHT)
        self.juegosBuenos.grid(row=10, column=3, sticky=E, padx=(0,5), pady=(1,0))

        self.cantJuegosBuenos= ttk.Label(self.window, text="0", justify=RIGHT)
        self.cantJuegosBuenos.grid(row=10, column=4, padx=(5,5), pady=(1,0), sticky=W)

        self.juegosMalos= ttk.Label(self.window, text=" Malos: ", justify=RIGHT)
        self.juegosMalos.grid(row=11, column=3, sticky=E, padx=(0,5), pady=(5,0))

        self.cantJuegosMalos= ttk.Label(self.window, text="0", justify=RIGHT)
        self.cantJuegosMalos.grid(row=11, column=4, padx=(5,5), pady=(5,0), sticky=W)

        self.botonFacil= ttk.Radiobutton(self.window, text=" Fácil", value=1,command= lambda: [self.dificult.append(1), self.dificultas(), self.cantJuegos.config(text="0"), self.cantJuegosBuenos.config(text="0"), self.cantJuegosMalos.config(text="0")])
        self.botonFacil.grid(row=11, column=0, sticky=W+E, padx=(10,0))

        self.botonNormal= ttk.Radiobutton(self.window, text=" Normal ", value=2,command= lambda:[self.dificult.append(2), self.dificultas(), self.cantJuegos.config(text="0"), self.cantJuegosBuenos.config(text="0"), self.cantJuegosMalos.config(text="0")])
        self.botonNormal.grid(row=11, column=1, sticky=W+E, padx=(30,20))

        self.botonDificil= ttk.Radiobutton(self.window, text=" Difícil ", value=3,command= lambda:[self.dificult.append(3), self.dificultas(), self.cantJuegos.config(text="0"), self.cantJuegosBuenos.config(text="0"), self.cantJuegosMalos.config(text="0")])
        self.botonDificil.grid(row=11, column=2, sticky=W+E, padx=(10,0))




def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()