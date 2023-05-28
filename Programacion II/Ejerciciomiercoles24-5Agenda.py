"""
Gestor de Contactos Crea un programa que funcione como un gestor de contactos. El
programa debe permitir al usuario almacenar nombres y números de teléfono en un
diccionario, así como buscar, agregar y eliminar contactos. Debe mostrar un menú con las
siguientes opciones:
"""
import os
def repetir(texto):
    num = input
    flag = True
    

os.system("cls")
contactos = {}

while 1:

    os.system("cls")

    print("""
Bienvenido al menu: elija una opcion
1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Mostrar todos los contactos
5. Salir
          """)
    op = input(":   ")

    os.system("cls")

    if op == "5":
        os.system("cls")
        print(" Adios :) \n\n\n")
        break

    elif op == "1":
        
        print("""Por favor, ingrese el nombre del contacto que desea añadir.""")
        nombre = input(":   ")

        validar = True
        while validar == True:
            print("""perfecto, ingrese el numero del contacto que desea añadir.""")
            numero = input(":   ")
            try:
                respaldo = numero
                numero = int(numero)
                validar = False
                numero = respaldo
            except ValueError:
                print("El numero debe estar conformado solo por numeros enteros.")
                validar = True

        breaking = False
        validar = True
        while validar == True:
            encontrado = False

            for key in contactos:
                if key == nombre:
                    encontrado = True

            if encontrado == True:
                print("\nEl nombre de contacto ingresado ya existe\n1)Sobreescribir\n2)Cancelar.")
                op = input(":   ")

                if op == "2":
                    breaking = True
                    validar = False
                elif op == "1":
                    validar = False
                else:
                    print("\nIngrese una opcion valida.\n")
                    validar = True

            else:
                validar = False

        if breaking == False:
            contactos[nombre]=numero
            print("Perfecto, contacto guardado.")
        else:
            print("El contacto no ha sido guardado.")
        
        space = input("\nPrecione cualquier tecla para continuar:   ")

    elif op == "2": #(busqueda) debo recorrer primero la lista. y a su vez recorrer el diccionario,
                    #de esta forma ver q hay dentro de cada diccionario y comparo su key nombre. para obtener el contacto q busco
        busqueda = input("ingresa el nombre del contacto a buscar :   ")
        for nom,num in contactos.items():
            if nom == busqueda:
                print(f"""
                El contacto con el nombre {nom} es:
                        nombre:  {nom}
                        teléfono: {num}""" )
                
        space = input("\nPrecione cualquier tecla para continuar:   ")
                
    elif op == "3":
        borrar = "no"
        eliminar= input("Ingrese el nombre del contacto que quiere eliminar:  ")
        for nom in contactos:
            if nom==eliminar:
                borrar = nom
        if borrar != "no":
            contactos.pop(borrar)
            print ("contacto borrado exitosamente.")
        else:
            print ("usuario no encontrado")
            
        space = input("\nPrecione cualquier tecla para continuar:   ")
        

    elif op == "4":
        msj = ""
        if len(contactos) == 0:
            msj = "No hay contactos guardados."
        else:
            for key in contactos:
                msj += key + " : " + str(contactos[key]) + "\n"
        print ("Lista de los contactos guardados:\n\n")
        print (msj)
        space = input("\nPrecione cualquier tecla para continuar:   ")

    else:
        print ("Opcion fuera del menu\n\n")
        space = input(":    ")