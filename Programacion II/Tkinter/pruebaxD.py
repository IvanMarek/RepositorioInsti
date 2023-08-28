num1 = input("Número: ")
num2 = input("Porcentagem: ")

def porcentagem(num1, num2):
    n1 = int(num1)
    n2 = int(num2)

    res =(n1 * n2 / 100)

    print(f"{n1} x {n2}% = {res}")

porcentagem(num1, num2)