# 7. Faça um código que receba o valor da base e da altura de um triângulo e
# calcule sua área. usando a fórmula A =(base x Altura ) /2

base = float(input("Digite o tamanho da base: "))
while base == 0:
    base = float(input("O tamanho da base não pode ser zero... Digite outro valor: "))

altura = float(input("Digite o tamanho da altura: "))
while altura == 0:
    altura = float(input("O tamanho da altura não pode ser zero... Digite outro valor: "))

area = (base * altura) / 2
print(f"A área do triangulo é {area} m².")
