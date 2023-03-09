
print("Bem-vindo ao Entrega-Pizza-Python!")
pizza = input("Qual tamanho de pizza você deseja? P, M ou G: ")
adicional_queijo = input("Você gostaria de adcionar mussarela extra? S ou N: ")
adicional_peperonni = input("Você gostaria de adcionar peperonni extra? S ou N: ")

conta = 0 
if pizza == "S":
    conta = 15
elif pizza == "M":
    conta = 20
elif pizza == "G":
    conta = 25

if adicional_peperonni == "S":
        conta = conta + 3

if adicional_queijo == "S":
        conta = conta + 2
print(f"O valor da pizza ficou em R${conta}")