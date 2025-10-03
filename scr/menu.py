import sys
import tkinter as tk
from tkinter import ttk
import mysql.connector
from operacoes import ver_saldo

login_usuario = None
if len(sys.argv) > 1:
    login_usuario = sys.argv[1]



mydb = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    user = "root",
    password = "root",
    database = "banco"
)

def callback():
    mycursor = mydb.cursor()
    deposito = int(valor.get())
    sql = "UPDATE usuarios SET saldo = saldo + %s WHERE login = %s"
    val = (deposito, login_usuario)

    mycursor.execute(sql, val)

    mydb.commit()

    txt = tk.Message(tab2, text="Deposito realizado com sucesso!", fg = "green")
    txt.pack()
    txt.after(2000, txt.destroy)

    mycursor.close()

def atualizar():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT saldo FROM usuarios WHERE login = %s", (login_usuario,))

    resultado = mycursor.fetchone()
    saldo = int(resultado[0])

    tt = ttk.Label(tab1, text=f"Seu saldo atual é R${saldo}")
    tt.pack()
    tt.after(2000, tt.destroy)


def sub():
    mycursor = mydb.cursor()
    sacar = int(saque.get())

    mycursor.execute("SELECT saldo FROM usuarios WHERE login = %s", (login_usuario,))

    resultado = mycursor.fetchone()
    saldo = int(resultado[0])
    
    sql = "UPDATE usuarios SET saldo = saldo - %s WHERE login = %s"
    valor = (sacar, login_usuario)


    if sacar <= saldo:
        txt = tk.Message(tab3, text="Saque realizado com sucesso!", fg = "green")
        txt.pack()
        txt.after(2000, txt.destroy)

        mycursor.execute(sql, valor)

        mydb.commit()
    
    if sacar > saldo:
        txt = tk.Message(tab3, text="Saldo insuficiente!", fg = "red")
        txt.pack()
        txt.after(2000, txt.destroy)

        return

    mycursor.close()



def tab(event):
    notebook = event.widget
    tab_id = notebook.select()
    tab_text = notebook.tab(tab_id, "text")
    print(f"Selected Tab Text: {tab_text}")


root = tk.Tk()
root.title("Banco Piton")
root.geometry("600x300")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')


tab1 = ttk.Frame(notebook)
tk.Label(tab1, text=f"Seja bem vindo, {login_usuario}!").pack()
tk.Button(tab1, text="Ver saldo", command=atualizar).pack()


tab2 = ttk.Frame(notebook)
tk.Label(tab2, text="Digite o valor que deseje depositar").pack()
valor = tk.Entry(tab2)
valor.pack()


tab3 = ttk.Frame(notebook)
tk.Label(tab3, text="Digite o valor que deseja sacar").pack()
saque = tk.Entry(tab3)
saque.pack()

butao = tk.Button(tab2, text="Depositar", command = callback)
butao.pack()

butao_saq = tk.Button(tab3, text="Sacar", command = sub)
butao_saq.pack()

notebook.add(tab1, text='Saldo')
notebook.add(tab2, text='Depositar')
notebook.add(tab3, text="Sacar")

root.mainloop()