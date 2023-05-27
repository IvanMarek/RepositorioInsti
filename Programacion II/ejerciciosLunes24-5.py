import os

"""Ejercicio2:
Calculadora de Estadísticas de Números
Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos."""



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

