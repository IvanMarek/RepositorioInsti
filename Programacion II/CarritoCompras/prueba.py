

import os
from validaciones import validacionMenu
from validaciones import validarCodProducto
from validaciones import imprimir_productos
#from validaciones import SumaralCarro
from validaciones import OpcionesSi_No
from validaciones import validarStock

CodCarro=1
carrito={}
subTotal=0



productos={
    "2462":{"Nombre": "Salame fino", "Marca": "Trimoleti", "Precio": 1300, "Stock": 11},
    "2466":{"Nombre":"Salame grueso" , "Marca": "Trimoleti", "Precio": 1500,"Stock": 9},
    "2351":{"Nombre":"Queso barra", "Marca":"La Paulina","Precio":1800, "Stock": 15},
    "2353":{"Nombre":"Queso cremoso", "Marca":"Del Bueno" ,"Precio":2000 ,"Stock":12 },
    "2236":{"Nombre":"Mortadela", "Marca":"Paladini" ,"Precio":1600 ,"Stock":20},    
    "1961":{"Nombre":"Jamon" ,"Marca": "Recreo","Precio":1700, "Stock": 9 },
    "1963":{"Nombre":"Jamon crudo", "Marca":"Piamontesa" , "Precio": 2100, "Stock":10 },
    "1965":{"Nombre":"Jamon cocido", "Marca":"Tres Cruces" , "Precio": 2200 , "Stock": 14}    
           }


while True:
    MostrarProductos=imprimir_productos(productos)
    continuar=input("""
                    Preciones enter para ingresar al menú     
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
            reducirStock=validarStock("\nIngrese la cantidad del producto que desea:\n",productos,codigoProduct)
            while True:
                carrito[CodCarro]=productos[codigoProduct]
                carrito[CodCarro]["CantidadCompra"]= reducirStock
                subTotal=carrito[CodCarro]["Precio"] * carrito[CodCarro]["CantidadCompra"]
                carrito[CodCarro]["Subtotal"]=subTotal
                print(f"""
                    Muestra el producto guardado en el nuevo diccionario de carrito y la cantidad del mismo q compro el cliente...

                    {carrito}

                    """)
                CodCarro+=1
                break
            #os.system("cls")
            print("\n               Perfecto, su producto fue añadido al carro con éxito")

            
    continuar=input("""

                  Presionar enter para continuar     
                  """)
    if opciones==2:
        for i in productos:
            pass