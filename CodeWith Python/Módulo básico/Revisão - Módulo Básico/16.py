#16. Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez
#(considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em
#horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo
#pode iniciar em um dia e terminar no dia seguinte

hora_inicio = int(input("Digite a hora que a partida iniciou: "))
hora_fim = int(input("Digite a hora que a partida terminou: "))
duracao_hora = hora_fim - hora_inicio
duracao_dia = 0
if duracao_hora >= 24:
    duracao_dia = duracao_hora//24
    duracao_hora -= duracao_dia*24
    if duracao_dia > 1:
        print(f"A partida durou {duracao_dia} dias e {duracao_hora} horas.")
    else:
        print(f"A partida durou {duracao_dia} dia e {duracao_hora} horas.")
else:
    if duracao_hora > 1:
        print(f"A partida durou {duracao_hora} horas.")
    else:
        print(f"A partida durou {duracao_hora} hora.")