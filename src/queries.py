from src.connection import conexao, cursor
from database.temp import temp_produtos

def listagem(lista):
    cursor.execute(f"SELECT * FROM {lista}")
    resultado = cursor.fetchall()
    print(resultado) # possibiliando listar todas as tabelas

def adicionar(tabela, lista, colunas):
    placeholders = ", ".join(["%s"] * len(lista[0]))
    colunas_str = ", ".join(colunas)

    query = f"INSERT INTO {tabela} ({colunas_str}) VALUES ({placeholders})"
    cursor.executemany(query, lista)
    conexao.commit()

def remover(tabela, id):
    query = f"DELETE FROM {tabela} WHERE id = {id}"
    cursor.execute(query)
    conexao.commit()