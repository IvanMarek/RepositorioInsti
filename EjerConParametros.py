import random

def suma(a,b,c):
  suma=0
  suma= a+b+c
  return(suma)

num1= int(input("primer numero: "))
num2= int(input("segundo numero: "))
num3= int(input("tercer numero: "))
resultado= suma(num1,num2,num3)
print(resultado)



def multi(a,b):
    multiplicacion= a*b
    return(multiplicacion)
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
cantidadClientes= int(input("Ingresar cantidad de clientes a agregar: "))
print(agenda(cantidadClientes))


def construirUnaMatriz(filas, columnas):
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

construirUnaMatriz(5,5)

def matrizConAgenda(filas,columnas,cantClientes):
    




matrizConAgenda(5,5,3)
