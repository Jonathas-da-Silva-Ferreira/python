import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import requests # type: ignore 

API_URL = "http://127.0.0.1:8000/api/tasks/"

class TaskApp(ctk.CTK):
    def __init__(self):
        super().__init__()

        self.title("Gerenciado de Tarefas")
        self.geometry("400x400")

        #Titulo
        self.label_title = ctk.CTkLabel(self, text="Minhas Tarefas", font=("Arial", 20))
        self.label_title.pack(pady=10)

        #Campo de entrada
        self.task_input = ctk.CTkEntry(self, placeholder_text="Digite uma nova tarefa")
        self.task_input.pack(pady=10)
        
        #Botão de adicionar
        self.add_button = ctk.CTkButton(self, text="Adicionar Tarefa", command=self.add_tasks)
        self.add_button.pack(pady=5)

        #Lista de tarefas
        self.task_listbox = tk.Listbox(self, height=10, bg="#f0f0f0", selectbackground="add8e6")
        self.task_listbox.pack(pady=10)

        #Botão de Ação
        self.delete_button = ctk.CTkButton(self, text="Excluir Tarefas", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = ctk.CTkButton(self, text="Concluir Tarefa", command=self.complete.task)

        self.get_tasks()

    def get_tasks(self):
        """
        Carregar as tarefas de API. """
        response = requests.get(API_URL)
        if response.status_code == 200:
            task = response.json()
            self.task_listbox.delete(0, tk.END)
            for task in task:
                status = "[✔]" if task['completed'] else "[]"
                self.task_listbox.insert(tk.END, f"{status} {task['title']}")
                
    def add_task(self):
        """"Adiocionar nova tarefa"""
        task_title = self.task_input.get()
        if task_title:
            response = requests.post(API_URL, data={"title": task_title, "completed": False})
            if response.status_code == 201:
                self.get_tasks()
                self.task_input.delete(0, tk.END)
                messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso")
            else:
                    messagebox.showerror("Erro", "Erro ao adicionar tarefa.")
            
    def delete_task(self):
        """Deletar tarefa"""
        selected_index = self.tasl_listbox.curseLection()[0]
        task_text = self.task_Listbox.get(selected_index)
        task_title = task
