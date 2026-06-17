#conexão com o sqlite3
import sqlite3
import datetime

from agendamento import servicos, horarios


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
        cpf = input("Digite o CPF do funcionário: ")
        if len(cpf) != 11:
            print("CPF inválido. O CPF deve conter 11 dígitos. Tente novamente.")
            continue
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
                    INSERT INTO funcionarios (nome, cpf, especialidade, comissao)
                        VALUES (?, ?, ?, ?)
                    """, (nome, cpf, especialidade, comissao))
        conexao.commit()
        conexao.close()

        print("Funcionário cadastrado com sucesso!")

        continuar = input("Deseja cadastrar outro funcionário? (sim/não): ").lower()
        if continuar != 'sim':
            break
        elif continuar == 'sim':
            return funcionarios()

#criar banco de dados para armazenar as comissões semanais dos funcionários
def exibir_comissoes_banco():
    visualizar_funcionarios()
    try:
        id_funcionario = int(input("\nDigite o ID do barbeiro para ver o relatório de comissões: "))
        
        conexao = sqlite3.connect('barbearia.db')
        cursor = conexao.cursor()
        
        # Busca o nome do funcionário
        cursor.execute("SELECT nome FROM funcionarios WHERE id = ?", (id_funcionario,))
        funcionario = cursor.fetchone()
        
        if funcionario:
            nome_barbeiro = funcionario[0]
            
            # Busca todos os serviços que esse barbeiro realizou
            cursor.execute('''
                SELECT servico_nome, valor_servico, valor_comissao, data_registro 
                FROM servicos_realizados 
                WHERE funcionario_id = ?
            ''', (id_funcionario,))
            
            servicos_feitos = cursor.fetchall()
            
            print(f"\n********************************************")
            print(f"   EXTRATO DE COMISSÕES: {nome_barbeiro.upper()}   ")
            print(f"********************************************")
            
            if not servicos_feitos:
                print("Nenhum serviço realizado/salvo para este funcionário ainda.")
            else:
                total_comissao = 0.0
                for item in servicos_feitos:
                    servico, valor, comissao, data = item
                    total_comissao += comissao
                    print(f"Data: {data} | {servico} | Valor: R${valor:.2f} -> Comissão: R${comissao:.2f}")
                
                print(f"********************************************")
                print(f" TOTAL A RECEBER: R${total_comissao:.2f}")
                print(f"********************************************")
        else:
            print("Funcionário não encontrado.")
            
        conexao.close()
        
    except ValueError:
        print("ID inválido. Por favor, digite um número inteiro.")

#visualizar funcionários
def visualizar_funcionarios():
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    if funcionarios:
        print("\nFuncionários Cadastrados:")
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, CPF: {funcionario[2]}, Especialidade: {funcionario[3]}, Comissão: {funcionario[4]}%")
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
        id_funcionario = int(input("\nDigite o ID do funcionário que realizou o serviço: "))
        conexao = sqlite3.connect('barbearia.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, especialidade, comissao FROM funcionarios WHERE id = ?", (id_funcionario,))
        funcionario = cursor.fetchone()
        conexao.close()
        
        if funcionario:
            nome = funcionario[0]
            especialidade = funcionario[1]
            comissao_funcionario = funcionario[2]
            print(f"\nFuncionário: {nome} | Especialidade: {especialidade} | Comissão: {comissao_funcionario}%")
            
            # Mostra os serviços
            print("\nServiços disponíveis:")
            for id_s, servico in servicos.items():
                print(f"{id_s}. {servico['nome']} - R${servico['preco']:.2f}")
                
            id_servico = int(input("\nDigite o ID do serviço realizado: "))
            
            if id_servico in servicos:
                valor_servico = servicos[id_servico]['preco']
                calculo_comissao = valor_servico * (comissao_funcionario / 100)
                print(f"\nA comissão do funcionário é: R${calculo_comissao:.2f}")
                gravar = input("\nDeseja registrar e salvar essa comissão no banco de dados? (sim/não): ").lower()
                if gravar == 'sim' or gravar == 's':
                    registrar_servico_banco(id_funcionario, id_servico)
            else:
                print("Serviço não encontrado.")
        else:
            print("Funcionário não encontrado.")
            
    except ValueError:
        print("ID inválido. Por favor, digite um número inteiro.")