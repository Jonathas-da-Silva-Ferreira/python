import tkinter as tk
import customtkinter as ctk
import requests # type: ignore

API_URL = "http://127.0.0.1:8000/api/tasks/"

class TaskApp(ctk.CTK):
    def __init__(self):
        super().__init__()
      
        self.title("Gerenciador de Tarefas")
        self.geometry("400x300")
        
        self.tasks_entry = ctk.CTKEntry(self, placeholder="Digite uma nova Tarefa")
        self.tasks_entry.pack(pady=10)

        self.add_button = ctk.CTKEntry(self, text="Adicionar Tarefa", comand=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(self)
        self.tasks_listbox.pack(pady=10)

        self.get_tasks()

    def get_tasks(self):
        response = requests.get