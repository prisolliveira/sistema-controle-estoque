import src.queries as qs
from datetime import datetime

temp_produtos = list()
temp_vendas = list()

def validar_texto(texto):
    if type(texto) is not str:
        raise TypeError("Esse campo deve ser um texto obrigatório.")
    return texto
def validar_decimal(decimal):
    if type(decimal) is not float:
        raise TypeError("Esse campo deve ser número decimal obrigatório.")
    if decimal < 0:
        raise TypeError("Somente números positivos.")
    return decimal
def validar_inteiro(inteiro):
    if type(inteiro) is not int:
        raise TypeError("Esse campo deve ser número inteiro obrigatório.")
    if inteiro < 0:
        raise TypeError("Somente números positivos")
    return inteiro

class Produtos:
    def __init__(self, nome, preco, quantidade, id_fornecedor):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.id_fornecedor = id_fornecedor

    def adicionar_temp(self):
        nome = validar_texto(self.nome)
        preco = validar_decimal(self.preco)
        quantidade = validar_inteiro(self.quantidade)
        id_fornecedor = validar_inteiro(self.id_fornecedor)

        temp_produtos.append([nome, preco, quantidade, id_fornecedor])


class Vendas:
    def __init__(self, id_produto, quantidade, data_venda, cliente):
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.data_venda = data_venda
        self.cliente = cliente

    def adicionar_temp(self):  
        id_produto = validar_inteiro(self.id_produto)
        quantidade = validar_inteiro(self.quantidade)

        preco = float(qs.encontrar("produtos", "id", self.id_produto))
        preco_total = preco * quantidade

        data_venda = datetime.strptime(self.data_venda, "%d/%m/%Y").date()
        cliente = validar_inteiro(self.cliente)

        temp_vendas.append([id_produto, quantidade, preco, 
                           preco_total, data_venda, cliente])

        