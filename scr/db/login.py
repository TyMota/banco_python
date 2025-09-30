import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost',
    port = '3307',
    user = 'root',
    password = 'root',
    database = 'banco'
)
def login():
    mycursor = mydb.cursor()

    login_digitado = input("Digite o Login: ")
    senha_digitado = input("Digite sua senha: ")
 

    query = ("SELECT id, login, senha, saldo FROM usuarios WHERE login = %s")
    
    mycursor.execute(query, (login_digitado,))

    usuario = mycursor.fetchone()

    if usuario:
        if senha_digitado == usuario[2]:
            print("Logado com sucesso!")
        else:
            print("Login ou senha errado!")
    else:
        print("Login ou senha errado!")

    return usuario


if __name__ == "__main__":
    login()