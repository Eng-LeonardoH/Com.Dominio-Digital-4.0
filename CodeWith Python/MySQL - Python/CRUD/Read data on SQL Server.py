import mysql.connector

#Conexão:
bd_academia = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
) #O Comando não reproduz nada
# print (banco)#Retorna o endereço de memória da conexão.

# ler tabela alunos:

# Criar query SQL
sql_command = "select * from alunos"
bd_cursor = bd_academia.cursor()

# Executar comando e coletar resposta
bd_cursor.execute(sql_command)
resposta = bd_cursor.fetchall()
for x in resposta:
    print(x)

# Fechar o cursor e a conexão com o banco de dados
bd_cursor.close()
bd_academia.close()
