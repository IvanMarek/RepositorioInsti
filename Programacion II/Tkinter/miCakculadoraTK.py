from tkinter import *
from tkinter import ttk
class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora")
        self.window.resizable(0,0)
        self.window.geometry("300x330")
        self.createWidgets()
        self.window.mainloop()


    def parent():



        return


    def createWidgets(self):
        entrada= Entry (self.window, font=("Arial", 20), relief=GROOVE, justify=RIGHT, bg= "#1a364e", fg="black")
        entrada.grid(row=0, column=1, columnspan=5, rowspan=5, sticky=W+E)
        #Botones numéricos

        boton1=Button(self.window, text="1", bg= "#333b3d", width=3, height=3)
        boton1.grid(column=1, row=9, sticky="nsew")

        boton2=Button(self.window, text="2", bg= "#333b3d")
        boton2.grid(column=2, row=9, sticky="nsew")

        boton3=Button(self.window, text="3", bg= "#333b3d")
        boton3.grid(column=3, row=9, rowspan=2, sticky="nsew")

        boton4=Button(self.window, text="4", bg= "#333b3d")
        boton4.grid(column=1, row=7, rowspan=2, sticky="nsew")

        boton5=Button(self.window, text="5", bg= "#333b3d")
        boton5.grid(column=2, row=7, rowspan=2, sticky="nsew")

        boton6=Button(self.window, text="6", bg= "#333b3d")
        boton6.grid(column=3, row=7, rowspan=2, sticky="nsew")

        boton7=Button(self.window, text="7", bg= "#333b3d")
        boton7.grid(column=1, row=5, rowspan=2, sticky="nsew")

        boton8=Button(self.window, text="8", bg= "#333b3d")
        boton8.grid(column=2, row=5, rowspan=2, sticky="nsew")

        boton9=Button(self.window, text="9", bg= "#333b3d")
        boton9.grid(column=3, row=5, rowspan=2, sticky="nsew")

        boton0=Button(self.window, text="0", bg= "#333b3d")
        boton0.grid(column=1, row=11, rowspan=2, sticky="nsew")


        #Botones especiales

        botonComa=Button(self.window, text=".", bg= "#333b3d")
        botonComa.grid(column=2, row=11, rowspan=2, sticky="nsew")

        botonDel=Button(self.window, text="⇦", bg= "#333b3d")
        botonDel.grid(column=3, row=11, rowspan=2, sticky="nsew")

        botonAC=Button(self.window, text="AC", bg= "#333b3d")
        botonAC.grid(column=1, row=3, rowspan=2, sticky="nsew")

        botonParen1=Button(self.window, text="(", bg= "#333b3d")
        botonParen1.grid(column=2, row=3, rowspan=2, sticky="nsew")

        botonParen2=Button(self.window, text=")", bg= "#333b3d")
        botonParen2.grid(column=3, row=3, rowspan=2, sticky="nsew")

        #botones operaciones
        botonsuma=Button(self.window, text="+", bg= "#333b3d")
        botonsuma.grid(column=4, row=11, rowspan=2, sticky="nsew")

        botonresta=Button(self.window, text="-", bg= "#333b3d")
        botonresta.grid(column=4, row=9, rowspan=2, sticky="nsew")

        botonmult=Button(self.window, text="*", bg= "#333b3d")
        botonmult.grid(column=4, row=7, rowspan=2, sticky="nsew")

        botondiv=Button(self.window, text="/", bg= "#333b3d")
        botondiv.grid(column=4, row=5, rowspan=2, sticky="nsew")

        botonporcen=Button(self.window, text="%", bg= "#333b3d")
        botonporcen.grid(column=4, row=3, rowspan=2, sticky="nsew")

        botonpotencia=Button(self.window, text="^", bg= "#333b3d")
        botonpotencia.grid(column=5, row=5, rowspan=2, sticky="nsew")

        botonraiz=Button(self.window, text="√", bg= "#333b3d")
        botonraiz.grid(column=5, row=3, rowspan=2, sticky="nsew")

        botonigual=Button(self.window, text="=", bg= "#333b3d")
        botonigual.grid(column=5, row=7, sticky="nsew", rowspan=6)


def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()
