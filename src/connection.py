import mysql.connector as mysql 

conexao = mysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "distribuidora"
)

cursor = conexao.cursor()