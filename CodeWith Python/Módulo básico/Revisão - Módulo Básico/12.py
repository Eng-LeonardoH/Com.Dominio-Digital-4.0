#12. Escreva um algoritmo para ler o número total de eleitores de um
#município, o número de votos brancos, nulos e válidos. Calcular e escrever o
#percentual que cada um representa em relação ao total de eleitores.

total_eleitores_municipio = 100 #int(input("Digite o número de eleitores do município: "))
votos_brancos_municipio = 5 #int(input("Digite o número de votos brancos: "))
votos_nulos_municipio = 15 #int(input("Digite o número de nulos brancos: "))
votos_válidos_municipio = 80 #int(input("Digite o número de válidos brancos: "))
votos_válidos_percentual = 0
votos_nulos_percentual = 0
votos_brancos_percentual = 0
print("Do total de eleitores: ")
votos_brancos_percentual = 100 * (votos_brancos_municipio / total_eleitores_municipio)
print(f"Foram {votos_brancos_percentual:,.2f}% de votos nulos.")
votos_nulos_percentual = 100 * (votos_nulos_municipio / total_eleitores_municipio)
print(f"Foram {votos_nulos_percentual:,.2f}% de votos nulos.")
votos_válidos_percentual = 100 * (votos_válidos_municipio / total_eleitores_municipio)
print(f"Foram {votos_válidos_percentual:,.2f}% de votos nulos.")