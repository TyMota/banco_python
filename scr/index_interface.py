import tkinter as tk
from interface_cadastro import *
from interface_login import *
import sys

janela = tk.Tk()
janela.title("Banco Piton")
janela.geometry("600x300")

f_login = janela_login(janela)
f_cadastro = janela_cadastro(janela)


for f in (f_login, f_cadastro):
    f.grid(row=0, column=1, sticky='news')

def raise_frame(frame):
    frame.tkraise()

# Botões para trocar de frame
tk.Button(f_login, text="Ir para Cadastro", command=lambda: raise_frame(f_cadastro)).pack()
tk.Button(f_cadastro, text="Ir para Login", command=lambda: raise_frame(f_login)).pack()

botao_Saida = tk.Button(janela, text="SAIR", command=sys.exit)
botao_Saida.grid(row=3, column=1)

raise_frame(f_login)
janela.mainloop()

