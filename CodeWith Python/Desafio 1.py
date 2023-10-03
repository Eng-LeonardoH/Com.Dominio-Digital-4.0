jogadores = ["",""]
opcoes = ["Pedra", "Papel", "Tesoura"]
entrada01 = 0
entrada02 = 0
fim_partida = 0

for i in range (2):
    jogadores[i] = input(f"Digite o nome do {i+1}º jogador: ")

print("Jogador 1 inicia a partida...")
while fim_partida != 1:
    entrada01 = int(input())
Jogador 1, escolha uma opção...
1 para Pedra
2 para Papel
3 para Tesoura
""")
