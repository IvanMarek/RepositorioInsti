def validarCodProducto(msj, productos):
    validar= True
    Codcorrecto=False
    while validar==True:
        
        codProducto=input(msj)
        for i in productos:
            if codProducto==i or codProducto==productos[i]["Nombre"]:
                codigoValido=i
                Codcorrecto=True
        else:
            print("Producto no encontrado. Ingrese nuevamente un código valido")

    return(codigoValido, Codcorrecto)


text="      Nombre       |        Marca        |        Precio         |        Stock        | "

        if Codcorrecto==True:

            print(f"""
                    {text}
Producto encontrado:     {productos[codigoValido]["Nombre"]}        {productos[codigoValido]["Marca"]}                 {productos[codigoValido]["Precio"]}                  {productos[codigoValido]["Stock"]}               
                  
                  """)


            

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

    return(codigoValido, Codcorrecto)


def SumaralCarro(msj, productos, codigoValido):
    validar=True
    añadirCarro=False
    cantidadProducto=0
    ProductosEnCarrito={}
    reducirStock=0
    while validar==True:
        op=input(msj)
        try:
            op= int(op)
            if op ==1:
                añadirCarro=True
                opcionValida=op
            
            if añadirCarro == True:
                cantidadProducto=int(input("    Ingresar la cantidad del producto que desea:   "))
                for i in productos:
                    if cantidadProducto <= productos[i]["Stock"]:
                        reducirStock= productos[i]["Stock"] - cantidadProducto
                        productos[i]["Stock"]= reducirStock
                #seleccionar cantidad de productos...
                #cargar producto a un nuevo diccionario llamado carro...
                #que guarde nombre  cantidad  precioUnitario Subtotal...
                #Preguntar¿? Desea seguir añadiendo productos? si-no? (si) volver a busqueda de productos... (NO) desea realizar compra?...
                #Si desea realizar compra enviar a ver carrito...
            if op==5:
                os.system("cls")
                break

                #limpiar pantalla y devolver al menu principal...
                pass
        except ValueError:
            print("Opcion incorrecta, Ingrese una opción valida")

    return(opcionValida)
            
