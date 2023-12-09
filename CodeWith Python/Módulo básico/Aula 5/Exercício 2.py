# programa para receber 10 números e mostrar a média


contador = 1
qtd_numeros = int(input("Digite a quantidade de números que deseja saber a média: "))
soma = 0.0

while contador <= qtd_numeros:
    soma += float(input(f"Digite o {contador}º número: "))
    contador += 1

soma = soma / (contador - 1)
print(f"A média dos {contador - 1} valores digitados é: {soma}...")
