from tkinter import *




def parent():



    return

pantalla = Tk()
pantalla.title("Calculadora")

entrada= Entry (pantalla, font=("Arial", 20), relief=GROOVE, justify=RIGHT, bg= "#1a364e", fg="black")
entrada.grid(row=0, column=1, columnspan=5, sticky="nsew")
#Botones numéricos
boton1=Button(pantalla, text="1", bg= "#333b3d").grid(column=1, row=5, sticky="nsew")
boton2=Button(pantalla, text="2", bg= "#333b3d").grid(column=2, row=5, sticky="nsew")
boton3=Button(pantalla, text="3", bg= "#333b3d").grid(column=3, row=5, sticky="nsew")
boton4=Button(pantalla, text="4", bg= "#333b3d").grid(column=1, row=4, sticky="nsew")
boton5=Button(pantalla, text="5", bg= "#333b3d").grid(column=2, row=4, sticky="nsew")
boton6=Button(pantalla, text="6", bg= "#333b3d").grid(column=3, row=4, sticky="nsew")
boton7=Button(pantalla, text="7", bg= "#333b3d").grid(column=1, row=3, sticky="nsew")
boton8=Button(pantalla, text="8", bg= "#333b3d").grid(column=2, row=3, sticky="nsew")
boton9=Button(pantalla, text="9", bg= "#333b3d").grid(column=3, row=3, sticky="nsew")
boton0=Button(pantalla, text="0", bg= "#333b3d").grid(column=1, row=6, sticky="nsew")


#Botones especiales

botonComa=Button(pantalla, text=".", bg= "#333b3d").grid(column=2, row=6, sticky="nsew")
botonDel=Button(pantalla, text="⇦", bg= "#333b3d").grid(column=3, row=6, sticky="nsew")
botonAC=Button(pantalla, text="AC", bg= "#333b3d").grid(column=1, row=2, sticky="nsew")
botonParen2=Button(pantalla, text="(", bg= "#333b3d").grid(column=2, row=2, sticky="nsew")
botonParen2=Button(pantalla, text=")", bg= "#333b3d").grid(column=3, row=2, sticky="nsew")

#botones operaciones
botonsuma=Button(pantalla, text="+", bg= "#333b3d").grid(column=4, row=5, sticky="nsew")
botonresta=Button(pantalla, text="-", bg= "#333b3d").grid(column=4, row=4, sticky="nsew")
botonmult=Button(pantalla, text="*", bg= "#333b3d").grid(column=4, row=3, sticky="nsew")
botondiv=Button(pantalla, text="/", bg= "#333b3d").grid(column=4, row=2, sticky="nsew")
botonigual=Button(pantalla, text="=", bg= "#333b3d").grid(column=4, row=6, sticky="nsew")

pantalla.mainloop()



