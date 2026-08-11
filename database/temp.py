# criar uma class para armazenar dados temporariamente

temp_produtos = list()

class produtos:

    def __init__(self, nome, preco, id_fornecedor):
        self.nome = nome
        self.preco = preco
        self.id_fornecedor = id_fornecedor


# se valor de atributo não corresponder com seu tipo de restrição
# não será adicionado na lista tempora

