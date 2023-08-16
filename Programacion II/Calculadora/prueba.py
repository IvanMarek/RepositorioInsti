def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

print("Calculadora Simple")
print("Operaciones disponibles: +, -, *, /")

while True:
    operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para salir: ")

    if operacion == 'salir':
        print("¡Hasta luego!")
        break

    if operacion in ('+', '-', '*', '/'):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)

        print(f"Resultado: {resultado}")
    else:
        print("Operación no válida. Por favor, ingrese +, -, *, o /")


        