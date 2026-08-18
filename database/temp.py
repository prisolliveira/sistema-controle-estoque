temp_produtos = list()

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
