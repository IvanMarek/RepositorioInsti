import random

def suma(a,b,c):
    suma=0
    suma= a+b+c
    return(suma)
print("Ejercicio Suma")
num1= int(input("primer numero: "))
num2= int(input("segundo numero: "))
num3= int(input("tercer numero: "))
resultado= suma(num1,num2,num3)
print(resultado)



def multi(a,b):
    multiplicacion= a*b
    return(multiplicacion)
print("Ejercicio Multiplicacion")
num4= int(input("ingresa num: "))
print(multi(resultado,num4))



def agenda(cliente):
    listaContacto=[]
    contacto=""
    cont=0
    while cont < cliente:  
        nombre= str(input("Ingresa un nombre: "))
        apellido= str(input("Ingres un apellido: "))
        numtel= int(input("Ingresa un Numero de telefono: "))  
        contacto= "El nombre del cliente es:   " +  nombre + " - " + " El apellido es:  " + apellido + " - " + "El numero de telefono es:  " + " - " + str(numtel)
        listaContacto.append(contacto)
        cont+=1
    return(listaContacto)
print("Ejercicio Agenda de Clientes")
cantidadClientes= int(input("Ingresar cantidad de clientes a agregar: "))
print(agenda(cantidadClientes))


def construirUnaMatriz(filas, columnas):
    print("Ejercicio Contrauir Matriz")
    mat=[]
    num=0
    suma=0
    msj=""
    for i in range(0,filas):
        mat.append([0]* columnas)
    for i in range(0,filas):
        for k in range (0,columnas):
            num=random.randint(10,50)
            mat[i][k]= num
            suma=suma+mat[i][k]
            msj=msj + " | " + str(mat[i][k])
        msj= msj + "\n"
    print(msj)

construirUnaMatriz(filas=int(input("Ingresa la cantidad de filas:  ")), columnas=int(input("ingresa la cantidad de columnas:  ")))

def mayorMenor(contador):
    
    num=0
    cont=0
    while cont<contador:
        num=int(input("Ingresa un numero:  "))
        if cont==0:
            max=num
            menor=num
        if num>max:
            max=num
        if num<menor:
            menor=num
        cont+=1
    print(f"""El numero maximo ingresado es:  {max} 
El numero minimo es:  {menor} """)
print("Ejercicio MayorMenor")    
mayorMenor(contador=int(input("Ingresa la cantidad de numeros que quieras verificar:  ")))
