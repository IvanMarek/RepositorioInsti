import os
from validaciones import validacionMenu
from validaciones import validarCodProducto
from validaciones import SumaralCarro
from validaciones import OpcionesSi_No

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
    
    msj="  Codigo | Nombre"
    for i in productos:
        msj= msj + f"""
    {i} | {productos[i]["Nombre"]} """
    print(msj)
    continuar=input("""        Preciones enter para ingresar al menú     
    """)
        
    print("""
        1. Buscar producto por código
        2. Ver carrito
        3. salir
        
        """)

    opciones= validacionMenu(":    ",1,3)


    if opciones ==1:
        print("         Buscar producto por código o nombre:         ")
        codigoProduct= validarCodProducto(":   ", productos )
        
        print("Desea añadir el producto al carro?. (1-SI,5-NO)")
        op=OpcionesSi_No(" :    ")

        if op==1:
            cantidad=True
            while cantidad==True:
                cantidadProducto=int(input("    Ingresar la cantidad del producto que desea:   "))
                validarop=False
                if cantidadProducto <= productos[codigoProduct]["Stock"]:
                    reducirStock= productos[codigoProduct]["Stock"] - cantidadProducto
                    productos[codigoProduct]["Stock"]= reducirStock
                    print(productos[codigoProduct])
                    break
                elif cantidadProducto > productos[codigoProduct]["Stock"] and productos[codigoProduct]["Stock"] !=0:
                    print(f"""
                    No contamos con la cantidad indicada, 
                    Contamos con {productos[codigoProduct]["Stock"]} Unidad\es del producto {productos[codigoProduct]["Nombre"]},
                    """)
                else:
                    print("          Producto sin stock         ")
                    break
        

    continuar=input("""       Presionar enter para continuar:      
    """)



