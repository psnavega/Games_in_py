import forca
import adivinhacao

print('*-'*10)
print('ESCOLHA O SEU GAME')
print('*-'*10)

choice = int(input("Digite o jogo que você quer jogar: [1] - Adivinha/ [2] - FORCA "))
def escolhe_jogo():
    if choice == 1:
        print("Jogando adivinhacao")
        adivinhacao.jogar_adivinhacao()
    elif choice == 2:
        print("Jogando forca")
        forca.jogar_foca()


if __name__ == "__main__":
    escolhe_jogo()
#QUANDO FOR IMPORTAR POR FORA, A FUNÇÃO NÃO ESTARÁ SENDO EXECUTADA, COM ESSE METODO SERÁ


