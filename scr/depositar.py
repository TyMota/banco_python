import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost',
    port = '3307',
    user = 'root',
    password = 'root',
    database = 'banco'
)

def depositar(login, senha, janela):
    mycursor = mydb.cursor()

    login_final = login.get()
    senha_final = senha.get()

    try:
        query = ("SELECT id, login, senha, saldo FROM usuarios WHERE login = %s")

        mycursor.execute(query, (login_final,))

        usuario = mycursor.fetchone()

        saldo = usuario[3]

        print(usuario)

    except:
        pass

    if usuario == None or usuario == "":
        txt = tk.Message(janela, text="Erro ao logar! Tente novamente.", fg = "red")
        txt.grid(row=4, column=1)
        txt.after(2000, txt.destroy)

    elif usuario[2] != senha_final:
        txt = tk.Message(janela, text="Erro ao logar! Tente novamente.", fg = "red")
        txt.grid(row=4, column=1)
        txt.after(2000, txt.destroy) 

    else:
        tk.Label(janela, text="Digite o valor").grid(row=6, column=0)
        deposito = tk.Entry(janela)
        deposito.grid(row=6, column=1)

        
        


def logar():
    janela = tk.Tk()
    janela.geometry("600x300")

    tk.Label(janela, text="Por questão de segurança.", fg="red").grid(row=0, column=1)

    tk.Label(janela, text="Digite o Login").grid(row=1, column=0)
    login = tk.Entry(janela)
    login.grid(row=1, column=1)

    tk.Label(janela, text="Digite a senha").grid(row=2, column=0)
    senha = tk.Entry(janela)
    senha.grid(row=2, column=1)

    tk.Button(janela, text="Logar", command=lambda: depositar(login, senha, janela)).grid(row=3, column=1)

    janela.mainloop()


logar()
