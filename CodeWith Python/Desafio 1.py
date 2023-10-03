jogadores = ["",""]
score = ["",""]
opcoes = ["Pedra", "Papel", "Tesoura"]
entrada01 = 0
entrada02 = 0
fim_partida = False
turno = 0

jogadores[0] = "Leo" #input(f"Digite o nome do 1º jogador: ") TESTES
jogadores[1] = "Juca" #input(f"Digite o nome do 2º jogador: ") TESTES

#for i in range(2):
#   jogadores[i] = input(f"Digite o nome do {i}º jogador: ")
while fim_partida == False:
    for turno in range(0, 2):
        entrada01 = int(input(f"""{jogadores[0]}, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura"""))
        while entrada01 < 1 or entrada01 > 3:
            entrada01 = int(input("Erro na entrada... Jogador 1, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura"))
        entrada02 = int(input("Jogador 2, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura"))
        while entrada02 <1 or entrada02 > 3:
            entrada02 = int(input("""Erro na entrada... Jogador 2, escolha uma opção...\n1 para Pedra\n2 para Papel\n3 para Tesoura"""))
        if entrada01 == 1:
            if entrada02 == 3:
                print("Jogador 1 venceu!")
                score[0] +=1
