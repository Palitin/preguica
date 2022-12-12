import mysql.connector

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

cursor = connection.cursor()

def verEstacionamento():
    # função de verificar o status de todas as vagas
    resultado = "+=========== VAGAS ===========+\n0 = vaga vazia | 1 = vaga ocupada"
    cursor.execute("SELECT * FROM vagas")
    for (id, id_pavimento, numero, ocupada) in cursor:
        resultado += f"\nID da vaga: {id} | Número da vaga: {numero} | ID do pavimento: {id_pavimento} | Status: {ocupada}"
    return resultado

def verPavimentos():
    # mostra os pavimentos
    resultado = "+=========== PAVIMENTOS ===========+"
    cursor.execute("SELECT * from pavimentos")
    for (id, nome_pavimento) in cursor:
        resultado += f"\nID do pavimento: {id} | Pavimento: {nome_pavimento}"
    print(resultado)

def escolherPavimento(pavimento):
    # mostra as vagas de um pavimento específico
    resultado = f'+=========== VAGAS DO PAVIMENTO {pavimento} ===========+\n0 = vaga vazia | 1 = vaga ocupada'
    cursor.execute(f"SELECT * FROM vagas WHERE id_pavimento = {pavimento}")
    for (id, id_pavimento, numero, ocupada) in cursor:
        resultado += f"\nID da vaga: {id} | Número da vaga: {numero} | Status: {ocupada}"
    return resultado

def checarVaga(pavimento, numero_vaga):
    # mostra o status de uma vaga específica
    cursor.execute(f"SELECT id, id_pavimento, ocupada FROM vagas WHERE id_pavimento = {pavimento} AND numero = {numero_vaga}")
    for (id, id_pavimento, ocupada) in cursor:
        resultado = f"+====== STATUS DA VAGA ======+\nID: {id}\nPavimento: {id_pavimento}\nStatus da vaga: {ocupada}"
    return resultado

def verVagasLivres():
    # cria uma lista com vagas vazias
    vagas_vazias = []
    cursor.execute("SELECT id FROM vagas WHERE ocupada = 0")
    for (id) in cursor:
        id = str(id)
        id = id.replace(",", "")
        id = id.replace("(", "")
        id = id.replace(")", "")
        vagas_vazias.append(id)
    return vagas_vazias

def alterarVaga(id_vaga, vagas_vazias, passou):
    # altera o status de uma vaga para ocupada
    if id_vaga in vagas_vazias:
        cursor.execute(f"UPDATE vagas SET ocupada = 1 WHERE id = {id_vaga}")
        passou = True
    else:
        passou = False
    return passou

def esvaziarEstacionamento():
    # esvazia todas as vagas
    pergunta = input("Você tem certeza? s//n ")
    if pergunta == "s":
        cursor.execute("UPDATE vagas SET ocupada = 0")

try:
    while True:
        operacao = input("1- Ver status das vagas\n2- Ver pavimento\n3- Ver vaga\n4- Alterar status da vaga\n5- Esvaziar estacionamento\nDigite o número da operação: ")
        if operacao == '1':
            resultado = verEstacionamento()
        elif operacao == "2":
            verPavimentos()
            escolha = int(input(" \nDigite o ID do pavimento: "))
            resultado = escolherPavimento(escolha)
        elif operacao == "3":
            pavimento = int(input("Digite o pavimento: "))
            num_vaga = int(input("Digite o número da vaga: "))
            resultado = checarVaga(pavimento, num_vaga)
        elif operacao == "4":
            passou = False
            vagas_livres = verVagasLivres()
            while passou == False:
                id_vaga = input("Digite o ID da vaga: ")
                passou = alterarVaga(id_vaga, vagas_livres, passou)
            resultado = "Vaga atualizada."
        elif operacao == "5":
            esvaziarEstacionamento()
            resultado = "Estacionamento esvaziado com sucesso."
        else:
            break
        print(resultado)
except Exception as erro:
    print(f"Morreu aqui...\n{erro}")

cursor.close()
connection.close()
