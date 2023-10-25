# 8. Faça um código que receba 4 números e realize a soma deles e
# a média entre eles. e mostre os resultados.

#Ajuste para permitir ao usuário escolher com quantos valores deseja entrar

entrada = float(input("Digite o 1º valor que deseja processar: "))
while entrada == 0:
    entrada = float(input("O 1º valor não pode ser zero. Tente novamente: "))

soma = entrada
contador = 1

while entrada != 0:
    contador += 1
    entrada = float(input(f"Digite o {contador}º valor que deseja processar (Digite 0 para parar): "))
    soma += entrada
media = soma / contador
print(f"A soma dos números é {soma} e a média é {media:,.2f}")
