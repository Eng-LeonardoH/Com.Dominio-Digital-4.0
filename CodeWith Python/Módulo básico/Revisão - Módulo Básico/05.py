# 5. Crie um algoritmo que leia um número e diga se ele é par ou ímpar.

numero = int(input("Insira um número inteiro: "))
while numero == 0:
    numero = float(input("Número não pode ser zero... Digite um número: "))
if (numero % 2) == 1:
    print("O número informado é impar.")
else:
    print("O número informado é par.")
