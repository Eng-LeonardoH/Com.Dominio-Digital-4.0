# Algoritmo que escreve o conteúdo de um vetor e o reproduz em ordem invertida.
A = [2, 5, 4, 2, 8, 5, 2]
B = []
contador = 0


for i in (A):
    contador += 1

print(B)

for i in range(contador):
    B.append(A[contador - i -1])

print(B)
