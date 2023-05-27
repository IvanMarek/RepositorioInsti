
def usuarios (Nombre,Edad):
    usuario= {
     "Nombre: " "" ,
     "Edad: " "",
    }
    menor=0
    for nombre,edad in usuarios:
        if Edad[edad] == 0:
            menor=Edad[edad]
            Nombre=nombre
        if Edad[edad]< menor:
            menor=Edad[edad]
            Nombre=nombre
    print(f"El menor es: {Nombre} ")
    return menor

Nombre=(input("Ingrese el nombre de la persona:  "))
Edad=(input("Ingresa la edad de la persona:  "))
 
resultado= usuarios(Nombre,Edad)
print(resultado)