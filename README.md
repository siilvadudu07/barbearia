# barbearia
trabalho de Raciocínio Algoritmico

## 👥 Integrantes do Grupo
* [José Eduardo da Silva]
* [José Lucas]

## 📋 Visão Geral do Sistema
O objetivo principal deste sistema é automatizar o controle interno de uma barbearia. Ele gerencia os profissionais, os serviços disponíveis, o cadastro de produtos/bebidas e realiza a integração financeira dos atendimentos por meio de comandas, calculando automaticamente as comissões e o faturamento líquido do estabelecimento.

---

## 🛠️ Divisão de Módulos Implementados

### 🪒 Módulo 1: Cadastro de Profissionais
Gestão dos profissionais do salão (cabeleireiros e barbeiros) contendo os campos obrigatórios (ID, Nome Completo e Especialidade).
* Cadastrar novos profissionais (Nome, ID, CPF).
* Listar todos os profissionais ativos.
* Buscar profissional pelo nome ou ID.
* Remover profissionais do sistema.

### 📅 Módulo 2: Realização de Agendamentos
Focado na reserva de horários para a realização dos procedimentos escolhidos pelos clientes.
* Cadastrar novos agendamentos (armazenando Horário, Categoria e Preço).
* Mostrar os horários disponíveis.
* Remover agendamentos do sistema.

### ✂️ Módulo 3: Cadastro de Serviços
Gerencia o catálogo e menu de serviços oferecidos pela barbearia aos clientes.
* Controle de Código do Serviço, Nome do Serviço (tipo do corte, coloração) e Preço Base.

### 💰 Módulo de Integração: Fluxo de Caixa e Comanda
Responsável por unir os módulos anteriores, detalhar qual barbeiro realizou o serviço e calcular automaticamente a comissão do profissional e o valor final.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal utilizando o comando:
   ```bash
   python main.py

## guia de comandos Git

1. Para Enviar as Suas Alterações (Commit + Push)
Sempre que você terminar de alterar um código e quiser mandar para o GitHub, rode esta sequência de comandos:

git add .
git commit -m "Explique de forma curta o que você mudou"
git push origin main

--

2. Para Baixar as Alterações do Seu Colega (Git Pull)
Sempre rode este comando antes de começar a programar para garantir que seu código está atualizado com o do seu colega:

git pull origin main

## o que pode causar conflito no trabalho

1. Alterar a mesma linha do mesmo arquivo ao mesmo tempo.

Se você e o José Lucas abrirem o arquivo main.py e alterarem exatamente a linha 15, o Git vai entrar em conflito.

Exemplo: Você altera a linha 15 para print("Bem-vindo à Barbearia") e dá git push. O seu colega, na máquina dele, altera a mesma linha 15 para print("Menu Principal da Barbearia") e tenta dar git push. O Git vai travar o envio dele porque não sabe qual dos dois textos deve manter.

--

2. Um apagar um arquivo que o outro editou

Se você abrir o agendamento.py e passar horas melhorando a função de remover agendamentos, mas o seu colega (por achar que o arquivo não seria mais usado) deletar o arquivo agendamento.py e enviar isso para o GitHub antes de você. Quando você tentar enviar suas melhorias, o Git vai dizer: "Ei, um quer atualizar o arquivo e o outro apagou ele. O que eu faço?"

--

3. Esquecer de dar git pull antes de começar a programar
Esse é o erro mais comum em trabalhos de faculdade.

O José Lucas faz alterações no código à tarde e dá git push.

À noite, você senta para programar, mas não roda o git pull. O seu VS Code continua com a versão antiga do código.

Você mexe no código e tenta dar git push. O GitHub vai rejeitar o seu envio na hora porque o seu código está desatualizado em relação ao que já está na nuvem.

--

## Como evitar esses conflitos?

Dividam as tarefas por arquivos: Combinem algo como: "Cara, hoje eu vou mexer no cadastro de funcionários (cadastro_funcionario.py) e você mexe no fluxo de caixa (main.py)". Mexer em arquivos diferentes nunca gera conflito.

Comunicação: Sempre que alguém terminar uma parte importante e der git push, avise no WhatsApp: "Enviei a minha parte lá, dá um pull aí!".

lembrar: Criem o hábito mecânico de digitar git pull origin main toda vez que sentarem para programar.

