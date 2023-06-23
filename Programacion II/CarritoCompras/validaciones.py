import os

def imprimir_productos(productos):
    
   
    print("{:^10}|{:^20}|{:^20}|{:^9}|{:^10}|".format("Codigo","Nombre", "Marca", "Precio", "Stock"))
    print("-------------------------------------------------------------------------------")
    for codigo, detalles in productos.items():
        nombre = detalles["Nombre"]
        marca = detalles["Marca"]
        precio = detalles["Precio"]
        stock = detalles["Stock"]

        # Utilizamos la función format() para establecer el ancho fijo de cada columna
        print("{:^10}|{:^20}|{:^20}|{:^9}|{:^10}|".format(codigo, nombre, marca, "$"+str(precio), stock))


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
        text=("|{:^20}|{:^20}|{:^10}|{:^10}|".format( "Nombre", "Marca", "Precio", "Stock"))
        codProducto= input(msj).lower()
        for i in productos:
            if codProducto==i or codProducto==(productos[i]["Nombre"]).lower():
                codigoValido=i
                Codcorrecto=True
        if Codcorrecto==True:
            for codigo, detalles in productos.items():
                if codigo == codigoValido:
                    nombre = detalles["Nombre"]
                    marca = detalles["Marca"]
                    precio = detalles["Precio"]
                    stock = detalles["Stock"]
            print(text)
            print("-----------------------------------------------------------------")
            print("|{:^20}|{:^20}|{:^10}|{:^10}|".format( nombre, marca, "$"+str(precio), stock))
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
    
def validarStock(msj,productos,codigoProduct):
    cantidad=True
    while cantidad==True:
        cantidadProducto=input(msj)
        try:
            cantidadProducto=int(cantidadProducto)
            if cantidadProducto <= productos[codigoProduct]["Stock"]:
                reducirStock= productos[codigoProduct]["Stock"] - cantidadProducto
                productos[codigoProduct]["Stock"]= reducirStock
                print(f"""
                Muestra la reduccion del stock en el diccionario...

                {productos[codigoProduct]}
                
                """)
                break
            elif cantidadProducto > productos[codigoProduct]["Stock"] and productos[codigoProduct]["Stock"] !=0:
                print(f"""
                No contamos con la cantidad indicada, 
                Contamos con {productos[codigoProduct]["Stock"]} Unidad\es del producto {productos[codigoProduct]["Nombre"]},
                """)
            else:
                print("          Producto sin stock         ")
                break
        except ValueError:
            print("Cantidad invalida, Ingrese una cantidad valida")

    return(cantidadProducto)
