

""""En esta opción el usuario deberá ingresar por teclado el coeficiente principal
 y el término independiente. Se deberá mostrar por pantalla la siguiente información:
   corte con el eje x, corte con el eje y, comportamiento de la recta (creciente o decreciente).
"""



import random
import os
from fractions import Fraction
opcion = 0
valor_pendiente=0
valor_independiente=0
pendiente= ""
raiz= 0

valor_pendiente = Fraction(input("Ingrese el coeficiente principal, siendo aX + b, ingrese a \n: "))
valor_independiente = Fraction(input("Ingrese el termino independiente, siendo aX + b, ingrese b \n: "))

if (valor_pendiente>0):
    pendiente= "creciente"
else:
    (valor_pendiente<0)
    pendiente= "decreciente"

raiz= (valor_independiente * -1) / valor_pendiente

print("el corte en eje X es: " + str(raiz))
print("el corte en eje y es: " + str(valor_independiente))
print("pendiente: " + (pendiente))
