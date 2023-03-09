operacao = input("Qual tipo de operação você quer fazer (1. Adição, 2. Subtração, 3. Divisão ou 4. Multiplicação): ")
if operacao == "1" or operacao == "2" or operacao == "3" or operacao == "4":

    num_1 = float(input("Número 1: "))
    num_2 = float(input("Número 2: "))

    if operacao == "1":
        print(num_1 + num_2)
    elif operacao == "2":
        print(num_1 - num_2)
    elif operacao == "3":
        print(round(num_1/num_2),2)
    elif operacao == "4":
        print(num_1 * num_2)
else:
    print("Operação Inválida")
