# Programa para ler duas notas de um aluno e exibir sua nota
nota_1 = float(input("Digite a primeira nota: \n"))
nota_2 = float(input("Digite a segunda nota: \n"))

print("As notas digitadas foram: \n",
      "Primeira nota: ", nota_1, "\n",
      "Segunda Nota: ", nota_2, "\n",
      sep=""
      )

media_aluno = (nota_1 + nota_2) / 2

print("A média deste aluno é :", media_aluno, end=".\n")
