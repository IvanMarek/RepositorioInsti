import random
import os
from fractions import Fraction
from math import sqrt
opcion = 0
valor_pendiente=0
valor_lineal=0
valor_ordenada=0
pendiente = ""
raiz = 0
delta=0
tipo_raiz=0
vertice_x=0
vertice_y=0
intervalo_crecimiento = ""
intervalo_decrecimiento = ""
b=0

raices = []


#Ejercicio 3


valor_pendiente = Fraction(input("Ingrese el coheficiente principal. Siendo ax2 + bx + c ingrese el valor de a \n :"))
valor_lineal = Fraction(input("Ingrese el termino lineal. Siendo ax2 + bx + c ingrese el valor de b \n :"))
valor_ordenada = Fraction(input("Ingrese el termino independiente. Siendo ax2 + bx + c ingrese el valor de c \n :"))

if(valor_pendiente>0):
    pendiente = 1
else:
    pendiente = -1

try:
    delta = sqrt(valor_lineal**2 - 4 * valor_pendiente * valor_ordenada)
except ValueError:
    b = 1


if(b==0):

    raiz = ((valor_lineal * (-1)) + delta) / (2 * valor_pendiente)

    raices.append(raiz)

    raiz = ((valor_lineal * (-1)) - delta) / (2 * valor_pendiente)

    raices.append(raiz)

if(delta<0):
    tipo_raiz = 1 #no tiene raices reales
elif(delta==0):
    tipo_raiz = 2 #raices dobles
elif(delta>0):
    tipo_raiz = 3 #raices multi 

vertice_x = (valor_lineal * -1) / (2 * valor_pendiente)

vertice_y = valor_pendiente * vertice_x ** 2 + valor_lineal * vertice_x + valor_ordenada


if(pendiente==1):
    intervalo_decrecimiento = "(-∞, " + str(vertice_x) + ")"  
    intervalo_crecimiento = "(" + str(vertice_x) + ", +∞)"
    print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
    print("El intervalo de crecimiento es " + intervalo_crecimiento)
    if( b==0):
        print("Las raices son: " + "x ="+ str(Fraction(raices[0])) + "   x2 ="+ str(Fraction (raices [1])))
    else:
        print("no tiene raices")
    print("El vertice X es: " + str(vertice_x))
    print("El vertice y es: " + str(vertice_y))
elif(pendiente==-1):
    intervalo_crecimiento = "(-∞, " + str(vertice_x) + ")"  
    intervalo_decrecimiento = "(" + str(vertice_x) + ", +∞)"
    print("El intervalo de crecimiento es " + intervalo_crecimiento)
    print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
    if( b==0):
        print("Las raices son: " + "x ="+ str(Fraction(raices[0])) + "   x2 ="+ str(Fraction (raices [1])))
    else:
        print("no tiene raices")
    print("El vertice X es: " + str(vertice_x))
    print("El vertice y es: " + str(vertice_y))
    #hola q hace
