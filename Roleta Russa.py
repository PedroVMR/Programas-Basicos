import random

print("Vamos ver quem vai ser sorteado!")
pessoas = input("Diga o nome de todas as pessoas?\n")
lista_pessoas = pessoas.split(", ")

lista_pessoas_len = len(lista_pessoas)
escolha_aleatoria = random.randint(0, lista_pessoas_len -1)

pessoa_escolhida = lista_pessoas[escolha_aleatoria]
print(f"A pessoa sorteada foi {pessoa_escolhida}!")