# Programa para ler 3 notas de um aluno e
# se ele tiver nota maior que 7.0, retornar
# "Aprovado", senão "Reprovado".
# Incluir a condicional a seguir: media >= 4 "Recuperação"
#                                media < 4 "Reprovado"

# -------------------------------------Inicio do programa-------------------------------------

# Variáveis
error = 0

# Entradas
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

# Verificação de entradas
if (nota1 > 10 or nota2 > 10 or nota3 > 10) or (nota1 < 0 or nota2 < 0 or nota3 < 0):
    print("Alguma nota foi inserida errada, reinicie o programa.")
    erro = 1
else:
    # Processamento
    media_aluno = (nota1 + nota2 + nota3) / 3  # Calcula a média do aluno
    if media_aluno >= 7:
        print("Aprovado")
    else:
        if media_aluno >= 4:
            print("Recuperação")
        else:
            print("Reprovado")
# Fim
