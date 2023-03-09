print("Bem-vindo à Calculadora do Amor")
nome1 = input("Diga o seu nome:\n").lower()
nome2 = input("Diga o nome dele(a):\n").lower()

nomes_combinados = nome1 + nome2
a = int(nomes_combinados.count("a"))
m = int(nomes_combinados.count("m"))
o = int(nomes_combinados.count("o"))
r = int(nomes_combinados.count("r"))

v = int(nomes_combinados.count("v"))
e = int(nomes_combinados.count("e"))
d = int(nomes_combinados.count("d"))
i = int(nomes_combinados.count("i"))

amor_verdadeiro = str(a + m + o + r) + str(v + e + d + i)
amor_verdadeiro_int = int(amor_verdadeiro)

if amor_verdadeiro_int < 10 or amor_verdadeiro_int > 90:
    print(f"A pontuação foi {amor_verdadeiro_int}%, vocês combinam como Coca-Cola e Mentos.")
elif amor_verdadeiro_int >= 40 and amor_verdadeiro_int <= 50:
    print(f"A pontuação foi {amor_verdadeiro_int}%, vocês são ok juntos...")
else:
    print(f"A pontuação foi {amor_verdadeiro_int}%")