import database.temp as tp
import src.queries as qs

# produto = tp.Produtos("Esponja", 2.4, 10, 2)
# produto.adicionar_temp()

venda = tp.Vendas(20, 2, "12/05/2026", 1)
venda.adicionar_temp()
print(tp.temp_vendas)

#print(tp.temp_produtos)  # confirma que não está vazia, antes de inserir
#qs.adicionar("produtos", tp.temp_produtos, ["nome", "preco", "quantidade", "id_fornecedor"])
#qs.remover("produtos", 22)