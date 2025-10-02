import tkinter as tk
import mysql.connector
import time
import sys

mydb = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    user = "root",
    password = "root",
    database = "banco"
)

def validar_login(login, senha, frame):
    mycursor = mydb.cursor()

    query = "SELECT id, login, senha, saldo FROM usuarios WHERE login = %s"
    mycursor.execute(query, (login,))
    usuario = mycursor.fetchone()

    if usuario is None:
        txt = tk.Message(frame, text="Erro ao logar!", fg="red")
        txt.pack()
        txt.after(2000, txt.destroy)
        return None
    
    if usuario[2] != senha:
        txt = tk.Message(frame, text="Erro ao logar!", fg="red")
        txt.after(2000, txt.destroy)
        return None
    
    else:
        time.sleep(1)
        sys.exit()
    
    return usuario
        


def janela_login(master, callback):
    """
    Função para chamar a janela de login.
    E retornar o login para ser ultilizado em outro arquivo
    """

    #Adciona o 1 frame
    frame = tk.Frame(master)

    #Adciona o texto de login e adciona aonde escreve o login
    txt = tk.Label(frame, text="Digite o login")
    txt.pack()
    login = tk.Entry(frame)
    login.pack()

    #Adciona o texto de senha e adciona aonde escreve a senha
    txt = tk.Label(frame, text="Digite sua senha")
    txt.pack()
    senha = tk.Entry(frame)
    senha.pack()

    #btt armazenar dados
    butao = tk.Button(frame, text="Logar", command=lambda: callback(login.get(), senha.get(), frame))
    butao.pack()

    return frame
