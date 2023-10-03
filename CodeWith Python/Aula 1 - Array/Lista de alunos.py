#Perguntar ao usuário quantos alunos e salvar o nome de cada um deles

qtd_alunos = 3 #int(input("Digite a quantidade de alunos: "))
lista_alunos = []

for i in range(qtd_alunos):
    lista_alunos.append(input("Digite o nome do aluno: "))
for i in range(qtd_alunos):
    print(f"O valor da posição {i} da lista de alunos é {lista_alunos[i]} e corresponde ao {i+1}º aluno.")