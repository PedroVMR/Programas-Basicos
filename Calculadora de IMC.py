# Os inputs recebem as variáveis "peso" e "altura" em forma de texto.
peso = input("Diga seu peso em kg: ")
altura = input("Diga sua altura em metros: ")
# O prefixo "_int" transforma as variáveis em números reais.
peso_int = float(peso)
altura_int = float(altura)
# O "result" faz a fórmula de cálculo do IMC = peso/altura^2 e o "round" arredonda o resultado em 2 casas decimais
result = (round(peso_int / (altura_int * altura_int), 2))
# o "print" imprime o resultado com a frase "Seu IMC é" e o f transforma o "result" em texto de novo.
print(f"Seu IMC é: {result}")

if result < 18.5:
    print("Você está abaixo do peso.")
elif result < 25:
    print("Você esta no peso ideal. (Parabéns!)")
elif result < 30:
    print("Você está levemente acima do peso")
elif result < 35:
    print("Você está com Obsedidade de grau I")
elif result < 40:
    print("Você está com Obesidade de grau II (Severa)")
else:
    print("Você esta com Obesidade grau III (Mórbida)")

