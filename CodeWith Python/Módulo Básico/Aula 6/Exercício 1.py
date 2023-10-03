# Código para ler duas notas de um aluno, calcular e imprimir a média desse aluno.
# Só devem ser aceitos valores válidos, durante a leitura

# Início do programa
nota01 = 0.0
nota02 = 0.0
media_calculada = 0.0
continuar = "S"

while continuar == "S" or continuar == "s":
    nota01 = float(input("Digite a 1ª nota: "))
    while nota01 >= 0 and nota01 <= 10:
        print(f"Nota 1 recebida. ({nota01})")
        break
    else:
        nota01 = float(input("Digite a 1ª nota novamente: "))
    nota02 = float(input("Digite a 2ª nota: "))
    while nota02 >= 0 and nota02 <= 10:
        print(f"Nota 2 recebida. ({nota02})")
        break
    else:
        nota02 = float(input("Digite a 2ª nota novamente: "))
    media_calculada = (nota01 + nota02) / 2
    print(f"A média do aluno foi {media_calculada}.")
    continuar = input("""
    Para continuar pressione S
    Para finalizar, precione Enter\n""")
# Fim do programa
