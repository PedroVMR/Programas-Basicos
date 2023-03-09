print("███████  ██████  ██████  ██████  ███████ ██    ██ ██ ██    ██  █████") 
print("██      ██    ██ ██   ██ ██   ██ ██      ██    ██ ██ ██    ██ ██   ██") 
print("███████ ██    ██ ██████  ██████  █████   ██    ██ ██ ██    ██ ███████") 
print("     ██ ██    ██ ██   ██ ██   ██ ██       ██  ██  ██  ██  ██  ██   ██") 
print("███████  ██████  ██████  ██   ██ ███████   ████   ██   ████   ██   ██")

# Decisões pela direita
print("Seus pais deixaram você na casa dos seus avôs pela primeira vez.")
quarto = input("Escolha um quarto: Esquerda ou Direita? ").lower()
if quarto == "direita":
    comida = input("Sua vó oferece comida, mas ele parece crua: Comer ou Não Comer? ").lower()
    if comida ==  "comer":
        print("DECISÃO ERRADA! A comida estava envenenada. VOCÊ MORREU!")
    elif comida == "não comer":
        print("Você acorda em um porão")
        vô_olhando = input("Vovô está observando você: Lutar ou Correr para a Porta? ").lower()
        if vô_olhando == "correr" or vô_olhando == "correr para a porta":
                print("DECISÃO ERRADA! Vovô tranca a porta e mata você. VOCÊ MORREU!")
        if vô_olhando == "lutar":
            print("Vovô cai no chão inconciente.")
            game = input("Vovó pede para você jogar um jogo com ela: Aceitar ou Recusar: ").lower()
            if game == "aceitar":
                vó_estranha = input("Vovó começa a agir estranho: Continuar Jogando ou Parar de Jogar: ").lower()
                if vó_estranha == "parar" or vó_estranha == "parar de jogar":
                    print("Você vai para cama.")
                    som_estranho = input("Você escuta um som estranho debaixo da cama: Investigar ou Ignorar? ").lower()
                    if som_estranho == "investigar":
                        print("DECISÃO ERRADA! Vovó estava se escondendo debaixo da cama e te matou. VOCÊ MORREU!")
                    elif som_estranho == "ignorar":
                        print("Você acorda e vai tomar café da manhã")
                        esconde_esconde = input("Seus avós querem brincar de esconde-esconde com você: Aceitar ou Recusar? ").lower()
                        if esconde_esconde == "aceitar":
                            print("Você se esconde atrás do sofá")
                            telefonema = input('Você escuta sua vó falando "Eu vou te pegar!": Ligar para 190 ou Ligar para Mãe? ').lower()
                            if telefonema == "190" or telefonema == "ligar para 190":
                                print("A policia acha que você está exagerando e desliga")
                                print("DECISÃO ERRADA! Vovó encontra você. VOCÊ MORREU!")
                            elif telefonema == "mãe" or telefonema == "ligar para mãe":
                                print("Você conta tudo para sua mãe")
                                print("Na verdade eles não eram seus verdadeiros avós.")   
                                print("Sua mãe liga para a policia. Você teve sorte dessa vez. VOCÊ SOBREVIVEU!")
                elif vó_estranha == "continuar" or vó_estranha == "continuar jogando":
                    print("Você ganhou de sua Vó no jogo.")
                    print("DECISÃO ERRADA! Vovó ficou furiosa com você e te matou. VOCÊ MORREU!")           
            elif game == "recusar":
                print("DECISÃO ERRADA! Vovó ficou furiosa com você e te matou. VOCÊ MORREU!")

# Decisões pela esquerda
elif quarto == "esquerda":
    game = input("Vovó pede para você jogar um jogo com ela: Aceitar ou Recusar: ").lower()
    if game == "aceitar":
        vó_estranha = input("Vovó começa a agir estranho: Continuar Jogando ou Parar de Jogar: ").lower()
        if vó_estranha == "parar" or vó_estranha == "parar de jogar":
            print("Você vai para cama.")
            som_estranho = input("Você escuta um som estranho debaixo da cama: Investigar ou Ignorar? ").lower()
            if som_estranho == "investigar":
                print("DECISÃO ERRADA! Vovó estava se escondendo debaixo da cama e te matou. VOCÊ MORREU!")
            elif som_estranho == "ignorar":
                print("Você acorda e vai tomar café da manhã")
                esconde_esconde = input("Seus avós querem brincar de esconde-esconde com você: Aceitar ou Recusar? ").lower()
                if esconde_esconde == "aceitar":
                    print("Você se esconde atrás do sofá")
                    telefonema = input('Você escuta sua vó falando "Eu vou te pegar!": Ligar para 190 ou Ligar para Mãe? ').lower()
                    if telefonema == "190" or telefonema == "ligar para 190":
                        print("A policia acha que você está exagerando e desliga")
                        print("DECISÃO ERRADA! Vovó encontra você. VOCÊ MORREU!")
                    elif telefonema == "mãe" or telefonema == "ligar para mãe":
                        print("Você conta tudo para sua mãe")
                        print("Na verdade eles não eram seus verdadeiros avós.")   
                        print("Sua mãe liga para a policia. Você teve sorte dessa vez. VOCÊ SOBREVIVEU!")
        elif vó_estranha == "continuar" or vó_estranha == "continuar jogando":
                    print("Você ganhou de sua Vó no jogo.")
                    print("DECISÃO ERRADA! Vovó ficou furiosa com você e te matou. VOCÊ MORREU!")           
    elif game == "recusar":
        print("DECISÃO ERRADA! Vovó ficou furiosa com você e te matou. VOCÊ MORREU!")
    