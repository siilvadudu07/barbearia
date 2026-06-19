import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()

    # tabela de funcionários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            comissao REAL NOT NULL
        )
    ''')
    
    # tabela de histórico de serviços realizados para comissão
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servicos_realizados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario_id INTEGER,
            servico_nome TEXT,
            valor_servico REAL,
            valor_comissao REAL,
            data_registro TEXT,
            FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
        )
    ''')

    # tabela de agendamentos dos clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            servico TEXT NOT NULL,
            preco REAL NOT NULL,
            horario TEXT NOT NULL,
            barbeiro_id INTEGER NOT NULL,
            FOREIGN KEY (barbeiro_id) REFERENCES funcionarios(id)
        )
    ''')
    
    conexao.commit()
    conexao.close()
    print("[Sistema] Banco de dados verificado/inicializado com sucesso!")