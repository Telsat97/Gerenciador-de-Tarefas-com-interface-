class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "[x]" if self.concluida else "[ ]"
        return f"{status} {self.descricao}"
    
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefas(self,descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)

    def listar_tarefa(self):
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i+1}. {tarefa}")

    def remover_tarefa(self, indice):
        try:
            del self.tarefas[indice - 1]
        except IndexError:
            print("Índice inválido. ")

gerenciador = GerenciadorTarefas()

while True:
    print("\n1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input(" Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da tarefa: ")
        gerenciador.adicionar_tarefas(descricao)
    elif opcao == "2":
        gerenciador.listar_tarefa()
    elif opcao == "3":
        gerenciador.listar_tarefa()
        indice = int(input("Numero da tarefa a marcar como concluida: "))
        try:
            gerenciador.tarefas[indice - 1].marcar_concluida()
        except IndexError:
            print("Índice invalido.")
    elif opcao == "4":
        gerenciador.listar_tarefa()
        indice = int(input("Numero da tarefa a remover: "))
        gerenciador.remover_tarefa(indice)
    elif opcao == "5":
        break
    else:
        print("Opção invalida.")
