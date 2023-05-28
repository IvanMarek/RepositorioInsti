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
listaNum= num.split() #genera una lista a partir de string separando los elementos por espacios.
print(listaNum)

for i in range(0,len(listaNum)): # recorre la lista y convierto los elementos en numeros enteros para poder operar con ellos...
    listaNum[i]=int(listaNum[i])

menor=listaNum[0]
mayor=listaNum[0]

for i in listaNum: #recorre la lista e identifica el numero mayor y menor
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i
    cantidadNum+=1
    suma+=i
promedio= suma/cantidadNum  #calcula el promedio de los numeros ingresados

primerPasovarianza=0
varianza=0
listaVarianza=[]
sumaTerminosVarianza=0 
desviacion=0
for i in listaNum: #primer paso de la varianza: calcular (numero - porcentaje)**2 y guardarlo en una lista para poder seguir calculando...
    primerPasovarianza= (i-promedio)**2
    listaVarianza.append(primerPasovarianza)
for k in listaVarianza:   #segundo paso de la varianza: (la sumatoria de todos los terminos del primer paso (que estan guardados en la lista)...) y guardarlos en una variable...
    sumaTerminosVarianza+=k
varianza=sumaTerminosVarianza/cantidadNum  #tercer paso de la varianza: (el total de la sumatoria dividido por la cantidad de numeros de la lista ingresada por el usuario...)
desviacion= sqrt(varianza)  # La desviacion es igual a la raiz cuadrada de la varianza...  podemos usar sqrt para resolver la raiz cuadrada o podemos... (el numero ** (1/2))

print(f"""

La suma de los numeros es igual a:  {suma}

El promedio de los numeros es:  {promedio}

El mayor de los numeros ingresados es:  {mayor}

El menor de los numeros ingresados es:  {menor}

La desviacion de los numeros es:  {desviacion}

""")



