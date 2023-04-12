

def jogar():
    print("******************")
    print("Bem vindo ao jogo de forca")
    print("******************")

    palavraSecreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        i = 0
        for letra in palavraSecreta:
            if(chute == letra):
                print("Econtrei a letra {} na posição {}".format(letra, i));
            index += 1
        print("Jogando...")
