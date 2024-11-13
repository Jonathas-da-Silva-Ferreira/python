import tkinter as tk
from tkinter import messagebox
import banco as db  # Importa o arquivo banco.py

def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    saldo = float(entry_saldo.get())
    db.cadastrar_cliente(nome, cpf, saldo)
    messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")
    limpar_campos()

def consultar():
    cpf = entry_cpf.get()
    saldo = db.consultar_saldo(cpf)
    if saldo is not None:
        messagebox.showinfo("Saldo", f"Saldo atual: R$ {saldo:.2f}")
    else:
        messagebox.showerror("Erro", "Cliente não encontrado.")

def depositar():
    cpf = entry_cpf.get()
    valor = float(entry_valor.get())
    db.atualizar_saldo(cpf, valor)
    messagebox.showinfo("Depósito", "Depósito realizado com sucesso!")

def sacar():
    cpf = entry_cpf.get()
    valor = -float(entry_valor.get())
    db.atualizar_saldo(cpf, valor)
    messagebox.showinfo("Saque", "Saque realizado com sucesso!")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_saldo.delete(0, tk.END)
    entry_valor.delete(0, tk.END)


#Configuração da Interface Grafica 

janela = tk.Tk()
janela.title("Sistema bancario")

tk.Label(janela, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="CPF").grid(row=1, column=0)
entry_cpf = tk.Entry(janela)
entry_cpf.grid (row=1, column=1)

tk.Label(janela, text="Saldo inicial").grid(row=2, column=0)
entry_saldo = tk.Entry(janela)
entry_saldo.grid (row=2, column=1)

tk.Label(janela, text="Valor").grid(row=3, column=0)
entry_valor = tk.Entry(janela)
entry_valor.grid(row=3, column=1)

tk.Button(janela, text="Cadastrar Cliente", command=cadastrar).grid(row=4, column=0)
tk.Button(janela, text="Consultar Saldo", command=consultar).grid(row=4, column=1)
tk.Button(janela, text="Depositar", command=depositar).grid(row=4, column=2)
tk.Button(janela, text="Sacar", command=sacar).grid(row=4, column=3)

janela.mainloop()