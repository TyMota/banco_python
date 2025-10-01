import mysql.connector
from db import login

mydb = mysql.connector.connect(
    host = 'Localhost',
    port = '3307',
    user = 'root',
    password = 'root',
    database = 'banco'
)



def ver_saldo():
    
    print("Por questão de segurança digite novamente o login e senha.")

    login_digitado = login.login()

    usuario_digitado = login_digitado[1]

    saldo = login_digitado[3]

    mycursor = mydb.cursor()

    sql = "SELECT saldo FROM usuarios WHERE login = %s"

    mycursor.execute(sql, (usuario_digitado,))

    saldo = mycursor.fetchone()[0]

    print(f'Seu saldo atual é: {saldo}')

    return saldo
    


def depositar():
    print("Por questão de segurança digite novamente o login e senha.")

    mycursor = mydb.cursor()

    login_digitado = login.login()

    usuario_digitado = login_digitado[1]

    saldo_digitado = int(login_digitado[3])

    depositar_saldo = int(input("Digite o valor que deseja depositar: "))

    saldo = saldo_digitado + depositar_saldo

    sql = 'UPDATE usuarios SET saldo = %s WHERE login = %s'
    
    mycursor.execute(sql, (saldo, usuario_digitado))

    mydb.commit()

    print(f"Saldo depositado com sucesso! Seu saldo atual é de {saldo}")


def sacar():
    print("Por questão de segurança digite novamente o login e senha.")

    mycursor = mydb.cursor()

    login_digitado = login.login()

    usuario_digitado = login_digitado[1]

    saldo_digitado = int(login_digitado[3])

    sacar_saldo = int(input("Digite o valor que deseja sacar: "))

    while sacar_saldo > saldo_digitado:
        print("Saldo insuficiente.")
        sacar_saldo = int(input("Digite o valor que deseja sacar: "))

    else:
            saldo_final = saldo_digitado - sacar_saldo
            print("Saque realizado com sucesso!")

    saldo = int(saldo_final)


    sql = 'UPDATE usuarios SET saldo = %s WHERE login = %s'

    mycursor.execute(sql, (saldo, usuario_digitado))

    mydb.commit()



if __name__ == "__main__":
    ver_saldo()

if __name__ == "__main__":    
    depositar()

if __name__ == "__main__":  
    sacar()


