# Programa para calcular o custo de combustível a partir da quantidade abastecida e do tipo de combustível.

# Início do Programa

# Variáveis
valor_gasolina = 5.8
valor_etanol = 4.9

# Entradas
combustivel_tipo = input("Insira G para gasolina ou E para etanol: ")

# Processamento
if combustivel_tipo == ("g" or "G"):
    combustivel_qtd = float(input("Digite a quantidade de litros que foram abastecidos :"))
    combustivel_custo = combustivel_qtd * valor_gasolina
    print(f"O Custo do combustível foi: R${combustivel_custo:,.2f}")
elif combustivel_tipo == ("e" or "E"):
    combustivel_qtd = float(input("Digite a quantidade de litros que foram abastecidos :"))
    combustivel_custo = combustivel_qtd * valor_etanol
    print(f"O Custo do combustível foi: R${combustivel_custo:,.2f}")
else:
    print("Ocorreu um erro na operação, reinicie e siga as orientações...")
# Fim do programa
