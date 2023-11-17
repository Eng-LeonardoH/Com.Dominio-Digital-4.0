import mysql.connector

#Conexão:
bd_academia = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
)
print (bd_academia)#Retorna o endereço de memória da conexão.

# Alterar dados em alunos:
nome_novo = "Aluno01"
telefone_novo = "22222222222"
endereco_novo = "Rua do Jaboticabal, Nº666, Junta de Seu Jorge, Maranguapaticatu, Alagoas, Brasil"

# Criar variável de comando UPDATE SQL
sql_command = "UPDATE alunos SET nome = %s, telefone = %s, endereco = %s WHERE nome = %s"

# Criar um cursor e executar a query com os novos dados e o nome do aluno a ser atualizado.
bd_cursor = bd_academia.cursor()
data = (nome_novo, telefone_novo, endereco_novo, "Aluno00")
# Executar comando
bd_cursor.execute(sql_command, data)
bd_academia.commit()

# Fechar o cursor e a conexão com o banco de dados
bd_cursor.close()
bd_academia.close()