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

def login_armazenar_dados(login_input, senha_input, janela):
    mycursor = mydb.cursor()

    login_final = login_input.get()
    senha_final = senha_input.get()

    try:
        query = ("SELECT id, login, senha, saldo FROM usuarios WHERE login = %s")
            
        mycursor.execute(query, (login_final,))

        usuario = mycursor.fetchone()

        dados = usuario

        if usuario == None:
            txt = tk.Message(janela, text="Erro ao logar! Tente novamente.", fg = "red")
            txt.grid(row=5, column=1)
            txt.after(2000, txt.destroy)
        if usuario[2] != senha_final:
            txt = tk.Message(janela, text="Erro ao logar! Tente novamente.", fg = "red")
            txt.grid(row=5, column=1)
            txt.after(2000, txt.destroy)
        else:
            txt = tk.Message(janela, text="Login realizado com sucesso!", fg = "green")
            txt.grid(row=5, column=1)
            txt.after(2000, txt.destroy)

    except TypeError: 
        print("Sem cadastro")


def janela_login():
    # Criar uma janela
    janela = tk.Tk()
    janela.title("Menu Login")
    janela.geometry("300x200")


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
    dados_button = tk.Button(janela, text="Logar", command=lambda: login_armazenar_dados(login_input, senha_input, janela))
    dados_button.grid(row=4, column=1)


    #Adicionar o botão de saida
    botao_Saida = tk.Button(janela, text="SAIR", command=btt_sair)
    botao_Saida.grid(row=6, column=1)

    #Adcionar a janela 
    janela.mainloop()


if __name__ == "__main__":
    janela_login()
