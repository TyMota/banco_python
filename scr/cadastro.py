import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    user = "root",
    password = "root",
    database = "banco"
)

def armazenar_cadastro(nome, idade, login, senha, frame):
    mycursor = mydb.cursor()

    saldo = 0

    while not nome or not idade or not login or not senha:
        txt = tk.Message(frame, text="Todos os campos são obrigatorios!", fg="red")
        txt.pack()
        txt.after(2000, txt.destroy)
        return

    else:

        sql = ("INSERT INTO usuarios (nome, ano, login, senha, saldo) VALUES (%s, %s, %s, %s, %s)")
        val = (nome, idade, login, senha, saldo)

        mycursor.execute(sql, val)

        mydb.commit()

        txt = tk.Message(frame, text="Cadastro realizado com sucesso!", fg="green")
        txt.pack()

        mydb.close()


def janela_cadastro(master, callback):
    """
    Função para criar um frame aonde o usuario ira colocar todos os seus dados
    """
    frame = tk.Frame(master)

    txt = tk.Label(frame, text="Digite seu nome")
    txt.pack()
    nome = tk.Entry(frame)
    nome.pack()

    txt = tk.Label(frame, text="Digite sua idade")
    txt.pack()
    idade = tk.Entry(frame)
    idade.pack()

    txt = tk.Label(frame, text="Digite o login")
    txt.pack()
    login = tk.Entry(frame)
    login.pack()

    txt = tk.Label(frame, text="Digite a senha")
    txt.pack()
    senha = tk.Entry(frame, show="*")
    senha.pack()

    butao = tk.Button(frame, text="Armazenar", command=lambda: callback(nome.get(), idade.get(), login.get(), senha.get(), frame))
    butao.pack()

    return frame

