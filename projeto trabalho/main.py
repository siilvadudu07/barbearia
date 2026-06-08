"""
main - integração
"""
from cadastro_funcionario import funcionarios, visualizar_funcionarios, excluir_funcionario

from agendamento import mostrar_horarios, mostrar_servicos, listar_agendamentos, remover_agendamento


def mostrar_menu():
    print("\nMenu Principal")
    print("1. Cadastrar Funcionário")
    print("2. Visualizar Funcionários")
    print("3. Excluir Funcionário")
    print("4. Mostrar Horários Disponíveis")
    print("5. Mostrar Serviços Disponíveis")
    print("6. Listar Agendamentos")
    print("7. Remover Agendamento")
    print("0. Sair")


def menuprincipal():
    while True:
        mostrar_menu()
        opcao = int(input("Qual ação você deseja realizar? (Digite o número): "))
        if opcao == 1:
            funcionarios() 
        elif opcao == 2:
            visualizar_funcionarios()
        elif opcao == 3:
            excluir_funcionario()
        elif opcao == 4:
            mostrar_horarios()
        elif opcao == 5:
            mostrar_servicos()
        elif opcao == 6:
            listar_agendamentos()
        elif opcao == 7:
            remover_agendamento()
        elif opcao == 0:
            print("Obrigadp por usar o sistema da barbearia! Até a próxima!")
            break  # Encerra o looping e fecha o programa
        else:
            print("Opção inválida! Digite um número de 0 a 7")


menuprincipal()

    
