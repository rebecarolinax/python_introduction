class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso!")

    def list_tasks(self):
        print("Lista de tarefas:")
        for index, task in enumerate(self.tasks, start=1):
            status = "concluída" if task.completed else "pendente"
            print(f"{index}. [{status}] {task.description}")

    def mark_task_as_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.completed = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Tarefa excluída com sucesso!")
        else:
            print("Número de tarefa inválido.")

def main():
    task_manager = TaskManager()
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            task_number = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            task_manager.mark_task_as_completed(task_number)
        elif choice == "4":
            task_number = int(input("Digite o número da tarefa a ser excluída: "))
            task_manager.delete_task(task_number)
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
