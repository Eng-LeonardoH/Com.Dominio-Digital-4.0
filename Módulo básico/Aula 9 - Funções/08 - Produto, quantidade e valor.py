from biblioteca import valor_estoque

nome_produto = "Garrafa Pet reciclável" #input("Digite o nome do produto: ")
valor_unitario = 1.29 #float(input("Digite o valor unitário do produto: "))
qtd = 47 #int(input("Quantas unidades existem no estoque? "))

valor_total = valor_estoque(nome_produto, qtd, valor_unitario)
print(f"O Valor total é R${valor_total}")