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
    while True:
        nome = input("Digite o nome do funcionário: ")
        especialidade = input("Digite a especialidade do funcionário: ")
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
    id_excluir = int(input("Digite o ID do funcionário que deseja excluir: "))

    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_excluir,))

    conexao.commit()
    conexao.close()

    print("Funcionário excluído com sucesso!")