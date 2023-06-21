import os

def imprimir_productos(productos):
    
   
    print("    Código  |        Nombre        |        Marca         |  Precio   |  Stock    |")
    print("-------------------------------------------------------------------------------")
    for codigo, detalles in productos.items():
        nombre = detalles["Nombre"]
        marca = detalles["Marca"]
        precio = detalles["Precio"]
        stock = detalles["Stock"]

        # Utilizamos la función format() para establecer el ancho fijo de cada columna
        print(" {:<10} |  {:<20}|  {:<20}| ${:<9}| {:<10}|".format(codigo, nombre, marca, precio, stock))


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
        text="    Código  |        Nombre        |        Marca         |  Precio   |  Stock    |"
        codProducto= input(msj).lower()
        for i in productos:
            if codProducto==i or codProducto==(productos[i]["Nombre"]).lower():
                codigoValido=i
                Codcorrecto=True
        if Codcorrecto==True:
            for codigo, detalles in productos.items():
                nombre = detalles["Nombre"]
                marca = detalles["Marca"]
                precio = detalles["Precio"]
                stock = detalles["Stock"]
            print(text)
            ("-------------------------------------------------------------------------------")
            print("    {:<7} |    {:<18}|    {:<18}| ${:<9}| {:<10}|".format(codigo, nombre, marca, precio, stock))
            break
        else:
            print("Producto no encontrado. Ingrese nuevamente un código valido")

    return(codigoValido)


def OpcionesSi_No(msj):
    validar=True
    while validar==True:
        op=input(msj)
        try:
            op=int(op)
            if op==1:
                Si=op
                return(Si)
            elif op==5:
                os.system("cls")
                No=op
                return(No)
            else:
                print("Opcion incorrecta, Ingrese una opción valida")
        except ValueError:
            print("Opcion incorrecta, Ingrese una opción valida")
    

"""       VolVier a hacer:

def SumaralCarro(msj, productos, codigoValido):
    validar=True
    añadirCarro=False
    cantidadProducto=0
    ProductosEnCarrito={}
    reducirStock=0
    while validar==True:
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
            #Mostrar carrito... (mostrar diccionario) y un subtotal general entre todos los productos....
        
    return(opcionValida)"""