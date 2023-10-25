# Programa para receber 10 numeros e exibir quantos são negativos
entrada1 = 0
somatorio = 0
qtd_negativos = 0

# Início do programa
for x in range(1, 11, 1):
    entrada1 = int(input(f"Digite o {x}º número:"))
    if entrada1 < 0:
        print(entrada1)
        qtd_negativos = qtd_negativos + 1
        somatorio = somatorio + entrada1

qtd_positivos = 10 - qtd_negativos
print(
    f"Foram digitados {qtd_negativos} números negativos. Eles somam {somatorio}. Dos números digitados, {qtd_positivos} foram positivos.")
# Fim do programa
