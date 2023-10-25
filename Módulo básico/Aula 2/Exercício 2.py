# Progrma para ler o nome de dois times e o numero de gols marcados para cada time.
# O programa vai exibir o nome do vencedor, caso seja empate, será exibido "empate"

# Início do programa

# Entradas
nome_time1 = input("Digite o nome do primeiro time: ")
nome_time2 = input("Digite o nome do segundo time: ")
placar_time1 = int(input(f"Digite o número de gols marcados pelo time {nome_time1}: "))
placar_time2 = int(input(f"Digite o número de gols marcados pelo time {nome_time2}: "))

# Processamento
if placar_time1 == placar_time2:
    print("Empate")
elif placar_time1 > placar_time2:
    print(f"O time {nome_time1} venceu a partida !!!")
else:
    print(f"O time {nome_time2} venceu a partida !!!")

# Fim do programa
