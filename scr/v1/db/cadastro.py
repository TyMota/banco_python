import mysql.connector

mydb = mysql.connector.connect(
    host = 'Localhost',
    port = '3307',
    user = 'root',
    password = 'root',
    database = 'banco'
)
def cadastrar():
    mycursor = mydb.cursor()
    
    nome = input("Digite seu nome: ")
    ano = int(input("Digite sua idade: "))
    login = input("Digite o Login: ")
    senha = input("Digite sua senha: ")
    saldo = 0
    
    
    try:
        sql = ("INSERT INTO usuarios (nome, ano, login, senha, saldo) VALUES (%s, %s, %s, %s, %s)")
        val = (nome, ano, login, senha, saldo)

        mycursor.execute(sql, val)

        mydb.commit()

        print("Perfil criado!")

    except mysql.connector.errors.IntegrityError:
        print("Login já cadastrado.")

    


if __name__ == "__main__":
    cadastrar()