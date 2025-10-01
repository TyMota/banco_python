import tkinter as tk
from tkinter import ttk
import sys
import mysql.connector
from menu_interface import *
from interface_login import *
from interface_cadastro import *

#Funcao para sair do programa
def btt_sair():
    sys.exit()


def menu_inicial():
    # Criar uma janela
    janela = tk.Tk()
    janela.title("Menu inicial")
    janela.geometry("300x200")
    
    tk.Button(janela, text="Login", command = janela_login).grid(row=0, column=1)

    tk.Button(janela, text="Cadastrar", command = janela_cadastro).grid(row=1, column=1)

    tk.Button(janela, text="SAIR", command=btt_sair).grid(row=2, column=1)

    #Adcionar a janela 
    janela.mainloop()


if __name__ == "__main__":
    menu_inicial()
