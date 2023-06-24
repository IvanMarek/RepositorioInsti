import os
from validaciones import *


carrito={}
subTotal=0

productos={
    "2462":{"Nombre": "Salame fino", "Marca": "Trimoleti", "Precio": 1300, "Stock": 11},
    "2466":{"Nombre":"Salame grueso" , "Marca": "Trimoleti", "Precio": 1500,"Stock": 9},
    "2351":{"Nombre":"Queso barra", "Marca":"La Paulina","Precio":1800, "Stock": 15},
    "2353":{"Nombre":"Queso cremoso", "Marca":"Del Bueno" ,"Precio":2000 ,"Stock":12 },
    "2236":{"Nombre":"Mortadela", "Marca":"Paladini" ,"Precio":1600 ,"Stock":20},    
    "1961":{"Nombre":"Jamón" ,"Marca": "Recreo","Precio":1700, "Stock": 9 },
    "1963":{"Nombre":"Jamón crudo", "Marca":"Piamontesa" , "Precio": 2100, "Stock":10 },
    "1965":{"Nombre":"Jamón cocido", "Marca":"Tres Cruces" , "Precio": 2200 , "Stock": 14}    
           }


while True:
    print("                     Bienvenido a la tienda de Ivi's")

    MostrarProductos=imprimir_productos(productos)
    continuar=input("""
                    Presione enter para ingresar al menú     
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
        print("\n¿Desea añadir el producto al carro? (1-SI,5-NO)\n")
        op=OpcionesSi_No(":   ")
        if op==1:
            cantidadProducto=validarStock("\nIngrese la cantidad del producto que desea:\n",productos,codigoProduct)
            if cantidadProducto!= False:
                while True:
                    if codigoProduct in carrito:
                        carrito[codigoProduct]["CantidadCompra"]+= cantidadProducto
                        carrito[codigoProduct]["Subtotal"]+= cantidadProducto * productos[codigoProduct]["Precio"]
                    else:
                        carrito[codigoProduct]={"Nombre" : productos[codigoProduct]["Nombre"],"Marca":productos[codigoProduct]["Marca"] ,"CantidadCompra" : cantidadProducto,"Precio" : productos[codigoProduct]["Precio"],"Subtotal" : cantidadProducto * productos[codigoProduct]["Precio"]}
                    print("\n               Perfecto, su producto fue añadido al carro con éxito")
                    break

        if op==5:
            os.system("cls")
            pass
        continuar=input("""
                        Presionar enter para continuar     
                  """)
    if opciones==2:
        mostrarCarrito(carrito)
        print("""
1. Modificar cantidad de un producto
2. Eliminar producto del carro de compras
3. Finalizar compra
4. Regresar al menú principal
""")
        opciones= validacionMenu(":    ",1,4)
        if opciones==1:
            print("\nIngrese el código o nombre del producto que desea modificar la cantidad\n")
            codigoProduct= validarCodigoProducto(" :   ", carrito)
            print(carrito[codigoProduct])

            op=OpcionesSi_No("¿Realmente desea modificar este producto?   (1-SI,5-NO) \n:  ")
            if op==1:
                cantidad_actualizada=validarCantidad("Ingresar la cantidad de producto que desea modificar(recuerde que esta opción es para reducir la cantidad del producto seleccionado):\n:     ", carrito, codigoProduct, productos)

            if op==5:
                os.system("cls")
                pass
                continuar=input("""
                        Presionar enter para volver al menú principal     
                  """)
                
        if opciones==2:
            print("\nIngrese el código o nombre del producto que desea eliminar:\n")
            codigoProductEliminar= validarCodigoProducto(" :   ", carrito)
            print(carrito[codigoProductEliminar])
            op=OpcionesSi_No("¿Realmente desea eliminar este producto?   \n(1-SI,5-NO) \n:  ")
            if op==1:
                eliminar=eliminiarProductoCarro(carrito,codigoProductEliminar,productos)
                continuar=input("""
                        Presionar enter para volver al menú principal     
                  """)
            if op==5:
                os.system("cls")
                pass
                continuar=input("""
                        Presionar enter para volver al menú principal     
                  """)

        if opciones==3:
            carro=mostrarCarrito(carrito)
            op=OpcionesSi_No("¿Realmente desea realizar la compra?   \n(1-SI,5-NO) \n:  ")
            if op==1:
                borrarCarro=finalizarCompra(carrito)
                os.system("cls")
                print("""
                        Muchas gracias por su compra
                        
                        
                        """)
                
            if op==5:
                os.system("cls")
                pass
                continuar=input("""
                        Presionar enter para volver al menú principal     
                  """)
                
        if opciones==4:
            os.system("cls")
            pass
            continuar=input("""
                        Presionar enter para volver al menú principal     
                  """)
    if opciones==3:
        os.system("cls")
        print("""
                        Gracias por usar la tienda de Ivi's <3 <3 <3 
                        
                        """)
        break