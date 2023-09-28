Algoritmo "Processamento de notas"
// Disciplina   : Desafio - Estruturas condicionais
// Professor   : Wellington de Moraes Oliveira
// Descrição   : Programa para analisar a média do aluno e reportar
//               sua situação em relação média.
// Autor(a)    : Leonardo Henrique Araujo de Melo  < LEONARDO >
// Data atual  : 02/09/2023
Var

media_aluno: inteiro

Inicio

escreva("Digite a média do aluno: ")
leia(media_aluno)

se(media_aluno >= 7)    então
escreva("APROVADO")
senao
se(media_aluno >= 5)então
escreva("RECUPERAÇÃO")
senao
escreva("REPROVADO")
fimse
fimse

Fimalgoritmo
