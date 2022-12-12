import mysql.connector

# recolhe os dados necessários para se conectar
dados = input("Digite o nome do host, o usuário e a senha: ")
dados = dados.split(" ")
host = dados[0]
user = dados[1]
password= dados[2]

try:
    # cria a conexao
    connection = mysql.connector.connect(
        host = host,
        user= user,
        password= password
    )
except:
    print("F deu erro")

cursor = connection.cursor()
try:
    # cria a DB
    database = 'LPR'
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    connection.database = database

    # cria as tabelas veiculo, cruzamentos e leituras respec.
    cursor.execute("CREATE TABLE IF NOT EXIXTS veiculo (id int AUTO_INCREMENT PRIMARY KEY, marca varchar(30), modelo varchar(30), ano year, cor varchar(15), placa varchar(8))")
    cursor.execute("CREATE TABLE IF NOT EXISTS cruzamento (id int AUTO_INCREMENT PRIMARY KEY, rua1 varchar(40), rua2 varchar (40))")
    cursor.execute("CREATE TABLE IF NOT EXISTS leitura (id int AUTO_INCREMENT PRIMARY KEY, placa varchar(8), FOREIGN KEY(cruzamento_id) REFERENCES cruzamento(id))")
    
    cursor.close()
except Exception as erro:
    print(f"Erro: {erro}")

try:
    connection.database = database

    for x in range(10):
        # adiciona 10 carros
        placas = ["12345678","23456781","34567812","45678123","56781234","67812345","78123456","81234567","87654321","21438567"]
        cursor.execute(f"INSERT INTO veiculo(marca, modelo, ano, cor, placa) VALUES('toyota','corolla','1987','prata',{placas[x]})")

    for x in range(5):
        # adiciona 5 cruzamentos
        ruas1 = ["rua Pastel", "rua Bolo", "rua Docinho", "rua Fome", "rua Coxinha"]
        ruas2= ["rua Fome", "rua Coxinha", "rua Bolo", "rua Pastel", "rua Docinho"]
        cursor.execute(f'INSERT INTO cruzamento(rua1, rua2) VALUES({ruas1[x], ruas2[x]})')
    
    cursor.close()
except Exception as erro:
    print(f"Erro: {erro}")


# PARTE 2:

def add_leituras(leituras):
    # registra todas as leituras
    for id, placa in leituras.items():
        cursor.execute(f'INSERT INTO leitura(placa, cruzamento_id) VALUES({placa},{id})')

qtd_leituras = int(input("Quantas leituras foram realizadas? "))

leituras = {}

for x in range(qtd_leituras):
    leitura = input("Informe o ID do cruzamento e a placa do veículo: ")
    
    leitura.split(" ")
    id_cruzamento = leitura[0]
    placa_veiculo = leitura[1]

    leituras[id_cruzamento] = placa_veiculo

try:
    connection.database = database

    add_leituras(leituras)
    
    cursor.close()
except Exception as erro:
    print(f'Erro: {erro}')

connection.close()
