

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


def validarCodProducto(msj, productos ):
    validar= True
    Codcorrecto=False
    while validar==True:
        codProducto=input(msj)
        for i in productos:
            if codProducto==i:
                codigoValido=i
                Codcorrecto=True
        if Codcorrecto==True:

            print(f"""
                
                Producto encontrado: {productos[codigoValido]["Nombre"]}
                  
                  """)
        else:
            print("Producto no encontrado. Ingrese nuevamente un código valido")

    return()