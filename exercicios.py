import random

def jogar():

    print("******************")
    print("Bem vindo ao jogo de advinhação")
    print("******************")

    numeroCorreto = random.randrange(1, 11)

    rodada = 1
    print("Qual nível de dificuldade: 1 - Fácil; 2 - Médio; 3 - Difícil ?")
    dificuldade = int(input("Nível: "))
    if dificuldade == 1:
        tentativas = 3
    elif dificuldade == 2:
        tentativas = 2
    elif dificuldade == 3:
        tentativas = 1


    for rodada in range(1, tentativas + 1):

        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = input("Digite um número entre 1 e 10: ")
        incorreto = int(chute) < 1 or int(chute) > 10
        if(incorreto):
            print("Você digitou um número incorreto")
            continue
        print("Você digitou", chute)

        if(numeroCorreto == int(chute)):
            print("Você acertou")
            break
        else:
            if(numeroCorreto > int(chute)):
                print("Você errou! O Número correto está a cima")
            elif(numeroCorreto < int(chute)):
                print("Você errou! O número correto está a baixo")
        rodada += 1