import sqlite3

def conectar():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cpf TEXT UNIQUE NOT NULL,
                        saldo REAL DEFAULT 0.0)''')
    conexao.commit()
    return conexao

def cadastrar_cliente(nome, cpf, saldo_inicial=0.0):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, cpf, saldo) VALUES (?, ?, ?)", (nome, cpf, saldo_inicial))
    conexao.commit()
    conexao.close()

def consultar_saldo(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT saldo FROM clientes WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado[0] if resultado else None

def atualizar_saldo(cpf, valor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET saldo = saldo + ? WHERE cpf = ?", (valor, cpf))
    conexao.commit()
    conexao.close()
