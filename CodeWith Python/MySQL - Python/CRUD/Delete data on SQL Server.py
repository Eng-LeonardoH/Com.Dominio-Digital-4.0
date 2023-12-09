import mysql.connector

#Conexão:
bd_academia = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
) #O Comando não reproduz nada
#print (banco)#Retorna o endereço de memória da conexão.

# Deleta Aluno01 da tabela alunos:
nome="Aluno01"

# Utilizar placeholders na query SQL
sql_command = "DELETE FROM alunos WHERE nome = %s"

# Criar um cursor e executar a query
bd_cursor = bd_academia.cursor()
bd_cursor.execute(sql_command, (nome,))
bd_academia.commit()

userid = bd_cursor.lastrowid
print(userid)

# Fechar o cursor e a conexão com o banco de dados
bd_cursor.close()
bd_academia.close()