import mysql.connector

#Conexão:
bd_academia = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
) #O Comando não reproduz nada
#print (banco)#Retorna o endereço de memória da conexão.

#criar dados em alunos:
nome="Aluno00"
telefone="111111111"
endereco = "Logradouro, Nº000, Bairro, Cidade, Estado, País"

# Utilizar placeholders na query SQL
sql_command = "INSERT INTO alunos(nome, telefone, endereco) VALUES (%s, %s, %s)"

# Criar um cursor e executar a query com os dados fornecidos
bd_cursor = bd_academia.cursor()
data = (nome, telefone, endereco)

bd_cursor.execute(sql_command, data)
bd_academia.commit()

userid = bd_cursor.lastrowid
print(userid)

# Fechar o cursor e a conexão com o banco de dados
bd_cursor.close()
bd_academia.close()