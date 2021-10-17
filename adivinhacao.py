def jogar_adivinhacao():
    import random

    print('*-'*10)
    print('Jogo de adivinhação')
    print('*-'*10)

    print(""" 
    ESCOLHA O SEU NIVEL 
    [1] - FÁCIL
    [2] - MÉDIA
    [3] - DIFÍCIL
    """)
    nivel = int(input("Escolha um nível: "))
    pont = 0
    cont = 0
    while True:
        if nivel == 1:
            chance = 5
            break
        elif nivel == 2:
            chance = 3
            break
        elif nivel == 3:
            chance = 1
            break
        else:
            print("Opção inválida!")
            break
    while True:
        maquina = random.randint(1, 10)
        palpite = int(input(f'Digite o seu palpite entre 1 e 10: '))

        if cont == chance:
            print("Perdeu por excesso")
            break
        elif maquina != palpite:
            print(f'Você errou! Você escolheu {palpite} e a máquina {maquina}.')
            cont += 1
        elif (maquina == palpite):
            print(f'Você ganhou! Você escolheu {palpite} e a máquina {maquina}.')
            break

        pont += abs(maquina - palpite)



    print(f'{pont} pontos' )
    print("<< ENCERRANDO >>")

if (__name__ == "__main__"):
    jogar_adivinhacao()



