import mysql.connector
#Conexão:
bd_academia = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
) #O Comando não reproduz nada

opcao = "0"
while opcao != "1" or opcao != "2" or opcao!= "3" or opcao!= "4": # Validação da entrada do usuário
    opcao = str(input("\n\n\nEscolha uma opção:\n"
                  "1 para CREATE\n"
                  "2 PARA READ\n"
                  "3 PARA UPDATE\n"
                  "4 PARA DELETE\n"
                  "5 PARA ENCERRAR A CONEXÃO COM O BD\n"
                  "Digite: "))
    if opcao == "1": # Cria o aluno00 na tabela alunos
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
        Object = bd_cursor.lastrowid
        print(f"O número de ordem do objeto criado é {Object}.")
        # Fechar o cursor
        bd_cursor.close()
        opcao = 0
    elif opcao == "2": # ler tabela alunos:
        # Criar query SQL
        sql_command = "select * from alunos"
        bd_cursor = bd_academia.cursor()
        # Executar comando e coletar resposta
        bd_cursor.execute(sql_command)
        resposta = bd_cursor.fetchall()
        print("Segue os dados constantes na tabela alunos:\n")
        for x in resposta:
            print(x)
        # Fechar o cursor
        bd_cursor.close()
        opcao = 0
    elif opcao == "3": # Altera Aluno00 para Aluno01 e muda seu endereço e telefone dentro da tabela alunos:
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
        # Fechar o cursor
        bd_cursor.close()
        opcao = 0
    elif opcao == "4":
        # Deleta Aluno01 da tabela alunos:
        nome = "Aluno01"
        # Utilizar placeholders na query SQL
        sql_command = "DELETE FROM alunos WHERE nome = %s"
        # Criar um cursor e executar a query
        bd_cursor = bd_academia.cursor()
        bd_cursor.execute(sql_command, (nome,))
        bd_academia.commit()
        userid = bd_cursor.lastrowid
        print(userid)
        # Fechar o cursor
        bd_cursor.close()
        opcao = 0
    elif opcao == "5":
        try:
            if bd_cursor:  # Verifica se o cursor está definido
                bd_cursor.close()
                opcao = "0"
            if bd_academia:  # Verifica se a conexão está definida
                bd_academia.close()
                opcao ="0"
            print("Conexão Encerrada.")
        except NameError as e:
            print("Erro ao fechar conexão:", e)
