# Programa para ler o nome de uma pessoa, sua idade e o seu salário e mostre essas informações na tela

nome = input("Insira seu nome:\n")
idade = int(input("Insira sua idade:\n"))
salario = float(input("Insira seu salário:\n"))

print("\n", nome, " tem ", idade,
      " anos de idade e recebe R$", salario,
      ", mas com o aumento, passará a receber R$",
      salario * 1.2,
      sep=""
      )
