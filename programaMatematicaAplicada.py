import random
import os
from fractions import Fraction
from math import sqrt


# GLOBAL

op = 0
con = 0
flag = True
space = ""

menu_flag = True

bucle_paralel = True







def encajar(txt):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            resul = round(float(Fraction(num)) , 2)

            flag = False

        except ValueError:
            print("valor ingresado no correcto")
            continue

    return(resul)


def exacto(txt):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            
            resul = (Fraction(num))

            flag = False

        except ValueError:
            print("El valor ingresado no es valido. Por favor, vuelva a intentar")
            continue

    return(resul)



"""def validar(txt):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            resul = int(num)
            flag = False

        except ValueError:
            print("valor ingresado no era una opcion valida. Por favor, vuelva a intentar")
            continue

    return(resul)"""

def validar_rango(txt,min,max):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            num = int(num)
            if((num <= max) and (num >= min)):
                flag = False
                resul = num
            else:
                print("valor ingresado fuera de rango. Por favor, vuelva a intentar")

        except ValueError:
            print("valor ingresado no es valido. Por favor, vuelva a intentar")
            continue

    return(resul)











while 1:
    os.system("cls")
    menu_flag = True
    
    print("""

Bienvenido al programa de resolucion de funciones lineales y cuadraticas.
¿En que podemos ayudarle?

    por favor ingrese una opcion.

    1) Sacar las Paralelas y Perpendiculares a una Funcion Lineal.

    2) Resolver una Funcion Lineal.

    3) Resolver una Funcion cuadratica.
    
    """)

    op = validar_rango("      :   ",1,3)

    os.system("cls")
    

    if op == 1:
        
        while menu_flag == True:

            # PARALELA

            coeficiente_principal = 0
            termino_independiente = 0
            con = 0
            paralela = []
            perpendicular = []
            
            print("""
Perfecto. Vamos a sacar las paralelas y perpendiculares de una Funcion Lineal.

Ax + B

    """)
            coeficiente_principal = exacto("ingrese el valor principal (A):   ")
            termino_independiente = exacto("ingrese el termino independiente (B):  ")

            
            

            os.system("cls")

            if (coeficiente_principal == 0 ):

                

                space = input("""
El coeficiente principal no puede ser 0.
Precione cualquier tecla para continuar ...     
    """)
                os.system("cls")
            else:
                negative = ((1 / coeficiente_principal) * (-1))

                while (con < 3): ### Comienza a sacar las paralelas ###
                    flag = True
            
                    numran = random.randint(-50,50)

                    for i in range (0,len(paralela)):
                        if ((numran == paralela[i]) or (numran == termino_independiente) or (numran == 0)):
                            flag = False
                    
                    if (numran < 0):
                        numran = "(" + str(numran) + ")"
                            
                    if (flag == True):
                        paralela.append(numran)
                        con += 1


                con = 0


                while (con < 3):
                    flag = True

                    numran = random.randint(-50,50)

                    for i in range (0,len(perpendicular)):
                        if ((numran == perpendicular[i]) or (numran == termino_independiente) or (numran == 0)):
                            flag = False
                    
                    if (numran < 0):
                        numran = "(" + str(numran) + ")"
                            
                    if (flag == True):
                        perpendicular.append(numran)
                        con += 1




                
                print (f"""
Funcion :  {coeficiente_principal}x + {termino_independiente}

Funciones paralelas a la dada:
{coeficiente_principal}x + {paralela[0]}
{coeficiente_principal}x + {paralela[1]}
{coeficiente_principal}x + {paralela[2]}

Funciones perpendiculares a la dada:
{negative}x + {perpendicular[0]}
{negative}x + {perpendicular[1]}
{negative}x + {perpendicular[2]}

la condicion de paralelismo es que el coeficiente principal sea el mismo y el termino independiente sea distinto.
La condicion de perpendicularidad es que la pendiente debe ser inversa y opuesta, el termino independiente puede cambiar o no hacerlo.
                            """)
                
                print("""
Seleccione una de las siguientes opciones:

1) Regresar al menu principal.

2) Sacar las paralelas y perpendiculares de otra funcion.

                """)

                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opcion fuera de rango")

                os.system("cls")
            

    if op == 2:
        
        while menu_flag == True:

            # LINEAL

            coeficiente_principal = 0
            termino_independiente = 0


            
            print("""
Perfecto. Vamos a resolver una Funcion Lineal.

Ax + B

    """)
            coeficiente_principal = exacto("ingrese el valor principal (A):   ")
            termino_independiente = exacto("ingrese el termino independiente (B):  ")

            os.system("cls")

            if (coeficiente_principal == 0 ):

                space = input("""
El coeficiente principal no puede ser 0.
Precione cualquier tecla para continuar ...     
    """)
                os.system("cls")
            else:
                if (coeficiente_principal > 0):
                    tipo_pendiente = "creciente"
                else:
                    tipo_pendiente = "decreciente"

                if (termino_independiente != 0):
                    corte_x = ((termino_independiente *-1) / coeficiente_principal )
                else:
                    corte_x = 0

                os.system("cls")

                print(f"""
Solucion de la funcion dada:
{coeficiente_principal}x + {termino_independiente}

El corte en X es = {corte_x}
El corte en Y es = {termino_independiente}
El comportamiento de la recta es {tipo_pendiente}

Seleccione una de las siguientes opciones:

1) Regresar al menu principal.

2) Sacar las paralelas y perpendiculares de otra funcion.
""")
                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opcion fuera de rango")


    if op == 3:
        
        while menu_flag == True:
            raices = []
            delta=0
            pendiente = 0
            # CUADRATICA

            valor_pendiente = exacto("Ingrese el coheficiente principal. Siendo ax² + bx + c. Ingrese el valor de a \n :     ")
            valor_lineal = exacto("Ingrese el termino lineal. Siendo ax² + bx + c. Ingrese el valor de b \n :    ")
            valor_ordenada = exacto("Ingrese el termino independiente. Siendo ax² + bx + c. Ingrese el valor de c \n :   ")
            
            if (valor_pendiente == 0 ):

                space = input("""
El coeficiente principal no puede ser 0.
Precione cualquier tecla para continuar ...     
    """)
                os.system("cls")
            else:

                if(valor_pendiente>0):
                    pendiente = 1
                else:
                    pendiente = -1

                delta = (valor_lineal**2 - 4 * valor_pendiente * valor_ordenada)
                    

                if delta >= 0:

                    raiz = ((valor_lineal * (-1)) + sqrt(delta)) / (2 * valor_pendiente)

                    raices.append(raiz)

                    raiz = ((valor_lineal * (-1)) - sqrt(delta)) / (2 * valor_pendiente)

                    raices.append(raiz)

                    if delta == 0:

                        tipo_raiz = "Las raices son de doble multiplicidad" #raices doble multiplicidad
                        

                    if delta > 0:

                        tipo_raiz = "Las raices son Reales" #raices reales

                    if (raices[0]) == raices[1]:
                        tipo_raiz = "Las raiz es una sola."



                if delta < 0:
                    tipo_raiz = "Las raices son imaginarias/complejas" #no tiene raices reales
                    


                    
                    

                vertice_x = (valor_lineal * -1) / (2 * valor_pendiente)

                vertice_y = valor_pendiente * vertice_x ** 2 + valor_lineal * vertice_x + valor_ordenada


                if valor_lineal < 0:
                    pri_lineal = "(" + str(valor_lineal) + ")"
                else:
                    pri_lineal = valor_lineal
                
                if valor_ordenada < 0:
                    pri_ordenada = "(" + str(valor_ordenada) + ")"
                else:
                    pri_ordenada = valor_ordenada
                

                print (f"""
Solucion a la raiz dada: {valor_pendiente}x² + {pri_lineal}x + {pri_ordenada}

{tipo_raiz}
                    """)
                if delta >= 0:
                    print(f"""
Raices: X1: {Fraction(raices[0])}     ,       X2: {Fraction(raices[1])}
                """)
                else:
                    print("La parabola no cruza el eje X en ningún punto real.")

                
                print(f"""
El vertice X es:  {vertice_x}
El vertice y es:  {vertice_y}

Coordenadas de vertice: ({vertice_x} ; {vertice_y})
                """)


                if(pendiente==1):
                    intervalo_decrecimiento = "(-∞, " + str(vertice_x) + ")"  
                    intervalo_crecimiento = "(" + str(vertice_x) + ", +∞)"
                    print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
                    print("El intervalo de crecimiento es " + intervalo_crecimiento)

                elif(pendiente==-1):
                    intervalo_crecimiento = "(-∞, " + str(vertice_x) + ")"  
                    intervalo_decrecimiento = "(" + str(vertice_x) + ", +∞)"
                    print("El intervalo de crecimiento es " + intervalo_crecimiento)
                    print("El intervalo de decrecimiento es " + intervalo_decrecimiento)

                if valor_pendiente > 0:
                    print ("La parabola es cóncava para arriba")
                else:
                    print ("La parabola es cóncava para abajo")
                

                print("""
Seleccione una de las siguientes opciones:

1) Regresar al menu principal.

2) Resolver otra funcion cuadratica.

""")
                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opción fuera de rango")

                os.system("cls")