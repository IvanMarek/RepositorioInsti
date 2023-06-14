

def validacionMenu(msj,OpcionMin,OpcionMax):

    bandera=True

    while bandera == True:

        num=input(msj)
        try:
            if num <= OpcionMax and num >= OpcionMin:
                bandera=False
                opcionCorrecta=num
            else:
                print("Opcion incorrecta, Ingrese una opción valida")
        except ValueError:
            print("Opcion incorrecta, Ingrese una opción valida")
            continue

    return(opcionCorrecta)


def validarCodProducto(msj, productos{} ):
    validar=True
    while validar==True:
        validar= True
        Codcorrecto=False
        codProducto=input(msj)

        for i in productos:
            if i==codProducto:
                Codcorrecto=True
        if Codcorrecto==True:

            print(f"""
                  Producto encontrado: {Nombre}
                  
                  """)








    return