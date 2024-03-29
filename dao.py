# Dal fica responsavel pelo Armazenamento persistente

from model import (
    Categoria,
    Estoque,
    Produtos,
    Vendas,
    Fornecedor,
    Cliente,
    Funcionario,
)
from datetime import datetime

DATA_BASE = 'data_base/'


# CLASSES DA ÁREA DE CATEGORIA:


class CategoriaDao:
    @classmethod
    def salvarCategoria(cls, categoria: Categoria):  # Salvar Categoria.
        with open(DATA_BASE + 'categoria.txt', 'a') as arq:
            arq.writelines(categoria + '\n')

    @classmethod
    def ler_categoria(cls):  # Ler Categoria para exclusão.
        with open(DATA_BASE + 'categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cate = []

        if len(cls.categoria) > 0:
            for i in cls.categoria:
                cate.append(Categoria(i))

        return cate

    @classmethod
    def lercategoria(cls):  # o usuário visualizar o que há em categoria.
        arquivo = open(DATA_BASE + 'categoria.txt', 'r')
        lista_categoria = arquivo.readlines()
        return lista_categoria


# CLASSES DA ÁREA DE PRODUTOS:


class EstoqueDao:
    @classmethod
    def salvar(
        cls, estoques: Produtos, quantidade
    ):  # Recebendo produtos da model
        with open(DATA_BASE + 'estoque.txt', 'a') as arq:
            arq.writelines(
                estoques.nome
                + '|'
                + estoques.preco
                + '|'
                + estoques.categoria
                + '|'
                + str(quantidade)
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(DATA_BASE + 'estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        est = []

        if len(cls.estoque) > 0:
            for i in cls.estoque:
                i = i.split('|')
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))

        return est

    @classmethod
    def ler_produto(cls):
        arquivos = open(DATA_BASE + 'estoque.txt', 'r')
        lista_arquivos = arquivos.readlines()
        return lista_arquivos


# CLASSES DE FORNECEDOR:


class FornecedorDao:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open(DATA_BASE + 'fornecedor.txt', 'a') as arq:
            arq.writelines(
                fornecedor.nome
                + '|'
                + fornecedor.telefone
                + '|'
                + fornecedor.cnpj
                + '|'
                + fornecedor.categoria
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(DATA_BASE + 'fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        fornec = []

        if len(cls.fornecedor) > 0:
            for i in cls.fornecedor:
                i = i.split('|')
                fornec.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return fornec

    @classmethod
    def ler_fornecedores(cls):
        forne = open(DATA_BASE + 'fornecedor.txt', 'r')
        lista_fornecedores = forne.readlines()
        return lista_fornecedores


# CLASSES DE CLIENTES


class ClienteDao:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open(DATA_BASE + 'clientes.txt', 'a') as arq:
            arq.writelines(
                cliente.nome
                + '|'
                + cliente.cpf
                + '|'
                + cliente.email
                + '|'
                + cliente.telefone
                + '|'
                + cliente.endereco
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(DATA_BASE + 'clientes.txt', 'r') as arq:
            cls.cliente = arq.readlines()

        clien = []

        if len(cls.cliente) > 0:
            for i in cls.cliente:
                i = i.split('|')
                clien.append(Cliente(i[0], i[1], i[2], i[3], i[4]))

        return clien

    @classmethod
    def ler_clientes(cls):
        client = open(DATA_BASE + 'clientes.txt', 'r')
        lista_clientes = client.readlines()
        return lista_clientes


# CLASSE DE FUNCIONARIO


class FuncionarioDao:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open(DATA_BASE + 'funcionario.txt', 'a') as arq:
            arq.writelines(
                funcionario.nome
                + '|'
                + funcionario.cpf
                + '|'
                + funcionario.email
                + '|'
                + funcionario.telefone
                + '|'
                + funcionario.endereco
                + '|'
                + funcionario.clt
                + '\n'
            )

    @classmethod
    def ler(cls):
        with open(DATA_BASE + 'funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        func = []

        if len(cls.funcionario) > 0:
            for i in cls.funcionario:
                i = i.split('|')
                func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return func

    @classmethod
    def lista_funcionario(cls):
        funcionario = open(DATA_BASE + 'funcionario.txt', 'r')
        lista_funcionario = funcionario.readlines()
        return lista_funcionario


# CLASSES DO CAIXA:


class VendasDao:
    @classmethod
    def salvar(cls, venda: Vendas):
        with open(DATA_BASE + 'vendas.txt', 'a') as arq:
            arq.writelines(
                venda.itens_vendidos.nome
                + '|'
                + venda.itens_vendidos.preco
                + '|'
                + venda.itens_vendidos.categoria
                + '|'
                + venda.vendedor
                + '|'
                + venda.comprador
                + '|'
                + str(venda.quantidade_vendida)
                + '|'
                + venda.data
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open(DATA_BASE + 'vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()

        lista_venda = []

        if len(cls.venda) > 0:
            for i in cls.venda:
                i = i.split('|')
                lista_venda.append(
                    Vendas(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5])
                )

        return lista_venda

    # Ordenar Relatório geral de produtos
    @classmethod
    def ler_relatorio_geral(cls):
        with open(DATA_BASE + 'vendas.txt', 'r') as arq:
            cls.rel = arq.readlines()

        lista_rel = []

        if len(cls.rel) > 0:
            for i in cls.rel:
                i = i.split('|')
                lista_rel.append(Produtos(i[2], i[4], i[5]))

        return lista_rel
