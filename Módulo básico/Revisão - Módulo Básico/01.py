# 1. Faça um algoritmo que receba 2 notas e calcule a média aritmética

nota01 = float(input("Digite a 1ª nota: "))
while nota01 < 0 or nota01 > 10:
    nota01 = float(input("Valor inválido, insira um valor entre 0 e 10... Digite uma nota válida: "))
nota02 = float(input("Digite a 2ª nota: "))
while nota02 < 0 or nota02 > 10:
    nota02 = float(input("Valor inválido, insira um valor entre 0 e 10... Digite uma nota válida: "))
media = (nota01 + nota02) / 2
print(f"A média é {media}")
