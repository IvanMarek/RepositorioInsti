import os

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



validar= True
Codcorrecto=False
while validar==True:
    text="      Nombre       |        Marca        |        Precio         |        Stock        | "
    codProducto=input("""Ingresar codigo del producto:  
    """)
    for i in productos:
        if codProducto==i or codProducto==productos[i]["Nombre"]:
            codigoValido=i
            Codcorrecto=True
    if Codcorrecto==True:

        print(f"""
                {text}
Producto encontrado:     {productos[codigoValido]["Nombre"]}        {productos[codigoValido]["Marca"]}                 {productos[codigoValido]["Precio"]}                  {productos[codigoValido]["Stock"]}               
                
                """)
        break
    else:
        print("Producto no encontrado. Ingrese nuevamente un código valido")
    
print("Desea añadir el producto al carro?. (1-SI,5-NO)")

op=input(""" """)
validarop=True
while validarop==True:
    try:
        op=int(op)
        if op==1:
            cantidadProducto=int(input("    Ingresar la cantidad del producto que desea:   "))
            validarop=False
            if cantidadProducto <= productos[codigoValido]["Stock"]:
                reducirStock= productos[codigoValido]["Stock"] - cantidadProducto
                productos[codigoValido]["Stock"]= reducirStock
                print(productos[codigoValido])
            elif cantidadProducto > productos[codigoValido]["Stock"]:
                print(f"""
                No contamos con la cantidad indicada, 
                Contamos con {productos[codigoValido]["Stock"]} Unidad\es del producto {productos[codigoValido]["Nombre"]},
                """)
                cantidad=True
                while cantidad==True:
                    cantidadProducto=int(input("    Ingresar la cantidad del producto que desea:   "))
                    if cantidadProducto <= productos[codigoValido]["Stock"]:
                        reducirStock= productos[codigoValido]["Stock"] - cantidadProducto
                        productos[codigoValido]["Stock"]= reducirStock
                        print(productos[codigoValido])
                        break
            else:
                print("Producto sin stock", productos[codigoValido]["Nombre"], productos[codigoValido]["Stock"])
        if op==5:
            print("Regresar al menu principal:   ")
            continuar=input(" Presionar enter para continuar")
            break
        else:
            print("Opcion incorrecta, Ingrese una opción valida")
            
    except ValueError:
        print("Opcion incorrecta, Ingrese una opción valida 2")

