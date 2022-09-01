import random

vitoria1 = 0
vitoria2 = 0
continua = 1

print("Bem vindo(a) ao Jokenpô!\nPrimeiramente vamos as regras do jogo.\nInicialmente escolha entre pedra/papel/tesoura\n"
      "a tesoura corta o papel, mas quebra com a pedra; o papel embrulha a pedra, mas é cortada pela tesoura e a pedra"
      " quebra a tesoura e é embrulhada pelo papel.")
opcao = int(input("Escolha a modalidade do jogo.\n1- Pessoa x Pessoa\n2- Pessoa x Computador\n3- Computador x Computador"))
if opcao == 1:
    while continua == 1:
        pessoa1 = int(input("1- Pedra\n2- Papel\n3- Tesoura"))
        pessoa2 = int(input("1- Pedra\n2- Papel\n3- Tesoura"))
        if pessoa1 == pessoa2:
            print("Empate")
        elif pessoa1 == 1 and pessoa2 == 2:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa1 == 2 and pessoa2 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa2 == 1 and pessoa1 == 2:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 2 and pessoa1 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa1 == 1 and pessoa2 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 3 and pessoa1 == 1:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2
        continua = int(input("Deseja continuar a jogar?\n1- sim\n2- não"))
elif opcao == 2:
    while continua == 1:
        pessoa1 = int(input("1- Pedra\n2- Papel\n3- Tesoura"))
        pessoa2 = random.randint(1,3)
        if pessoa1 == pessoa2:
            print("Empate")
        elif pessoa1 == 1 and pessoa2 == 2:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa1 == 2 and pessoa2 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa2 == 1 and pessoa1 == 2:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 2 and pessoa1 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa1 == 1 and pessoa2 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 3 and pessoa1 == 1:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2
        continua = int(input("Deseja continuar a jogar?\n1- sim\n2- não"))
elif opcao == 3:
    while continua == 1:
        pessoa1 = random.randint(1,3)
        pessoa2 = random.randint(1, 3)
        if pessoa1 == pessoa2:
            print("Empate")
        elif pessoa1 == 1 and pessoa2 == 2:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa1 == 2 and pessoa2 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa2 == 1 and pessoa1 == 2:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 2 and pessoa1 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa1 == 1 and pessoa2 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 3 and pessoa1 == 1:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2
        continua = int(input("Deseja continuar a jogar?\n1- sim\n2- não"))

    print("Primeiro jogador ganhou",vitoria1, "vezes\n Segundo jogador ganhou",vitoria2,"vezes")
