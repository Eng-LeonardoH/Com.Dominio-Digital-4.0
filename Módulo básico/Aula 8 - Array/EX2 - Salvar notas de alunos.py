soma = 0.0
media = 0.0
qtd_notas = 5
qtd_alunos_acima_media = 0
notas_aluno = [0,1,2,3,4]
for i in range(qtd_notas): #Preenchimento da lista
    notas_aluno[i] = float(input(f"Digite a {i+1}ª nota: "))
    while notas_aluno[i] > 10 or notas_aluno[i]< 0:
        notas_aluno[i] = float(input(f"Nota inválida!\nDigite a {i + 1}ª nota: "))
for i in range(qtd_notas): #Soma dos valores da lista
    soma += notas_aluno[i]
media = soma/qtd_notas
print(f"A media é {media}")
for i in range(qtd_notas): #Contagem de alunos aprovados
    if notas_aluno[i] >= media:
        qtd_alunos_acima_media += 1
print(f"A quantidade de alunos aprovados por média é: {qtd_alunos_acima_media}")
