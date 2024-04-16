#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
def jogo_da_forca():
    p_oc = "sabinada"  
    p_mos = "_" * len(p_oc)
    tent = len(p_oc) + 2
    print("Você tem", tent, "tentativas para adivinhar a palavra.")

    while tent > 0 and "_" in p_mos:
        print("\nPalavra:", p_mos)
        letra = input("Digite uma letra: ")

        if letra in p_oc:
            for c in range(len(p_oc)):
                if p_oc[c] == letra:
                    p_mos = p_mos[:c] + letra + p_mos[c+1:]
        else:
            tent= tent - 1
            print("Letra incorreta. Você tem", tent, "tentativas restantes.")

    if "_" not in p_mos:
        print("\nParabéns! Você adivinhou a palavra:", p_oc)
    else:
        print("\nVocê perdeu. A palavra era:", p_oc)

jogo_da_forca()