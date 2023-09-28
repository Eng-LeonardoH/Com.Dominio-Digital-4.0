# Programa para ler o nome de uma pessoa, sua idade e o seu salário e mostre essas informações na tela
FILHOS_ADICIONAL = float(150)
DESCONTO_IMPOSTO_DE_RENDA = 0.15
DESCONTO_INSS = 0.08

nome = input("Insira seu nome:\n")
filhos_quantidade = int(input("Quantos filhos possui? (Será creditado 150/filho, seja honesto) \n"))
filhos_adicional_valor = filhos_quantidade * FILHOS_ADICIONAL
idade = int(input("Insira sua idade:\n"))
salario = float(input("Insira seu salário antigo:\n"))
porcentagem_de_aumento = (1 + (int(input("De 0 a 100, digite qual a porcentagem de aumento:\n")) / 100))
salario_aumentado = salario * porcentagem_de_aumento
salario_final_com_deducoes = salario_aumentado - (salario_aumentado * (DESCONTO_INSS + DESCONTO_IMPOSTO_DE_RENDA))
Junior
print("\n\n\n\n\n\n\n\n", nome, " tem ", idade,
      " anos de idade e recebia R$", salario,
      ".\nCom o aumento, passou a receber R$",
      salario * porcentagem_de_aumento,
      ", além disso,\nreceberá também um adicional por filho que totaliza: ",
      filhos_quantidade * FILHOS_ADICIONAL,
      ".\nPortanto receberá um valor total de R$",
      filhos_adicional_valor + salario_aumentado,
      ".\n\nNo mês de férias, receberá um adicional de ", (salario_aumentado / 3), ", totalizando R$",
      salario_aumentado + (salario_aumentado / 3),
      sep="", end=".\n\n"
      )
print("Serão descontados os seguintes valores: \n\n",
      "Desconto INSS: R$", DESCONTO_INSS * salario_aumentado,
      "\nDesconto do Imposto de Renda: R$", DESCONTO_IMPOSTO_DE_RENDA * salario_aumentado,
      "\n\nRestará, após as deduções o valor a receber de R$",
      salario_aumentado - DESCONTO_IMPOSTO_DE_RENDA * salario_aumentado - DESCONTO_INSS * salario_aumentado,
      sep="", end=".\n\n\n\n"
      )
