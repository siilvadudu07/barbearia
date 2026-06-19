"""
agendamentos
"""
agendamentos = []
import sqlite3

#-MÓDULO 3-
#serviços disponíveis
servicos = {
    1: {"nome": "Corte de Cabelo", "preco": 30.0},
    2: {"nome": "Corte só a lateral", "preco": 25.0},
    3: {"nome": "Barba", "preco": 15.0},
    4: {"nome": "Corte + Barba", "preco": 40.0},
    5: {"nome": "Corte Infantil", "preco": 15.0},
    6: {"nome": "Pintura", "preco": 75.50},
    7: {"nome": "Sobrancelha", "preco": 10.0}
}

#ajeitar o banco de dados para incluir os serviços e os horários disponíveis, para que o barbeiro possa escolher quais serviços ele oferece e quais horários ele tem disponível para agendamento. Assim, quando o cliente for agendar um serviço, ele poderá escolher entre os serviços e horários disponíveis do barbeiro específico. 


#-MÓDULO 2-
#horários disponíveis
horarios = {
    1: "09:00",
    2: "10:00",
    3: "11:00",
    4: "12:00",
    5: "13:00",
    6: "14:00",
    7: "15:00",
    8: "16:00",
    9: "17:00",
    10: "18:00",
    11: "19:00",
    12: "20:00",
    13: "21:00",
}

#mostrar serviços disponíveis
def mostrar_servicos():
    print("\nServiços disponíveis:---")
    for id, servico in servicos.items():
        print(f"{id}. {servico['nome']} - R${servico['preco']:.2f}")

#mostrar horários disponíveis
def mostrar_horarios():
    print("\nHorários disponíveis:")
    for id, horario in horarios.items():
        print(f"{id}. {horario}")

#função para agendar um serviço
def agendar_servico():
    mostrar_servicos()
    servico_id = int(input("\nDigite o número do serviço que deseja agendar: "))
    
    if servico_id not in servicos:
        print("Serviço inválido. Tente novamente.")
        return
        
    nome_servico_escolhido = servicos[servico_id]["nome"]

    # conecta no banco para buscar os barbeiros com essa especialidade
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM funcionarios WHERE especialidade = ?", (nome_servico_escolhido,))
    barbeiros_disponiveis = cursor.fetchall()
    conexao.close()

    if not barbeiros_disponiveis:
        print(f"\nDesculpe, não temos nenhum barbeiro disponível especializado em: {nome_servico_escolhido}.")
        return

    # mostra os barbeiros que podem fazer o serviço para o cliente escolher ANTES do horário
    print("\nBarbeiros disponíveis para este serviço:")
    for b in barbeiros_disponiveis:
        print(f"ID: {b[0]} - Nome: {b[1]}")
    
    id_barbeiro_escolhido = int(input("Digite o ID do barbeiro que prefere: "))

    # Valida se o ID digitado é de um barbeiro que realmente faz o serviço
    ids_validos = [b[0] for b in barbeiros_disponiveis]
    if id_barbeiro_escolhido not in ids_validos:
        print("ID de barbeiro inválido para este serviço.")
        return

    # mostra e escolhe o horário
    mostrar_horarios()
    horario_id = int(input("\nDigite o número do horário que deseja agendar: "))
    
    if horario_id not in horarios:
        print("Horário inválido. Tente novamente.")
        return

    horario_escolhido = horarios[horario_id]

#Verifica se o horário já está reservado para ESSE barbeiro
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM agendamentos WHERE horario = ? AND barbeiro_id = ?", (horario_escolhido, id_barbeiro_escolhido))
    conflito = cursor.fetchone()

    if conflito:
        print("\nEste barbeiro já tem um agendamento nesse horário! Escolha outro profissional ou horário.")
        conexao.close()
        return

    # salva diretamente no banco de dados
    cursor.execute('''
        INSERT INTO agendamentos (servico, preco, horario, barbeiro_id)
        VALUES (?, ?, ?, ?)
    ''', (nome_servico_escolhido, servicos[servico_id]["preco"], horario_escolhido, id_barbeiro_escolhido))
    
    conexao.commit()
    conexao.close()
    
    print(f"\nAgendamento confirmado no Banco de Dados: {nome_servico_escolhido} às {horario_escolhido}!")

#lista de agendamentos
def listar_agendamentos():
    
    print("\n--- Lista de Agendamentos ---")
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT agendamentos.id, agendamentos.servico, agendamentos.horario, agendamentos.preco, funcionarios.nome 
        FROM agendamentos 
        INNER JOIN funcionarios ON agendamentos.barbeiro_id = funcionarios.id 
    ''') #inner join = combina os dados das duas tabelas para mostrar o nome do barbeiro junto com o agendamento
    todos_agendamentos = cursor.fetchall()
    conexao.close()

    if len(todos_agendamentos) == 0:
        print("\nNenhum agendamento encontrado.")
        return

    for agendamento in todos_agendamentos:
        id_agend, servico, hora, preco, nome_barbeiro = agendamento
        print(f"{id_agend}. {servico} às {hora} - R${preco:.2f} (Barbeiro: {nome_barbeiro})")
    return len(todos_agendamentos)


#remover agendamento
def remover_agendamento():
    qtd = listar_agendamentos()
    
    if qtd == 0:
        return

    id_remover = int(input("\nDigite o ID Ref do agendamento que deseja remover(Enter para sair): "))
    
    conexao = sqlite3.connect('barbearia.db')
    cursor = conexao.cursor()
    
    # Verifica se esse ID existe antes de deletar
    cursor.execute("SELECT servico FROM agendamentos WHERE id = ?", (id_remover,))
    existe = cursor.fetchone()
    
    if not existe:
        print("ID de agendamento não encontrado.")
        conexao.close()
        return

    cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id_remover,))
    conexao.commit()
    conexao.close()
    
    print(f"\nAgendamento ID {id_remover} removido com sucesso do sistema!")
    

