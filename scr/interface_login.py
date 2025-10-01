import tkinter as tk
import mysql.connector


mydb = mysql.connector.connect(
    host = 'Localhost',
    port = '3307',
    user = 'root',
    password = 'root',
    database = 'banco'
)

def login_armazenar_dados(login_input, senha_input, frame):
    mycursor = mydb.cursor()

    login_final = login_input.get()
    senha_final = senha_input.get()

    try:
        query = ("SELECT id, login, senha, saldo FROM usuarios WHERE login = %s")
            
        mycursor.execute(query, (login_final,))

        usuario = mycursor.fetchone()

        if usuario == None:
            txt = tk.Message(frame, text="Erro ao logar! Tente novamente.", fg = "red")
            txt.pack()
            txt.after(2000, txt.destroy)
        if usuario[2] != senha_final:
            txt = tk.Message(frame, text="Erro ao logar! Tente novamente.", fg = "red")
            txt.pack()
            txt.after(2000, txt.destroy)
        else:
            txt = tk.Message(frame, text="Login realizado com sucesso!", fg = "green")
            txt.pack()
            txt.after(2000, txt.destroy)

    except TypeError: 
        print("Sem cadastro")


def janela_login(master):
    # Criar uma janela
    frame = tk.Frame(master)

    #Adicionar login e input para colocar
    login = tk.Label(frame, text="Digite o login")
    login.pack()
    login_input = tk.Entry(frame)
    login_input.pack()

    #Adicionar senha e input para colocar
    senha = tk.Label(frame, text="Digite sua senha")
    senha.pack()
    senha_input = tk.Entry(frame)
    senha_input.pack()

    #Btt amarzenar dados
    dados_button = tk.Button(frame, text="Logar", command=lambda: login_armazenar_dados(login_input, senha_input, frame))
    dados_button.pack()

    return frame

