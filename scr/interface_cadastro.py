import tkinter as tk
import mysql.connector


mydb = mysql.connector.connect(
    host = 'Localhost',
    port = '3307',
    user = 'root',
    password = 'root',
    database = 'banco'
)

def cadastro_armazenar_dados(nome_input, idade_input, login_input, senha_input, janela):
    mycursor = mydb.cursor()
    
    nome_final = nome_input.get()
    idade_final = idade_input.get()
    login_final = login_input.get()
    senha_final = senha_input.get()
    saldo = 0

    if not nome_final or not idade_final or not login_final or not senha_final:
        txt = tk.Message(janela, text="Todos os campos são obrigatórios!", fg="red")
        txt.pack()
        txt.after(2000, txt.destroy)
        return 

    try:
        sql = ("INSERT INTO usuarios (nome, ano, login, senha, saldo) VALUES (%s, %s, %s, %s, %s)")
        val = (nome_final, idade_final, login_final, senha_final, saldo)

        mycursor.execute(sql, val)

        mydb.commit()

        txt = tk.Message(janela, text="Dados Cadastrados com Sucesso!", fg = "green")
        txt.pack()

    except:
        txt = tk.Message(janela, text="Erro ao cadastrar o usuario! Tente novamente.", fg = "red")
        txt.pack()


def janela_cadastro(master):
    # Criar uma janela
    janela = tk.Frame(master)

    #Adicionar nome e input para colocar
    nome = tk.Label(janela, text="Digite seu nome")
    nome.pack()
    nome_input = tk.Entry(janela)
    nome_input.pack()

    #Adicionar idade e input para colocar
    idade = tk.Label(janela, text="Digite sua idade")
    idade.pack()
    idade_input = tk.Entry(janela)
    idade_input.pack()

    #Adicionar login e input para colocar
    login = tk.Label(janela, text="Digite o login")
    login.pack()
    login_input = tk.Entry(janela)
    login_input.pack()

    #Adicionar senha e input para colocar
    senha = tk.Label(janela, text="Digite sua senha")
    senha.pack()
    senha_input = tk.Entry(janela)
    senha_input.pack()

    #Btt amarzenar dados
    dados_button = tk.Button(janela, text="Armazenar", command=lambda: cadastro_armazenar_dados(nome_input, idade_input, login_input, senha_input, janela))
    dados_button.pack()


    #Adcionar a janela 
    return janela