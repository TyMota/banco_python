import tkinter as tk
from tkinter import ttk
import mysql.connector
from login import *



mydb = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    user = "root",
    password = "root",
    database = "banco"
)

def ver_saldo():
    """
    Função para ver o saldo
    """
    login_usuario = None
    if len(sys.argv) > 1:
        login_usuario = sys.argv[1] 

    mycursor = mydb.cursor()

    sql = f"SELECT * FROM usuarios WHERE login = '{login_usuario}'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        saldo = x[5]

    mycursor.close()

    return saldo

ver_saldo()



