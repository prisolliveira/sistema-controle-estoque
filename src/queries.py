from src.connection import conexao, cursor

def listagem(lista):
    cursor.execute(f"SELECT * FROM {lista}")
    resultado = cursor.fetchall()
    print(resultado) # Possibiliando listar todas as tabelas

def adicionar(tabela, lista, colunas):
    placeholders = ", ".join(["%s"] * len(lista[0]))
    colunas_str = ", ".join(colunas)

    query = f"INSERT INTO {tabela} ({colunas_str}) VALUES ({placeholders})"
    cursor.executemany(query, lista)
    conexao.commit()

def remover(tabela, id):
    query = f"DELETE FROM {tabela} WHERE id = %s"
    cursor.execute(query, (id,)) # Evitar SQL INJECTION: utilizar parâmentros nas querys
    conexao.commit()

def encontrar(tabela, id_tabela, id_valor):
    cursor.execute(f"SELECT preco_unit FROM {tabela} WHERE {id_tabela} = {id_valor}")
    resultado = cursor.fetchone() # Para pegar valores das consultas (SELECT) utilizamos fetchone ou fetchall

    if resultado:
        return resultado[0]
    else:
        return None


def venda(id_produto, quant, cliente):
    from database.temp import temp_vendas
    adicionar("vendas", temp_vendas)


# ANOTAÇÕES
# Não é possível fazer com que dois arquivos dependam um do outro.