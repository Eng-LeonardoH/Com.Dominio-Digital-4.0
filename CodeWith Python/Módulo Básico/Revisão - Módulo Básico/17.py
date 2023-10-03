#17.As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00
#se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
#compradas, calcule e escreva o custo total da compra.

preco_maca_unidade = 1.3
preco_maca_varejo = 1.0
qtd_maca = int(input("Digite a quantidade de maçãs compradas: "))
custo_total = 0.0

if qtd_maca >= 12:
    custo_total = qtd_maca * preco_maca_varejo
else:
    custo_total = qtd_maca * preco_maca_unidade
print(f"As maçãs custaram R${custo_total:,.2f}.")