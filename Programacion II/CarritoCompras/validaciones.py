

def validacionMenu(msj,OpcionMin,OpcionMax):

    bandera=True

    while bandera == True:

        num=input(msj)
        try:
            num = int(num)
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
            if codProducto==i or codProducto==productos[i]["Nombre"]:
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


def SumaralCarro(msj, productos):
    validar=True
    añadirCarro=False
    ProductosEnCarrito={}
    while validar==True:
        op=input(msj)
        try:
            if op ==1:
                añadirCarro=True
                #seleccionar cantidad de productos...
                #cargar producto a un nuevo diccionario llamado carro...
                #que guarde nombre  cantidad  precioUnitario Subtotal...
                #Preguntar¿? Desea seguir añadiendo productos? si-no? (si) volver a busqueda de productos... (NO) desea realizar compra?...
                #Si desea realizar compra enviar a ver carrito...
            if op==5:
                #limpiar pantalla y devolver al menu principal...
                pass
        except ValueError:
            pass
            


