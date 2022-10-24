import mysql.connector

def criar_tabela(nome, campos):
    comando = f"CREATE TABLE {nome} (ID int AUTO_INCREMENT, )"
    for campo in campos:
        comando += f"{campo} varchar"
    
    cursor.execute(comando)
    return None

dados = input("Digite o nome do host, o usuário e a senha: ")
dados = dados.split(" ")
host = dados[0]
user = dados[1]
password= dados[2]

try:
    connection = mysql.connector.connect(
        host = host,
        user= user,
        password= password
    )
except:
    print("F deu erro")

cursor = connection.cursor()
try:
    database = input("Informe o nome da nova base dados: ")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

    connection.database = database

    nova_tabela = input("Digite o nome da tabela e a quantidade de campos: ")
    nova_tabela = nova_tabela.split(" ")
    nome_tabela = nova_tabela[0]
    campos_tabela = int(nova_tabela[1])
    criar_tabela(nome_tabela, campos_tabela)
except:
    print("Erro")

