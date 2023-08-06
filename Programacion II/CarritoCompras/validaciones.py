import os

def imprimir_productos(productos):
    
    print("+-------------------------------------------------------------------------+")
    print("|{:^10}|{:^20}|{:^20}|{:^9}|{:^10}|".format("Código","Nombre", "Marca", "Precio", "Stock"))
    print("|-------------------------------------------------------------------------|")
    for codigo, detalles in productos.items():
        nombre = detalles["Nombre"]
        marca = detalles["Marca"]
        precio = detalles["Precio"]
        stock = detalles["Stock"]

        # Utilizamos la función format() para establecer el ancho fijo de cada columna
        print("|{:^10}|{:^20}|{:^20}|{:^9}|{:^10}|".format(codigo, nombre, marca, "$"+str(precio), stock))
    print("+-------------------------------------------------------------------------+")


def validacionMenu(msj,OpcionMin,OpcionMax): #funcion muy util..... posible uso siempre....

    bandera=True

    while bandera == True:

        num=input(msj)
        try:
            num = int(num)
            if num <= OpcionMax and num >= OpcionMin:
                bandera=False
                opcionCorrecta=num
            else:
                print("Opción incorrecta, Ingrese una opción valida")
        except ValueError:
            print("Opción incorrecta, Ingrese una opción valida")
        continue

    return(opcionCorrecta)


def validarCodProducto(msj, productos):
    Codcorrecto=False
    while True:
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
            print("-----------------------------------------------------------------")
            print(text)
            print("-----------------------------------------------------------------")
            print("|{:^20}|{:^20}|{:^10}|{:^10}|".format( nombre, marca, "$"+str(precio), stock))
            print("-----------------------------------------------------------------")
            break
        else:
            print("Producto no encontrado. Ingrese nuevamente un código válido")

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
                print("Opción incorrecta, Ingrese una opción válida")
        except ValueError:
            print("Opción incorrecta, Ingrese una opción válida")
    
def validarStock(msj,productos,codigoProduct):
    cantidad=True
    while cantidad==True:
        cantidadProducto=input(msj)
        try:
            cantidadProducto=int(cantidadProducto)
            if cantidadProducto <= productos[codigoProduct]["Stock"] and cantidadProducto > 0:
                reducirStock= productos[codigoProduct]["Stock"] - cantidadProducto
                productos[codigoProduct]["Stock"]= reducirStock
                return(cantidadProducto)
            elif cantidadProducto > productos[codigoProduct]["Stock"] and productos[codigoProduct]["Stock"] !=0:
                print(f"""
                No contamos con la cantidad indicada, 
                Contamos con {productos[codigoProduct]["Stock"]} Unidad\es del producto {productos[codigoProduct]["Nombre"]},
                """)
            elif cantidadProducto < 0 or cantidadProducto == 0:
                print("Cantidad inválida, Ingrese una cantidad válida")
            else:
                print("          Producto sin stock         ")
                return(False)

        except ValueError:
            print("Cantidad inválida, Ingrese una cantidad válida")

def mostrarCarrito(carrito):
    if len(carrito)>0:
        total=0
        print("{:^80}".format("TU CARRO DE LA COMPRAS"))
        texto=("|{:^30}|{:^30}|{:^20}|{:^15}|{:^15}|".format( "Nombre", "Marca", "Precio x Unidad", "Cantidad","Subtotal"))
        print("--------------------------------------------------------------------------------------------------------------------")
        print(texto)
        print("--------------------------------------------------------------------------------------------------------------------")
        for codigo,detalles in carrito.items():
            nombre = detalles["Nombre"]
            marca = detalles["Marca"]
            precio = detalles["Precio"]
            cantidad = detalles["CantidadCompra"]
            subtotal = detalles["Subtotal"]
            total+=subtotal
            print("|{:^30}|{:^30}|{:^20}|{:^15}|{:^15}|".format( nombre, marca, "$"+str(precio), cantidad, "$"+str(subtotal)))
        print("""--------------------------------------------------------------------------------------------------------------------""")
        print("|{:>114}|".format("$"+str(total)))
        print("--------------------------------------------------------------------------------------------------------------------")
    else:
        print("\n\n\n         Su carro de compras esta vacío...  \n\n\n")
        return(False)
   


def validarCodigoProducto(msj, carrito):
    Codigocorrecto=False
    while True:
        texto=("|{:^30}|{:^30}|{:^20}|{:^15}|{:^15}|".format( "Nombre", "Marca", "Precio x Unidad", "Cantidad","Subtotal"))
        codProducto= input(msj).lower()
        for i in carrito:
            if codProducto==i or codProducto==(carrito[i]["Nombre"]).lower():
                codigoValido=i
                Codigocorrecto=True
        if Codigocorrecto==True:
            for codigo, detalles in carrito.items():
                if codigo == codigoValido:
                    nombre = detalles["Nombre"]
                    marca = detalles["Marca"]
                    precio = detalles["Precio"]
                    cantidad = detalles["CantidadCompra"]
                    subtotal = detalles["Subtotal"]
            print("{:^80}".format("El producto:  "))
            print("--------------------------------------------------------------------------------------------------------------------")
            print(texto)
            print("--------------------------------------------------------------------------------------------------------------------")
            print("|{:^30}|{:^30}|{:^20}|{:^15}|{:^15}|".format( nombre, marca, "$"+str(precio), cantidad, "$"+str(subtotal)))
            print("""--------------------------------------------------------------------------------------------------------------------""")
            return(codProducto)
        else:
            print("Producto no encontrado. Ingrese nuevamente un código válido")


def validarCantidad(msj,carrito, codigoProduct,productos):
    while True:
        cantidad=input(msj)
        try:
            cantidad=int(cantidad)
            if cantidad < carrito[codigoProduct]["CantidadCompra"] and cantidad > 0:
                carrito[codigoProduct]["CantidadCompra"] -= cantidad
                productos[codigoProduct]["Stock"] += cantidad
                reducirSubtotal= carrito[codigoProduct]["Precio"]*cantidad
                carrito[codigoProduct]["Subtotal"]-=reducirSubtotal
                break
            elif cantidad > carrito[codigoProduct]["CantidadCompra"] and carrito[codigoProduct]["CantidadCompra"] !=0:
                print(f"""
                No puede modificar esa cantidad de producto, 
                Tiene en el carro {carrito[codigoProduct]["CantidadCompra"]} Unidad\es del producto {carrito[codigoProduct]["Nombre"]},
                """)
            elif cantidad == carrito[codigoProduct]["CantidadCompra"]:
                modificarEliminar= OpcionesSi_No("Desea eliminar el producto?  (1-SI,5-NO) \n:  ")
                if modificarEliminar==1:
                    eliminar=eliminarProductoCarro(carrito,codigoProduct,productos)
                    break
                if modificarEliminar==5:
                    os.system("cls")
                    pass
                    continuar=input("""
                            Presionar enter para volver al menú principal
                        """)
            elif cantidad <= 0:
                print("Cantidad inválida, Ingrese una cantidad válida")
                
        except ValueError:
            print("Cantidad inválida, Ingrese una cantidad válida")
    return(cantidad)


def eliminarProductoCarro(carrito, codigoProductEliminar, productos):
    while True:
        cantidadRetorno=carrito[codigoProductEliminar]["CantidadCompra"]
        productos[codigoProductEliminar]["Stock"]+= cantidadRetorno
        del carrito[codigoProductEliminar]
        print("El producto fue eliminado correctamente de su carro")
        break

    
def finalizarCompra(carrito):
    carrito.clear()
