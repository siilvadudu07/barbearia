"""
main - integração
"""
from banco import inicializar_banco
from cadastro_funcionario import exibir_comissoes_banco, calcular_comissao, funcionarios, visualizar_funcionarios, excluir_funcionario, registrar_servico_banco
from agendamento import mostrar_servicos, mostrar_horarios, agendar_servico, listar_agendamentos, remover_agendamento

# Inicia o banco de dados antes de tudo
inicializar_banco()

# Função para pausar a execução e esperar o usuário pressionar ENTER
def pausa():
    input("\nPressione ENTER para continuar...")

# --- MENUS DE CLIENTE ---
def mostrar_menucliente():
    print("\n--- ÁREA DO CLIENTE ---")
    print("1. Mostrar Horários Disponíveis")
    print("2. Mostrar Serviços Disponíveis")
    print("3. Listar Agendamentos")
    print("4. Agendar um Serviço")
    print("5. Remover Agendamento")
    print("0. Voltar ao Menu Principal")
    
def menucliente():
    while True:
        mostrar_menucliente()
        try:
            opcao = int(input("Qual ação você deseja realizar? (Digite o número): "))

            if opcao == 1:
                mostrar_horarios()
                pausa()
            elif opcao == 2:
                mostrar_servicos()
                pausa()
            elif opcao == 3:
                listar_agendamentos()
                pausa()
            elif opcao == 4:
                agendar_servico()
                pausa()
            elif opcao == 5:
                remover_agendamento()
                pausa()
            elif opcao == 0:
                break # Saíds do laço e volta pro menu principal
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Erro: Digite apenas números.")

def mostrar_menubarbeiro():
    print("\n--- ÁREA DO BARBEIRO ---")
    print("1. Cadastrar Funcionário")
    print("2. Visualizar Funcionários")
    print("3. Excluir Funcionário")
    print("4. Mostrar Horários")
    print("5. Mostrar Serviços")
    print("6. Listar Agendamentos")
    print("7. Remover Agendamento")
    print("8. Calcular e Gravar Comissão")
    print("9. Extrato de Comissões")
    print("0. Voltar ao Menu Principal")

def menubarbeiro():
    while True:
        mostrar_menubarbeiro()
        try:
            opcao = int(input("Qual ação você deseja realizar? (Digite o número): "))

            if opcao == 1:
                funcionarios()
                pausa()
            elif opcao == 2:
                visualizar_funcionarios()
                pausa()
            elif opcao == 3:
                excluir_funcionario()
                pausa()
            elif opcao == 4:
                mostrar_horarios()
                pausa()
            elif opcao == 5:
                mostrar_servicos()
                pausa()
            elif opcao == 6:
                listar_agendamentos()
                pausa()
            elif opcao == 7:
                remover_agendamento()
                pausa()
            elif opcao == 8:
                calcular_comissao()
                pausa()
            elif opcao == 9:
                exibir_comissoes_banco()
                pausa()
            elif opcao == 0:
                break # Saíds do laço e volta pro menu principal
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Erro: Digite apenas números.")

def iniciar_sistema():
    while True:
        print("   SISTEMA DE GESTÃO - BARBEARIA")
        print("-----------------------------------")
        print("1. Entrar como Cliente")
        print("2. Entrar como Barbeiro")
        print("0. Encerrar o Sistema")
        
        try:
            funcao = int(input("Digite 1, 2 ou 0: "))
            
            if funcao == 1:
                menucliente()
            elif funcao == 2:
                menubarbeiro()
            elif funcao == 0:
                print("\nObrigado por usar o sistema da barbearia! Até a próxima!\n")
                break # Quebra o laço principal, encerrando o programa
            else:
                print("Opção inválida! Digite 1, 2 ou 0.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

# O programa começa rodando esta função
iniciar_sistema()