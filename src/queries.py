from connection import conexao, cursor

def listagem(lista):
    cursor.execute(f"SELECT * FROM {lista}")
    resultado = cursor.fetchall()
    print(resultado) # possibiliando listar todas as tabelas


listagem("fornecedores")
