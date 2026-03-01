# Vamos adicionar uma interface, dar vida realmente
import tkinter as tk
from tkinter import messagebox



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
        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas")

        # Elementos da interface
        self.lista_tarefas = tk.Listbox(self.root, width=50, height=10)
        self.lista_tarefas.pack(padx=10, pady=10)

        self.entry_tarefa = tk.Entry(self.root, width=50)
        self.entry_tarefa.pack(padx=10, pady=5)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(padx=10, pady=5)
        tk.Button(frame_botoes, text="Adicionar", command=self.adicionar_tarefas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Marcar como Concluido", command=self.marcar_concluida).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Remover", command=self.remover_tarefa).pack(side=tk.LEFT, padx=5)

        self.atualizar_lista()



    def adicionar_tarefas(self):
        descricao = self.entry_tarefa.get()
        if descricao:
            tarefa = Tarefa(descricao)
            self.tarefas.append(tarefa)
            self.atualizar_lista()
            self.entry_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso"," Digite uma tarefa.")

        
    def marcar_concluida(self):
        try:
            indice = self.lista_tarefas.curselection()[0]
            self.tarefas[indice].marcar_concluida()
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa.")
            

    def remover_tarefa(self):
        try:
            indice = self.lista_tarefas.curselection()[0]
            del self.tarefas[indice]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa.")

    def atualizar_lista(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista_tarefas.insert(tk.END, str(tarefa))

    def run(self):
        self.root.mainloop()

# Rodar o aplicativo
if __name__ == '__main__':
    gerenciador = GerenciadorTarefas()
    gerenciador.run()