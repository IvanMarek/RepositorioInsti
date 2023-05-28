import os
from math import sqrt 

"""Ejercicio2:
Calculadora de Estadísticas de Números
Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos.
varianza (la sumatoria de todo los numeros menos el promedio. elevado al cuadrado. dividido la cantidad de numeros)
ejemplo (8- el promedio)**2 + (19-promedio)**2 todo dividido la cantidad de numeros
desviacion estandar es: la raiz cuadrada de la varianza"""


listaNum=[]
suma=0
promedio=0
cantidadNum=0

num=input("Ingrese una lista de numeros separados por espacios:  ")
listaNum= num.split()
print(listaNum)

for i in range(0,len(listaNum)):
    listaNum[i]=int(listaNum[i])

menor=listaNum[0]
mayor=listaNum[0]

for i in listaNum:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i
    cantidadNum+=1
    suma+=i
promedio= suma/cantidadNum

primerPasovarianza=0
varianza=0
listaVarianza=[]
sumaTerminosVarianza=0 
desviacion=0
for i in listaNum: #primer paso de la varianza (numero - porcentaje)**2
    primerPasovarianza= (i-promedio)**2
    listaVarianza.append(primerPasovarianza)
for k in listaVarianza: #segundo paso de la varianza (la sumatoria de todos los terminos del primer paso...)
    sumaTerminosVarianza+=k
varianza=sumaTerminosVarianza/cantidadNum #tercer paso de la varianza (el total del segundo paso dividido la cantidad de numeros de la lista ingresada por el usuario...)
desviacion= sqrt(varianza)

print(suma)

print(promedio)

print(f"""El numero mayor es: {mayor}

El numero menor es: {menor}
      """)
print(f""" {listaVarianza}

La suma de todos los terminos es: {sumaTerminosVarianza}

la varianza es: {varianza}

la deviacion es: {desviacion}
""")