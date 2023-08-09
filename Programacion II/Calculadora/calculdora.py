from fractions import *

def cantidadNumOperar(msj):
    while True:
        cant=input(msj)
        try:
            cant=int(cant)
            if cant < 10 and cant > 0:
                return(cant)
            elif cant > 10:
                print("\n No es posible calcular mas de 10 numero en esta calculadora \n\n ")
            elif cant <0 or cant ==0:
                print("\n La cantidad seleccionada no es valida \n\n")
        except ValueError:
            print("\n\nCantidad invalida, ingrese una cantidad valida \n\n")

def numsNotStr(msj):
    while True:
        num=input(msj)
        try:
            num=Fraction(num)
            return(num)
        except ValueError:
            print("El dato ingresado no es un numero")

def suma():
    cont=0
    numeros=[]
    resultado=0
    Cantidad=cantidadNumOperar("Ingrese la cantidad de números a sumar:  \n")
    while cont < Cantidad:
        num=numsNotStr("Ingrese un número:   \n")
        numeros.append(num)
        cont+=1
    for i in numeros:
        resultado += i
    print("El resultado de la suma de los números dados es:  " + str(resultado))
sumar=suma()

def resta():
    cont=0
    numeros=[]
    resultado=0
    Cantidad=cantidadNumOperar("Ingrese la cantidad de números a restar:  \n")
    while cont < Cantidad:
        num=numsNotStr("Ingrese un número:   \n")
        numeros.append(num)
        cont+=1
    for i in numeros:
        resultado -= i
    print("El resultado de la resta de los números dados es:  " + str(resultado))
restar=resta()

def multiplicacion():
    cont=0
    numeros=[]
    Cantidad=cantidadNumOperar("Ingrese la cantidad de números a multiplicar:  \n")
    while cont < Cantidad:
        num=numsNotStr("Ingrese un número:   \n")
        numeros.append(num)
        cont+=1
    while len(numeros)>1:
        resultado = numeros[0] * numeros[1]
        numeros[0]= resultado
        numeros.pop(1)

    print("El resultado de la multiplicación de los números dados es:  " + str(resultado))
multiplicar=multiplicacion()

def division():
    cont=0
    decimales= 2
    numeros=[]
    Cantidad=cantidadNumOperar("Ingrese la cantidad de números a dividir:  \n")
    while cont < Cantidad:
        num=numsNotStr("Ingrese un número:   \n")
        if num != 0:
            numeros.append(num)
            cont+=1
        else:
            print("Los numeros ingresado no pueden ser 0  \n")
    while len(numeros)>1:
            if numeros[1] > 0 or numeros[1] < 0:
                resultado = numeros[0] / numeros[1]
                numeros[0]= resultado
                numeros.pop(1)

    resultadoDecimal= float(resultado)

    print("\n  El resultado (redondeado) de la división de los números dados es:  " + str(round(resultado, decimales))+ "\n" )
    print("\n  El resultado (Decimales) de la división de los números dados es:  " + str(resultadoDecimal)+ "\n" )
    print("\n  El resultado (fracción) de la división de los números dados es:  " + str(resultado)+ "\n" )
dividir=division()

def potenciacion():
    num=numsNotStr("\n Ingrese un número:   \n")
    num2=numsNotStr("Ingrese el exponente de la potencia:   \n")
    poten= num**num2

    print("El resultado de la potenciación de los números dados es:  " + str(poten))
potenciciación=potenciacion()

def radicacion():
    decimales= 2
    while True:
        num=numsNotStr("\n Ingrese un número:   \n")
        num2=numsNotStr("Ingrese un número como indice de la raíz:   \n")
        if num < 0 and num2 % 2 != 0:
            raiz= num**(1/num2)
            redondeo=(raiz)
            print("El resultado de la  de los números dados es:  " + str(redondeo))
            break
        if num < 0 and num2 %2 == 0:
            print("No es posible realizar raíces pares en numero negativos... por ejemplo: 2 √-16 ")
        if num2 >1:
            raiz= num**(1/num2)
            cadena_formato = "El resultado de la  de los números dados es:  {:.{}f}".format(raiz, decimales)
            print(cadena_formato)
            break
        else:
            print(" No es posible calcular, se calculan raíces cuadradas en adelante")
Radicación=radicacion()

def porcentaje():
    num=numsNotStr("\n Ingrese un número:   \n")
    num2=numsNotStr("Ingrese el porcentaje a aplicar:   \n")
    porcen= num*num2/100
    print("El porcentaje es:  " +  str(porcen))

porciento=porcentaje()