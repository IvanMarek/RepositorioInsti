import os
from validaciones import validacionMenu
from validaciones import validarCodProducto
from validaciones import imprimir_productos
from validaciones import OpcionesSi_No
from validaciones import validarStock
from validaciones import mostrarCarrito
from validaciones import validarCodigoProducto
from validaciones import validarCantidad
from validaciones import eliminiarProductoCarro

carrito={}
subTotal=0

productos={
    "2462":{"Nombre": "Salame fino", "Marca": "Trimoleti", "Precio": 1300.86, "Stock": 11},
    "2466":{"Nombre":"Salame grueso" , "Marca": "Trimoleti", "Precio": 1500.46,"Stock": 9},
    "2351":{"Nombre":"Queso barra", "Marca":"La Paulina","Precio":1800.60, "Stock": 15},
    "2353":{"Nombre":"Queso cremoso", "Marca":"Del Bueno" ,"Precio":2000 ,"Stock":12 },
    "2236":{"Nombre":"Mortadela", "Marca":"Paladini" ,"Precio":1600.25 ,"Stock":20},    
    "1961":{"Nombre":"Jamon" ,"Marca": "Recreo","Precio":1700, "Stock": 9 },
    "1963":{"Nombre":"Jamon crudo", "Marca":"Piamontesa" , "Precio": 2100, "Stock":10 },
    "1965":{"Nombre":"Jamon cocido", "Marca":"Tres Cruces" , "Precio": 2200 , "Stock": 14}    
           }


while True:
    MostrarProductos=imprimir_productos(productos)
    continuar=input("""
                    Presiones enter para ingresar al menú     
    """)
        
    print("""
        1. Buscar producto por código o nombre
        2. Ver carrito
        3. salir
        """)

    opciones= validacionMenu(":    ",1,3)


    if opciones ==1:
        print("\n     Buscar producto por código o nombre:         \n")
        codigoProduct= validarCodProducto("""
    :   """, productos )
        
        print("\nDesea añadir el producto al carro?. (1-SI,5-NO)\n")
        op=OpcionesSi_No(":   ")

        if op==1:
            cantidadProducto=validarStock("\nIngrese la cantidad del producto que desea:\n",productos,codigoProduct)
            while True:
                if codigoProduct in carrito:
                    carrito[codigoProduct]["CantidadCompra"]+= cantidadProducto
                    carrito[codigoProduct]["Subtotal"]+= cantidadProducto * productos[codigoProduct]["Precio"]
                else:
                    carrito[codigoProduct]={"Nombre" : productos[codigoProduct]["Nombre"],"Marca":productos[codigoProduct]["Marca"] ,"CantidadCompra" : cantidadProducto,"Precio" : productos[codigoProduct]["Precio"],"Subtotal" : cantidadProducto * productos[codigoProduct]["Precio"]}
                
                print(f"""
                    Muestra el producto guardado en el nuevo diccionario de carrito y la cantidad del mismo q compro el cliente...

                    {carrito}

                    """)
                break
            #os.system("cls")
            print("\n               Perfecto, su producto fue añadido al carro con éxito")
        if op==5:
            os.system("cls")
            break
            
        continuar=input("""
                        Presionar enter para continuar     
                  """)
    if opciones==2:
        mostrarCarrito(carrito)
        
        print("""
1. Modificar cantidad de un producto
2. Eliminar producto del carro de compras
3. Finalizar compra
4. Regresar al menu principal
""")
        opciones= validacionMenu(":    ",1,3)

        if opciones==1:
            print("\nIngrese el codigo o nombre del producto que desea modificar la cantidad\n")
            codigoProduct= validarCodigoProducto(" :   ", carrito)
            print(carrito[codigoProduct])

            op=OpcionesSi_No("Realmente desea modificiar  de este producto?   (1-SI,5-NO) \n:  ")
            if op==1:
                cantidad_actualizada=validarCantidad("Ingresar la cantidad de producto que desea modificar(recuerde que esta opción es para reducir la cantidad del producto seleccionado):\n:     ", carrito, codigoProduct, productos)
                print(f"""
                    Muestra la reduccion del stock en el diccionario...

                    {carrito[codigoProduct]}
                    
                    """)
            if op==5:
                os.system("cls")
                break
        if opciones==2:
            print("\nIngrese el codigo o nombre del producto que desea eliminar:\n")
            codigoProduct= validarCodigoProducto(" :   ", carrito)
            print(carrito[codigoProduct])
            op=OpcionesSi_No("Realmente desea eliminar este producto?   \n(1-SI,5-NO) \n:  ")
            if op==1:
                eliminar=eliminiarProductoCarro(carrito,codigoProduct,productos)
                carrito=mostrarCarrito(carrito)
            if op==5:
                os.system("cls")
                break
        
        if opciones==3:
            carrito=mostrarCarrito(carrito)
            op=OpcionesSi_No("Realmente desea realizar la compra?   \n(1-SI,5-NO) \n:  ")
            if op==1:
                carrito.clear()
                os.system("cls")
                print("Muchas gracias por su compra")
                break

            if op==5:
                os.system("cls")
                break


        if opciones==4:
            os.system("cls")
            break

        continuar=input("""
                        Presionar enter para continuar     
                  """)
    if opciones==3:
        os.system("cls")
        print("Gracias por usar la tienda de Ivi's <3 <3 <3 ")
        break



    #solucionar ver carro luego de eliminar un producto(error no deja volver a ver el carro...)
    #solucionar finalizar compra no limpia el diccionario carrito....