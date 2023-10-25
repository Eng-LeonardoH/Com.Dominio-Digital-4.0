entrada_numero1 = 5
entrada_numero2 = 5
for contador in range(entrada_numero1 + 1):
    print(contador * str(contador), end=" ")

print()
contador = 1
while contador <= entrada_numero2:
    print(contador * str(contador), end=" ")
    contador += 1
