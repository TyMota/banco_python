import tkinter as tk
from login import *
from cadastro import *
import sys


janela = tk.Tk()
janela.title("Banco Piton")
janela.geometry("600x300")

f_login = janela_login(janela, validar_login)
f_cadastro = janela_cadastro(janela, armazenar_cadastro)

for frame in (f_login, f_cadastro):
    frame.grid(row=0, column=1, sticky="news")

def raise_frame(frame):
    frame.tkraise()

tk.Button(f_login, text="Ir para cadastro", command=lambda: raise_frame(f_cadastro)).pack()
tk.Button(f_cadastro, text="Ir para login", command=lambda: raise_frame(f_login)).pack()

tk.Button(janela, text="Sair", command=sys.exit).grid(row=4, column=1)

raise_frame(f_cadastro)
janela.mainloop()

