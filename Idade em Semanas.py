idade = input("Diga quantos anos você tem: ")

idade_dias = int(idade) * 365
idade_semanas = int(idade) * 52
idade_meses = int(idade) * 12

dias_restantes = 32850 - idade_dias
semanas_restantes = 4690 - idade_semanas
meses_restantes = 1080 - idade_meses
print(f"Você tem {dias_restantes} dias, {semanas_restantes} semanas, e {meses_restantes} meses restantes 💀. ")
