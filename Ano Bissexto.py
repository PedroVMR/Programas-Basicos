
ano = int(input("Escolha um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    else:
        print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")