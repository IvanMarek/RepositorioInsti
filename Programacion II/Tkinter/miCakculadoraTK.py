from tkinter import *


pantalla = Tk()


entrada= Entry (pantalla, font=("Arial", 20), relief=GROOVE, justify=RIGHT, bg= "#e9abb1")
entrada.grid(row=0, column=1, columnspan=5, sticky="nsew")
#Botones numéricos
boton1=Button(pantalla, text="1").grid(column=1, row=5, sticky=W+E)
boton2=Button(pantalla, text="2").grid(column=2, row=5, sticky=W+E)
boton3=Button(pantalla, text="3").grid(column=3, row=5, sticky=W+E)
boton4=Button(pantalla, text="4").grid(column=1, row=4, sticky=W+E)
boton5=Button(pantalla, text="5").grid(column=2, row=4, sticky=W+E)
boton6=Button(pantalla, text="6").grid(column=3, row=4, sticky=W+E)
boton7=Button(pantalla, text="7").grid(column=1, row=3, sticky=W+E)
boton8=Button(pantalla, text="8").grid(column=2, row=3, sticky=W+E)
boton9=Button(pantalla, text="9").grid(column=3, row=3, sticky=W+E)
boton0=Button(pantalla, text="0").grid(column=1, row=6, sticky=W+E)


#Botones especiales

botonComa=Button(pantalla, text=".").grid(column=2, row=6, sticky=W+E)
botonDel=Button(pantalla, text="⇦").grid(column=3, row=6, sticky=W+E)
botonAC=Button(pantalla, text="AC").grid(column=1, row=2, sticky=W+E)
botonParen2=Button(pantalla, text="(").grid(column=2, row=2, sticky=W+E)
botonParen2=Button(pantalla, text=")").grid(column=3, row=2, sticky=W+E)

#botones operaciones
botonsuma=Button(pantalla, text="+").grid(column=4, row=5, sticky=W+E)
botonresta=Button(pantalla, text="-").grid(column=4, row=4, sticky=W+E)
botonmult=Button(pantalla, text="*").grid(column=4, row=3, sticky=W+E)
botondiv=Button(pantalla, text="/").grid(column=4, row=2, sticky=W+E)
"""botonpor=Button(pantalla, text="%").grid(column=4, row=, sticky=W+E)"""
botonigual=Button(pantalla, text="=").grid(column=4, row=6, sticky=W+E)
"""botonParen2=Button(pantalla, text=")").grid(column=3, row=2, sticky=W+E)"""
pantalla.mainloop()