"""
agendamentos
"""
agendamentos = []

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
    
    mostrar_horarios()
    
    horario_id = int(input("\nDigite o número do horário que deseja agendar: "))
    
    if horario_id not in horarios:
        print("Horário inválido. Tente novamente.")
        return

    #verifica se o horario ja foi reservado
    for agendamento in agendamentos:
        if agendamento["horario"] == horarios[horario_id]:
            print("Horário já reservado. Tente outro horário.")
            return

    novo_agendamento = {
        "servico": servicos[servico_id]["nome"],
        "preco": servicos[servico_id]["preco"],
        "horario": horarios[horario_id]
    }

    agendamentos.append(novo_agendamento)

    print(f"\nAgendamento confirmado: {servicos[servico_id]['nome']} às {horarios[horario_id]}.")
    print(f"Preço: R${servicos[servico_id]['preco']:.2f}")

#lista de agendamentos
def listar_agendamentos():
    
    print("\n--- Lista de Agendamentos ---")
    
    if len(agendamentos) == 0:
        print("\nNenhum agendamento encontrado.")
        return

    for i, agendamento in enumerate(agendamentos):
        print(f"{i+1}. {agendamento['servico']} às {agendamento['horario']} - R${agendamento['preco']:.2f}")    


#remover agendamento
def remover_agendamento():
    listar_agendamentos()
    
    if len(agendamentos) == 0:
        return

    agendamento_id = int(input("\nDigite o número do agendamento que deseja remover: "))
    
    if agendamento_id < 1 or agendamento_id > len(agendamentos):
        print("Agendamento inválido. Tente novamente.")
        return

    agendamento_removido = agendamentos.pop(agendamento_id - 1)
    print(f"\nAgendamento removido: {agendamento_removido['servico']} às {agendamento_removido['horario']} - R${agendamento_removido['preco']:.2f}")
    