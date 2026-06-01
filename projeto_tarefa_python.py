# Projeto de Gerenciamento de Tarefas em Python

print("===== LISTA DE TAREFAS =====")
tarefas = [] # Criação da lista vazia

while True: # Loop infinito para o menu
    print("\n===== MENU =====")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ") # Recebe a opção do usuário
    
    if opcao == "4": # Verifica se o usuário escolheu sair
        print("Saída concluída com sucesso")
        break # Encerra o loop e o programa

    elif opcao == "1": # Verifica se o usuário escolheu adicionar uma tarefa
        tarefa = input("Digite uma tarefa: ") # Recebe a tarefa do usuário
        tarefas.append(tarefa) # Adiciona a tarefa à lista
        print(f"Tarefa '{tarefa}' adicionada com sucesso") # Confirmação de adição da tarefa
    
    elif opcao == "3": # Verifica se o usuário escolheu remover uma tarefa
        if not tarefas: # Verifica se a lista de tarefas está vazia
            print("Não tem tarefas cadastradas") # Informa que não há tarefas para remover
        
        else: # Exibe a lista de tarefas para o usuário escolher qual remover
            print("\n===== TAREFAS =====")
            for indice, tarefa in enumerate(tarefas): # Exibe cada tarefa com seu índice correspondente
                print(f"{indice + 1} - {tarefa}")
        
            escolha = int(input("Qual tarefa deseja remover: ")) # Recebe a escolha do usuário para remover uma tarefa e transforma em inteiro
            indice_remover = escolha - 1 # Ajusta o índice para corresponder à posição correta na lista (índices começam em 0). O escolha do usuário começa em 1, então subtrai-se 1 para obter o índice correto.
            tarefa_removida = tarefas.pop(indice_remover) # Remove a tarefa da lista usando o método pop() e armazena a tarefa removida em uma variável para exibir a mensagem de confirmação
            print(f"Tarefa {tarefa_removida} removida com sucesso") # Confirmação de remoção da tarefa
    
    elif opcao == "2": # Verifica se o usuário escolheu listar as tarefas
        if not tarefas: # Verifica se a lista de tarefas está vazia
            print("Não tem tarefas cadastradas")
        
        else: # Exibe a lista de tarefas para o usuário
            print("\n===== TAREFAS =====")
            for indice, tarefa in enumerate(tarefas): # Exibe cada tarefa com seu índice correspondente. O enumerate() é usado para obter o índice e a tarefa ao mesmo tempo. O índice é incrementado em 1 para exibir a numeração correta para o usuário (começando em 1).
                print(f"{indice + 1} - {tarefa}") # Exibe a tarefa com seu índice correspondente. O indice + 1 é usado para exibir a numeração correta para o usuário (começando em 1).
    
    else: # Caso o usuário escolha uma opção inválida, exibe uma mensagem de erro
        print("Opção inválida")
