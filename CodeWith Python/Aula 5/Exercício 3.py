# Programa para ler 2 valores e dividir um pelo o outro

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
chance = 2

while numero2 == 0 and chance >= 0:
    numero2 = float(input(f"""
    O segundo número não pode ser zero!!!
    Você pode tentar mais {chance} vezes
    Digite outro número: 
    """))
    chance -= 1

else:
    if chance == 0:
        print("Erro!")
    else:
        divisao = numero1 / numero2
        print(f"A divisão entre {numero1} e {numero2} tem resultado: {divisao}")
