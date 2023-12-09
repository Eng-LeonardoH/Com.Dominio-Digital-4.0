# Programa para er 10 numeros e responder com a soma dos números digitados

# Início do programa
soma = 0

# Processamento

print("Digite uma sequência de dez números para ver a soma:")
for contador in range(10):
    soma = soma + float(input(f"Digite o {contador + 1}º Numero: \n"))

print(f"A soma dos valores é: {soma}")

# Fim do Programa
