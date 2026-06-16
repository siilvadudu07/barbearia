#conexão com o sqlite3
import sqlite3

from agendamento import servicos, horarios, agendamentos

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

import datetime

def registrar_servico_banco(id_funcionario, id_servico):
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()
    
    # buscar o funcionário
    cursor.execute("SELECT nome, comissao FROM funcionarios WHERE id = ?", (id_funcionario,))
    funcionario = cursor.fetchone()
    
    if funcionario:
        nome_func, comissao_porcentagem = funcionario
        servico_nome = servicos[id_servico]['nome']
        valor_servico = servicos[id_servico]['preco']
        
        # Calculo do valor que vai pro barbeiro
        valor_comissao = valor_servico * (comissao_porcentagem / 100)
        data_atual = datetime.date.today().strftime("%d/%m/%Y") #tranfsforma a data no formato dia/mes/ano
        
        # Insere no histórico
        cursor.execute('''
            INSERT INTO servicos_realizados (funcionario_id, servico_nome, valor_servico, valor_comissao, data_registro)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_funcionario, servico_nome, valor_servico, valor_comissao, data_atual))
        
        conexao.commit()
        print(f"Sucesso! R${valor_comissao:.2f} de comissão gerada para {nome_func}.")
    else:
        print("Funcionário não encontrado.")
    conexao.close()

def servicosparacadastrar():
    print("Serviços disponíveis para cadastro:")
    print("1. Corte de Cabelo")
    print("2. Corte só a lateral")
    print("3. Barba")
    print("4. Corte + Barba")
    print("5. Corte Infantil")
    print("6. Pintura")
    print("7. Sobrancelha")


#funcionário
def funcionarios():
    while True:
        nome = input("Digite o nome do funcionário: ")
        servicosparacadastrar()
        especialidade = int(input("Digite o número da especialidade do funcionário: "))
        if especialidade == 1:
            especialidade = "Corte de Cabelo"
        elif especialidade == 2:
            especialidade = "Corte só a lateral"
        elif especialidade == 3:
            especialidade = "Barba"
        elif especialidade == 4:
            especialidade = "Corte + Barba"
        elif especialidade == 5:
            especialidade = "Corte Infantil"
        elif especialidade == 6:
            especialidade = "Pintura"
        elif especialidade == 7:
            especialidade = "Sobrancelha"
        else:
            print("Especialidade inválida. Tente novamente.")
            continue
        comissao = float(input("Digite a comissão do funcionário (em %): "))

        conexao = sqlite3.connect('barbearia.db')
        cursor = conexao.cursor()

        cursor.execute("""
                    INSERT INTO funcionarios (nome, especialidade, comissao)
                        VALUES (?, ?, ?)
                    """, (nome, especialidade, comissao))
        conexao.commit()
        conexao.close()

        print("Funcionário cadastrado com sucesso!")

        continuar = input("Deseja cadastrar outro funcionário? (sim/não): ").lower
        if continuar != 'sim':
            break

#criar banco de dados para armazenar as comissões semanais dos funcionários
def banco_comissoes():
    conexao = sqlite3.connect('comissoes.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comissoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_funcionario TEXT NOT NULL,
            valor_comissao REAL NOT NULL,
            data TEXT NOT NULL
        )
    ''')

    for agendamento in agendamentos:
        nome_funcionario = agendamento['funcionario']
        id_servico = agendamento['servico']
        valor_servico = servicos[id_servico]['preco']
        comissao_funcionario = 0.0

        conexao_comissao = sqlite3.connect('barbearia.db')
        cursor_comissao = conexao_comissao.cursor()
        cursor_comissao.execute("SELECT comissao FROM funcionarios WHERE nome = ?", (nome_funcionario,))
        resultado = cursor_comissao.fetchone()
        if resultado:
            comissao_funcionario = resultado[0]
        conexao_comissao.close()

        valor_comissao = valor_servico * (comissao_funcionario / 100)
        data_agendamento = agendamento['data']

        cursor.execute("""
            INSERT INTO comissoes (nome_funcionario, valor_comissao, data)
            VALUES (?, ?, ?)
        """, (nome_funcionario, valor_comissao, data_agendamento))
    conexao.commit()
    conexao.close()

#visualizar funcionários
def visualizar_funcionarios():
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    if funcionarios:
        print("\nFuncionários Cadastrados:")
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Especialidade: {funcionario[2]}, Comissão: {funcionario[3]}%")
    else:
        print("Nenhum funcionário cadastrado.")

    conexao.close()


#excluir funcionário
def excluir_funcionario():
    visualizar_funcionarios()
    id_excluir = int(input("Digite o ID do funcionário que deseja excluir: "))

    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_excluir,))

    conexao.commit()
    conexao.close()

    print("Funcionário excluído com sucesso!")

def calcular_comissao():
    visualizar_funcionarios()
    try: 
        id_funcionario = int(input("Digite o ID do funcionário que realizou o serviço: "))
        conexao = sqlite3.connect('barbearia.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, especialidade, comissao FROM funcionarios WHERE id = ?", (id_funcionario,))
        funcionario = cursor.fetchone()
        conexao.close()
        if funcionario:
            nome = funcionario[0]
            especialidade = funcionario[1]
            comissao_funcionario = funcionario[2]
            print(f"Funcionário: {nome}, Especialidade: {especialidade}, Comissão: {comissao_funcionario}%")
            print("Serviços disponíveis:")
            for id, servico in servicos.items():
                print(f"{id}. {servico['nome']} - R${servico['preco']:.2f}")
            id_servico = int(input("Digite o ID do serviço realizado: "))
            if id_servico in servicos:
                valor_servico = servicos[id_servico]['preco']
                calculo_comissao = valor_servico * (comissao_funcionario / 100)
                print(f"A comissão do funcionário é: R${calculo_comissao:.2f}")
            else:
                print("Serviço não encontrado.")
        else:
            print("Funcionário não encontrado.")
    except ValueError:
        print("ID inválido. Por favor, digite um número inteiro.")