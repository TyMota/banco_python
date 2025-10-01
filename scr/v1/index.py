from db import cadastro
from db import login
from menu import*
from saldo import*
import sys


print("=========================")
print("BEM VINDO AO BANCO PITON!")
print("=========================")

escolha = menu_login()

while True:
    if escolha == 1:
        logado = login.login()
        break

    elif escolha == 2:
        cadastro = cadastro.cadastrar()
        break

    else:
        print("Você saiu do programa!")
        sys.exit()

while True:
    escolha_banco = menu_saldo()

    if escolha_banco == 1:
        ver_saldo()


    elif escolha_banco == 2:
        sacar()

    elif escolha_banco == 3:
        depositar()

    else:
        print("Você saiu do programa!")
        sys.exit()
