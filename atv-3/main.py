import mysql.connector

def verEstacionamento(cursor):
    # função de verificar o status de todas as vagas
    resultado = "+=========== VAGAS ===========+\n0 = vaga vazia | 1 = vaga ocupada"
    cursor.execute("SELECT * FROM vagas, pavimentos WHERE 'id_pavimento' = 'id';")
    for (id, id_pavimento, numero, ocupada) in cursor:
        resultado += f"\nID da vaga: {id} | Número da vaga: {numero} | ID do pavimento: {id_pavimento} | Status: {ocupada}"
    return resultado

# conexão com a base de dados
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
        password= password,
        database = 'estacionamento'
    )
except:
    print("F deu erro")

