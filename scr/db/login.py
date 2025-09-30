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

    while usuario == None:
        print("Login errado!")
        login_digitado = input("Digite o Login: ")
            
        query = ("SELECT id, login, senha, saldo FROM usuarios WHERE login = %s")
        
        mycursor.execute(query, (login_digitado,))

        usuario = mycursor.fetchone()

    while usuario[2] != senha_digitado:
        print("Senha errada!")
        senha_digitado = input("Digite sua senha: ")
       
    return usuario


if __name__ == "__main__":
    login()


