import random


def jogar_foca():
    print_welcome()
    secret_word = load_secret_word()
    temp = initialize_right_letter(secret_word)
    print(temp)

    enforcou = False
    acertou = False
    erros = 0

    while not acertou and not enforcou:

        chute = ask_chute()
        if chute in secret_word:
            right_kick(chute, secret_word, temp)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in temp
        print(temp)
    if acertou:
        imprime_vencedor()
    else:
        imprime_perdedor(secret_word)
    print('<< ENCERROU >>')


def print_welcome():
    print("*-" * 20)
    print("WELCOLME TO FORCA GAME by PNavega")
    print("*-" * 20)


def load_secret_word():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    secret_word = palavras[numero].lower()
    return secret_word


def initialize_right_letter(word):
    return ["_" for letra in word]


def ask_chute():
    chute = input("Qual a letra? ").lower().strip()
    return chute


def right_kick(chute, secret_word, temp):
    if chute in secret_word:
        index = 0
        for letter in secret_word:
            if chute[0] == letter:
                temp[index] = letter
            index += 1


def imprime_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_perdedor(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



if __name__ == "__main__":
    jogar_foca()

