

def usuarios():
    cantidadUsuarios=input("Ingresa la cantidad de usuarios  ")
    usuarios={}
    cont=0

    while cont < cantidadUsuarios:
        nombre=input("ingresar el nombre del usuario:  ")
        edad=input("ingresa la edad del usuario:  ")
        usuarios[nombre]=edad
        cont+=1
    

    nombreJoven=""
    edadJoven=0
    cont2=0
    
    for nombre,edad in usuarios.items():
        if cont2==0:
            edadJoven=edad
            nombreJoven=nombre
        if edad<edadJoven:
            edadJoven=edad
            nombreJoven=nombre
    print(f"El usuario mas joven es: {nombreJoven} ")
usuarios()   

    