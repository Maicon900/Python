import forca
import exercicios

print("******************")
print("Escolha o jogo!")
print("******************")

print("1 - Forca; 2 - Advinhação");
jogo = int(input("Qual o jogo? "));

if jogo == 1:
    forca.jogar()
    print("Jogando forca");
elif jogo == 2:
    exercicios.jogar()
    print("Jogando advinhação")