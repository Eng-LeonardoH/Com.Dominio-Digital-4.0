jogadores = ["",""]
score = [int(),int()]
entrada01 = 0
entrada02 = 0
fim_partida = "0"
turno = 0
jogadores[0] = "Leo" #input(f"Digite o nome do 1º jogador: ") TESTES
jogadores[1] = "Juca" #input(f"Digite o nome do 2º jogador: ") TESTES

#for i in range(2):
#   jogadores[i] = input(f"Digite o nome do {i}º jogador: ")
while fim_partida == "0":
    for turno in range(0, 2):
        entrada01 = int(input(f"{jogadores[0]}, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura\nDigite: "))
        while entrada01 < 1 or entrada01 > 3:
            entrada01 = int(input(f"Erro na entrada... {jogadores[0]}, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura\nDigite: "))
        entrada02 = int(input(f"{jogadores[1]}, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura\nDigite: "))
        while entrada02 <1 or entrada02 > 3:
            entrada02 = int(input("Erro na entrada... {jogadores[1]} escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura\nDigite: "))
        if entrada01 == 1:
            if entrada02 == 3:
                print("Jogador 1 venceu!")
                score[0] += 1
            elif entrada02 == 2:
                print("Jogador 2 venceu!")
                score[1] += 1
            elif entrada02 == 1:
                print("Empate!")
        elif entrada01 == 2:
           if entrada02 == 1:
                print("Jogador 1 venceu!")
                score[0] += 1
           elif entrada02 == 3:
                print("Jogador 2 venceu!")
                score[1] += 1
           elif entrada02 == 2:
                print("Empate!")
        elif entrada01 == 3:
           if entrada02 == 2:
                print("Jogador 1 venceu!")
                score[0] += 1
           elif entrada02 == 1:
                print("Jogador 2 venceu!")
                score[1] += 1
           elif entrada02 == 3:
                print("Empate!")
    print(f"O placar está em {score[0]} para {jogadores[0]} e {score[1]} para {jogadores[1]}")
    fim_partida = input("Digite 0 para continuar, ou qualquer outro botão para parar\nDigite: ")
