# 8. Faça um código que receba 4 números e realize a soma deles e
# a média entre eles. e mostre os resultados.

#Ajuste para permitir ao usuário escolher com quantos valores deseja entrar

qtd_numeros = int(input("Digite quantos valores deseja processar: "))
soma = 0.0
entrada = 0.0

for i in range (1,entrada +1):
    entrada = float(input(f"Digite o {i}º número: "))
    soma += entrada

media = soma / qtd_numeros
print(f"A soma dos números é {soma} e a média é {media:,.2f}.")
