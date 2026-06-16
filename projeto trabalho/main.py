"""
main - integração
"""
from cadastro_funcionario import banco_comissoes, calcular_comissao, conectar_banco, funcionarios, visualizar_funcionarios, excluir_funcionario, banco_comissoes
from agendamento import mostrar_horarios, mostrar_servicos, listar_agendamentos, remover_agendamento, agendar_servico

conectar_banco()

def retorno():
    print("Digite 0 para voltar ao menu principal")
    if input() == "0":
        menuprimeiro()

def menuprimeiro():
    print("Você é cliente ou barbeiro?")
    print("1.Cliente")
    print("2.Barbeiro")
    funcao = int(input("Digite 1 ou 2: "))
    if funcao == 1:
        menucliente()
    elif funcao == 2:
        menubarbeiro()
    else:
        print("Opção inválida! Digite 1 para cliente ou 2 para barbeiro.")

def mostrar_menucliente():
    print("\nOlá cliente! Bem-vindo ao sistema de agendamento da barbearia.")
    print("1. Mostrar Horários Disponíveis")
    print("2. Mostrar Serviços Disponíveis")
    print("3. Listar Agendamentos")
    print("4. Agendar um Serviço")
    print("0. Retornar ao Menu Principal")
    
def menucliente():
    mostrar_menucliente()
    opcao = int(input("Qual ação você deseja realizar? (Digite o número): "))
    if opcao == 1:
        mostrar_horarios()
        retorno()
        
    elif opcao == 2:
        mostrar_servicos()
        retorno()
    elif opcao == 3:
        listar_agendamentos()
        retorno()
    elif opcao == 4:
        agendar_servico()
        retorno()
    elif opcao == 0:
        print("Obrigado por usar o sistema da barbearia! Até a próxima!")
        retorno()
    else:
        print("Opção inválida! Digite um número de 0 a 4")

def mostrar_menubarbeiro():
    print("Menu Principal")
    print("1. Cadastrar Funcionário")
    print("2. Visualizar Funcionários")
    print("3. Excluir Funcionário")
    print("4. Mostrar Horários Disponíveis")
    print("5. Mostrar Serviços Disponíveis")
    print("6. Listar Agendamentos")
    print("7. Remover Agendamento")
    print("8. Calcular Comissão")
    print("9. Mostrar Comissão")
    print("0. Retornar ao Menu Principal")

def mostrar_comissao():
    banco_comissoes()

def menubarbeiro():
    while True:
        mostrar_menubarbeiro()
        opcao = int(input("Qual ação você deseja realizar? (Digite o número): "))

        if opcao == 1:
            funcionarios()
            retorno()
        elif opcao == 2:
            visualizar_funcionarios()
            retorno()
        elif opcao == 3:
            excluir_funcionario()
            retorno()
        elif opcao == 4:
            mostrar_horarios()
            retorno()
        elif opcao == 5:
            mostrar_servicos()
            retorno()
        elif opcao == 6:
            listar_agendamentos()
            retorno()
        elif opcao == 7:
            remover_agendamento()
            if len(listar_agendamentos()) == 0:
                print("Nenhum agendamento encontrado.")
                return menubarbeiro()
        elif opcao == 8:
            calcular_comissao()
            retorno()
        elif opcao == 9:
            mostrar_comissao()
            retorno()
        elif opcao == 0:
            print("Obrigadp por usar o sistema da barbearia! Até a próxima!")
            retorno()
            break  # Encerra o looping e fecha o programa
        else:
            print("Opção inválida! Digite um número de 0 a 7")

#começo
conectar_banco()
menuprimeiro()
