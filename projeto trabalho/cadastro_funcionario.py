#conexão com o sqlite3
import sqlite3

#função para conectar ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()

    #cria a tabela de funcionários no banco de dados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            comissao REAL NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()


profissionais = {}
contador_id = 1

#funcionário
def funcionarios():
    global contador_id
    while True:
        # Solicitar informações do funcionário
        print("\n CADASTRO DE FUNCIONÁRIOS")
        nome = input("Digite o nome do funcionário: ")
        especialidade = input("Digite a especialidade do funcionário: ")
        comissao = float(input("Digite a comissão do funcionário: "))
        profissionais[contador_id] = {"nome": nome, "especialidade": especialidade}
        
        #adiciona funcionario ao dicionário de profissionais
        profissionais[contador_id] = {
            "nome": nome,
            "especialidade": especialidade,
            "comissao": comissao
            }

        print("Funcionário cadastrado com sucesso!")
        contador_id += 1

        #perguntar se deseja cadastrar outro funcionário
        continuar = input("Deseja cadastrar outro funcionário? (sim/nao): ")
        continuar = continuar.lower()
        if continuar != "sim":
            break

#visualizar funcionários
def visualizar_funcionarios():
    
    if not profissionais:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\n FUNCIONÁRIOS CADASTRADOS")
        
        for id, info in profissionais.items():
            print(f"ID: {id}, Nome: {info['nome']}, Especialidade: {info['especialidade']}, Comissão: {info['comissao']}%")

#excluir funcionário
def excluir_funcionario():
    
    id_excluir = int(input("Digite o ID do funcionário que deseja excluir: "))
    
    if id_excluir in profissionais:
        del profissionais[id_excluir]
        print("Funcionário excluído com sucesso!")
    else:
        print("ID de funcionário não encontrado.")
    
    print("\n FUNCIONÁRIOS ATUALIZADOS")
    visualizar_funcionarios()

funcionarios()
visualizar_funcionarios()
excluir_funcionario()