# Projeto de Gerenciamento de Tarefas em Python

print("===== LISTA DE TAREFAS =====")
tarefas = []

for i in range(3):
    tarefa = input("Digite uma tarefa: ")
    tarefas.append(tarefa)

print("\n===== TAREFAS CADASTRADAS =====")
for tarefa in tarefas:
    print(f"- {tarefa}")