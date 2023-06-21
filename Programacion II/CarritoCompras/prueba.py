

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

def imprimir_productos(productos):
    
   
    print("   Código  |       Nombre        |       Marca         |  Precio   |  Stock     |")
    print("---------------------------------------------------------------------------------")
    for codigo, detalles in productos.items():
        nombre = detalles["Nombre"]
        marca = detalles["Marca"]
        precio = detalles["Precio"]
        stock = detalles["Stock"]

        # Utilizamos la función format() para establecer el ancho fijo de cada columna
        print("    {:<6} |    {:<17}|    {:<17}|   ${:<7}| {:<10} |".format(codigo, nombre, marca, precio, stock))

imprimir_productos(productos)