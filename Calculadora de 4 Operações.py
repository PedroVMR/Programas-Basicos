operacao = input("Qual tipo de operação você quer fazer (Adição, Subtração, Divisão ou Multiplicação): ")
if operacao == "adicao" or operacao == "subtracao" or operacao == "divisao" or operacao == "multiplicao":

    num_1 = float(input("Número 1: "))
    num_2 = float(input("Número 2: "))

    if operacao == "adicao":
        print(num_1 + num_2)
    elif operacao == "subtracao":
        print(num_1 - num_2)
    elif operacao == "divisao":
        print(round(num_1/num_2),2)
    elif operacao == "multiplicacao":
        print(num_1 * num_2)
else:
    print("Operação Inválida")