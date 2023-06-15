

def validacionMenu(msj,OpcionMin,OpcionMax):

    bandera=True

    while bandera == True:

        num=int(input(msj))
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


def validarCodProducto(msj, productos):
    validar= True
    Codcorrecto=False
    while validar==True:
        text="      Nombre       |        Marca        |        Precio         |        Stock        | "
        codProducto=input(msj)
        for i in productos:
            if codProducto==i:
                codigoValido=i
                Codcorrecto=True
        if Codcorrecto==True:

            print(f"""
                    {text}
Producto encontrado:     {productos[codigoValido]["Nombre"]}        {productos[codigoValido]["Marca"]}                 {productos[codigoValido]["Precio"]}                  {productos[codigoValido]["Stock"]}               
                  
                  """)
        else:
            print("Producto no encontrado. Ingrese nuevamente un código valido")

    return()


def SumaralCarro(msj):
    validar=True
    añadirCarro=False
    while validar==True:
        op=input(msj)
        if op ==1 or op==5:
            



