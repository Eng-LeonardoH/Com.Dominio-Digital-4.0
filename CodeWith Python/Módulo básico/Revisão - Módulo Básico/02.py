# 2. Crie um código que leia um número diferente de zero e diga se este número é positivo ou negativo
numero = float(input("Digite um número: "))
while numero == 0:
    numero = float(input("Número não pode ser zero... Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
