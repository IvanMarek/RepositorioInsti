""""Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de
error.
El programa termina cuando el usuario introduce un cero."""

meses=("","enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto","septiembre", "octubre" ,"noviembre", "diciembre")
num=1
while num != 0: 
    num= int(input("Escriba un numero:  "))
    if num > 12:
        print("Error Solo hay 12 meses en un año")
    for i in meses:
        if meses.index[i] == (num):
            print[i]
print("Fin del programa")    



"""EJERCICIO 2

Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
repite según lo halle en la tupla que has creado.

RESUELVE validar los ingresos del usuario."""

numeros=(1,5,6,9,9,9,4,2,4,6,3,1,7,8,7,8,10,10,9)
while 1:
    num=int(input("Ingresa un numero entre 1 y 10:  "))
    if num < 1 or (num > 10):
        print("Parametros fuera de tupla")
    else:
        print(numeros.count(num))



"""EJERCICIO 3

Crea una tupla con números e indica el numero con mayor valor y el que menor tenga."""

numeros=(1,5,6,9,4,2,3,7,8,10,23,21,-40,39,50,200)
mayor=0
menor=0
for i in range(0,len(numeros)):
    if i==0:
        max=numeros[i]
        menor=numeros[i]
    if numeros[i]>max:
        max=numeros[i]
    if numeros[i]<menor:
        menor=numeros[i]
print("El numero maximo ingresado es:  " + str(max) + "  -  " + "El numero minimo ingresado es:  "+ str(menor))




"""EJERCICIO 4

Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y
muestra los valores de la tupla.

RESUELVE el caso en que no exista ese índice en la tupla."""


tupla=(1,2,3,4,5,6,7,8,9,10)

while 1: 
    indice=int(input("Ingres un indice del 1 al 10:  "))
    if indice<0 or (indice>9):
        print("indice fuera de parametros")
    else:
        print(tupla[indice])

