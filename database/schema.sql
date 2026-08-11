USE distribuidora;

CREATE TABLE fornecedores(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(320),
    telefone VARCHAR(15) NOT NULL
);

CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL,
    id_fornecedor INT NOT NULL,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id) 
);

CREATE TABLE vendas(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unit DECIMAL(10, 2) NOT NULL,
    preco_total DECIMAL(10, 2) NOT NULL,
    data_venda DATE NOT NULL,
    cliente VARCHAR(100) NOT NULL,
    FOREIGN KEY(id_produto) REFERENCES produtos(id)
);

CREATE TABLE compras(
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unit DECIMAL(10, 2) NOT NULL,
    preco_total DECIMAL(10, 2) NOT NULL,   
    data_compra DATE NOT NULL,
    id_fornecedor INT NOT NULL,
    nota_fiscal VARCHAR(20),
    FOREIGN KEY(id_produto) REFERENCES produtos(id),
    FOREIGN KEY(id_fornecedor) REFERENCES fornecedores(id)
);

ALTER TABLE compras
MODIFY COLUMN nota_fiscal VARCHAR(20) NOT NULL;