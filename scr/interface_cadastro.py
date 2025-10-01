import tkinter as tk
import sys
import mysql.connector

#Funcao para sair do programa
def btt_sair():
    sys.exit()

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

    try:
        sql = ("INSERT INTO usuarios (nome, ano, login, senha, saldo) VALUES (%s, %s, %s, %s, %s)")
        val = (nome_final, idade_final, login_final, senha_final, saldo)

        mycursor.execute(sql, val)

        mydb.commit()

        txt = tk.Message(janela, text="Dados Cadastrados com Sucesso!", fg = "lightgreen")
        txt.grid(row=5, column=1)

    except:
        txt = tk.Message(janela, text="Erro ao cadastrar o usuario! Tente novamente.", fg = "red")
        txt.grid(row=5, column=1)


def janela_cadastro():
    # Criar uma janela
    janela = tk.Tk()
    janela.title("Menu Cadastro")
    janela.geometry("300x200")

    #Adicionar nome e input para colocar
    nome = tk.Label(janela, text="Digite seu nome")
    nome.grid(row=0, column=0)
    nome_input = tk.Entry(janela)
    nome_input.grid(row=0, column=1)

    #Adicionar idade e input para colocar
    idade = tk.Label(janela, text="Digite sua idade")
    idade.grid(row=1, column=0)
    idade_input = tk.Entry(janela)
    idade_input.grid(row=1, column=1)

    #Adicionar login e input para colocar
    login = tk.Label(janela, text="Digite o login")
    login.grid(row=2, column=0)
    login_input = tk.Entry(janela)
    login_input.grid(row=2, column=1)

    #Adicionar senha e input para colocar
    senha = tk.Label(janela, text="Digite sua senha")
    senha.grid(row=3, column=0)
    senha_input = tk.Entry(janela)
    senha_input.grid(row=3, column=1)

    #Btt amarzenar dados
    dados_button = tk.Button(janela, text="Armazenar", command=lambda: cadastro_armazenar_dados(nome_input, idade_input, login_input, senha_input, janela))
    dados_button.grid(row=4, column=1)


    #Adicionar o botão de saida
    botao_Saida = tk.Button(janela, text="SAIR", command=btt_sair)
    botao_Saida.grid(row=6, column=1)

    #Adcionar a janela 
    janela.mainloop()


if __name__ == "__main__":
    janela_cadastro()
