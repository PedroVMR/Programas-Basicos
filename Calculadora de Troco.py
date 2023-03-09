# Adicionando as variáveis 
print("Bem-vindo a Calculadora de Troco!")
valor_base = float(input("Qual o valor da conta: R$"))
pessoas_pagantes = int(input("Quantas pessoas vão dividir a conta: "))
gorjeta = int(input("Qual porcetagem de gorjeta você gostaria de deixar (10, 12 ou 15%): "))

# Convertendo os valores
gorjeta_porcetagem = int(gorjeta) / 100

valor_com_gorjeta = round((valor_base * gorjeta_porcetagem) + valor_base, 2)
valor_cada = round(valor_com_gorjeta / pessoas_pagantes, 2)

print(f"Cada pessoa irá pagar R${valor_cada}")