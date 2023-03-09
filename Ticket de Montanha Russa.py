print("Bem-vindo a montanha russa")
altura = int(input("Qual a sua altura em cm: "))
conta = 0

if altura > 1.2:
    print("Você pode andar na montanha russa!")
    idade = int(input("Qual a sua idade? "))
    if idade < 12:
        conta = 5
        print("O ticket infantil custa R$5")
    elif idade <= 18:
        conta = 7
        print("O ticket adolecente custa R$7")
    else: 
        conta = 12
        print("O ticket de Adulto custa R$12")
    foto = input("Você gostaria de receber uma foto após a volta na montanha russa? S ou N? ")
    if foto == "S":
        conta = conta + 3

    print(f"O valor final será R${conta}")


else:
    print("Sinto muito, você vai ter que crescer um pouco mais.")
