# é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web.

from controller import (
    CategoriaController,
    EstoqueController,
    FornecedorController,
    ClienteController,
    FuncionarioController,
    VendasController,
    RelatoriosProdController,
    RelatorioData,
)
from dao import (
    CategoriaDao,
    EstoqueDao,
    FornecedorDao,
    ClienteDao,
    FuncionarioDao,
    VendasDao,
)


print(
    '================================== Gerenciamento de Mercearia ======================================'
)
print()
print()

while True:
    decisao = input(
        '[1]Categoria [2]Produto [3]Fornecedor [4]Cliente [5]Funcionário [6]Caixa [7]Relatórios [0]Fechar: '
    )

    # caso digite algo que não seja nenhuma opção acima
    try:
        decisao = int(decisao)

        print('')
        match decisao:

            case 0:
                break

            # Área de Cadastro/Alteração/Remoção

            case 1:
                decisao_user = input(
                    '[C]adastrar'
                    + '\n'
                    + '[A]lterar'
                    + '\n'
                    + '[R]emover'
                    + '\n'
                    + '[V]oltar'
                    + '\n'
                ).lower()

                print()

                # Mostrar lista de categoria pro usuário

                if decisao_user == 'c':
                    mostrar = CategoriaDao.lercategoria()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    nome_categoria = input('Nome da categoria: ').upper()
                    CategoriaController.cadastrarCategoria(
                        novaCategoria=nome_categoria
                    )  # Chamando controller

                elif decisao_user == 'a':
                    mostrar = CategoriaDao.lercategoria()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    alterar_categoria = input(
                        'Digite o nome da categoria que deseja alterar: '
                    ).upper()
                    alterada_categoria = input(
                        'Digite o nome da nova categoria alterada: '
                    ).upper()
                    CategoriaController.alterarCategoria(
                        alterarCategoria=alterar_categoria,
                        alteradaCategoria=alterada_categoria,
                    )

                elif decisao_user == 'r':
                    mostrar = CategoriaDao.lercategoria()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    indice_categoria = input(
                        'Digite o nome da categoria que dejesa remover: '
                    ).upper()
                    CategoriaController.removerCategoria(indice_categoria)

                elif decisao_user == 'v':
                    continue

                else:
                    print()
                    print('Desculpe.. Opção inválida. Tente novamente.')
                    print('Opções [C] [R] [A] [V]')
                    print()
                    continue

            # ÁREA DE PRODUTOS

            case 2:
                decisao_user2 = input(
                    '[C]adastrar'
                    + '\n'
                    + '[A]lterar'
                    + '\n'
                    + '[R]emover'
                    + '\n'
                    + '[V]oltar'
                    + '\n'
                ).lower()

                print('')

                if decisao_user2 == 'c':
                    mostrar = (
                        EstoqueDao.ler_produto()
                    )   # Print da lista de produtos(estoque) pro usuário
                    print('---------------')
                    for i in mostrar:
                        print(i, end='')

                    nome = input('Nome do produto: ').upper()
                    preco = input('Valor do produto: R$ ')
                    categoria = input('Categoria do produto: ').upper()
                    quantidade = input('Quantidade do produto para estoque: ')

                    EstoqueController.cadastrar_produto(
                        nome=nome,
                        preco=preco,
                        categoria=categoria,
                        quantidade=quantidade,
                    )

                elif decisao_user2 == 'a':

                    mostrar = EstoqueDao.ler_produto()
                    print('---------------')
                    for i in mostrar:
                        print(i, end='')

                    nome_alterar = input(
                        'Nome do produto que deseja alterar: '
                    ).upper()
                    print('Dados para alteração')
                    nome_alterado = input('Nome do produto: ').upper()
                    valor_alterado = input('Valor do produto: R$').upper()
                    categoria_alterada = input(
                        'Categoria do produto: '
                    ).upper()
                    quantidade_alterada = input(
                        'Digite a quantidade do produto: '
                    ).upper()

                    EstoqueController.alterar_produto(
                        alterar_produto=nome_alterar,
                        nome=nome_alterado,
                        preco=valor_alterado,
                        categoria=categoria_alterada,
                        quantidade=quantidade_alterada,
                    )

                elif decisao_user2 == 'r':

                    mostrar = EstoqueDao.ler_produto()
                    print('---------------')
                    for i in mostrar:
                        print(i, end='')

                    produtoRemovido = input(
                        'Digite nome do produto que deseja remover: '
                    ).upper()
                    EstoqueController.remover_produto(
                        nome_produto=produtoRemovido
                    )

                elif decisao_user2 == 'v':
                    continue

                else:
                    print('')
                    print('Desculpe... Opção inválida. Tente novamente.')
                    print('Opções [C] [R] [A] [V]')
                    print('')
                    continue

            # ÁREA DE FORNECEDOR

            case 3:
                decisao_user3 = input(
                    '[C]adastrar'
                    + '\n'
                    + '[A]lterar'
                    + '\n'
                    + '[R]emover'
                    + '\n'
                    + '[V]oltar'
                    + '\n'
                ).lower()

                print('')

                if decisao_user3 == 'c':

                    mostrar = FornecedorDao.ler_fornecedores()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    nomeForne = input('Nome do fornecedor: ').upper()
                    telefone = input('Número de telefone: ')
                    cnpj = input('Digite CNPJ da empresa: ')
                    categoria = input('DIgite a categoria: ').upper()

                    FornecedorController.cadastrar(
                        nome=nomeForne,
                        telefone=telefone,
                        cnpj=cnpj,
                        categoria=categoria,
                    )

                elif decisao_user3 == 'r':

                    mostrar = FornecedorDao.ler_fornecedores()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    removerFornecedor = input('Nome do fornecedor: ').upper()
                    FornecedorController.remover_fornecedor(
                        nome_fornecedor=removerFornecedor
                    )

                elif decisao_user3 == 'a':

                    mostrar = FornecedorDao.ler_fornecedores()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    alterar = input('Nome do fornecedor: ').upper()
                    print('Informações da alteração do fornecedor')
                    nomeAlt = input('Nome do fornecedor: ').upper()
                    telAlt = input('Digite o telefone: ')
                    cnpjAlt = input('Digite o cnpj: ')
                    catAlt = input('Digite a categoria: ').upper()

                    FornecedorController.alterarFornecedor(
                        alterarForne=alterar,
                        nome=nomeAlt,
                        telefone=telAlt,
                        cnpj=cnpjAlt,
                        categoria=catAlt,
                    )

                elif decisao_user3 == 'v':
                    continue

                else:
                    print('')
                    print(
                        'Desculpe... Opção inválida, tente novamente as opções...'
                    )
                    print('Digite [C] [R] [A] [V]')
                    print('')
                    continue

            # ÁREA DE CLIENTES

            case 4:
                decisao_user4 = input(
                    '[C]adastrar'
                    + '\n'
                    + '[A]lterar'
                    + '\n'
                    + '[R]emover'
                    + '\n'
                    + '[V]oltar'
                    + '\n'
                ).lower()

                print('')

                if decisao_user4 == 'c':

                    mostrar = ClienteDao.ler_clientes()
                    print('-------------')
                    for i in mostrar:
                        print(i, end='')

                    nomeClt = input('Nome do cliente: ').upper()
                    cpfClt = input('Digite o CPF: ').upper()
                    emailClt = input('Digite seu Email: ').lower()
                    telefoneClt = input('Telefone de contato: ')
                    enderecoclt = input('Digite seu endereço: ').upper()

                    ClienteController.cadastrarCliente(
                        nome=nomeClt,
                        cpf=cpfClt,
                        email=emailClt,
                        telefone=telefoneClt,
                        endereco=enderecoclt,
                    )

                elif decisao_user4 == 'r':

                    mostrar = ClienteDao.ler_clientes()
                    print('-------------')
                    for i in mostrar:
                        print(i, end='')

                    remo_client = input(
                        'Digite o nome do cliente que deseja remover: '
                    ).upper()
                    ClienteController.removerCliente(nome_cliente=remo_client)

                elif decisao_user4 == 'a':

                    mostrar = ClienteDao.ler_clientes()
                    print('-------------')
                    for i in mostrar:
                        print(i, end='')

                    alterarCLient = input('Nome do cliente: ').upper()

                    print('Alterar dados: ')

                    nome_cl = input('nome do cliente: ').upper()
                    cpf_cl = input('CPF do cliente: ')
                    email_cl = input('Email do cliente: ').lower()
                    tel_cl = input('Número de telefone: ')
                    end_cl = input('Endereço do cliente: ').upper()

                    ClienteController.alterarCliente(
                        nomeCliente=alterarCLient,
                        nome=nome_cl,
                        cpf=cpf_cl,
                        email=email_cl,
                        telefone=tel_cl,
                        endereco=end_cl,
                    )

                elif decisao_user4 == 'v':
                    continue

                else:
                    print('Desculpe, não consegui fazer sua solicitação')

            # ÁREA DE FUNCIONÁRIO

            case 5:
                decisao_user5 = input(
                    '[C]adastrar'
                    + '\n'
                    + '[A]lterar'
                    + '\n'
                    + '[R]emover'
                    + '\n'
                    + '[V]oltar'
                    + '\n'
                ).lower()

                print('')

                if decisao_user5 == 'c':

                    mostrar = FuncionarioDao.lista_funcionario()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    nome_func = input('Nome do funcionário: ').upper()
                    cpf_func = input('Digite o CPF: ')
                    email_func = input('Digite o email: ').lower()
                    tel_func = input('Telefone de contato: ')
                    end_func = input('Digite o endereço com Nº: ').upper()
                    clt_func = input(
                        'Empregado com carteira asssinada: '
                    ).upper()

                    FuncionarioController.cadastrar_funcionario(
                        nome=nome_func,
                        cpf=cpf_func,
                        email=email_func,
                        telefone=tel_func,
                        endereco=end_func,
                        clt=clt_func,
                    )

                elif decisao_user5 == 'r':

                    mostrar = FuncionarioDao.lista_funcionario()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    nome_funcionario = input('Nome do funcionário: ').upper()
                    FuncionarioController.remover_funcionario(
                        remover_func=nome_funcionario
                    )

                elif decisao_user5 == 'a':

                    mostrar = FuncionarioDao.lista_funcionario()
                    print('--------------')
                    for i in mostrar:
                        print(i, end='')

                    nome_alterar = input(
                        'Digite o nome do funcionário que deseja alterar: '
                    ).upper()
                    print('')
                    print('Dados para alteração')
                    print('')
                    nome_f = input('Digite o nome: ').upper()
                    cpf_f = input('Digite o CPF: ')
                    email_f = input('Digite Email: ').lower()
                    telefone_f = input('Número de telefone: ')
                    endereco_f = input(
                        'Digite o nome do endereço com número: '
                    ).upper()
                    clt_f = input('Carteira assinada: [S]im [N]ão: ').upper()

                    FuncionarioController.alterar_funcionario(
                        nome_funcionario=nome_alterar,
                        nome=nome_f,
                        cpf=cpf_f,
                        email=email_f,
                        telefone=telefone_f,
                        endereco=endereco_f,
                        clt=clt_f,
                    )

                elif decisao_user5 == 'v':
                    continue

                else:
                    print('Caractere inválido')
                    continue

            # ÁREA DE CAIXA

            case 6:
                decisao_user6 = input('[1]Venda [2]Sair: ')
                try:
                    decisao_user6 = int(decisao_user6)
                except:
                    print('Opção inválida..')
                    continue

                if decisao_user6 == 1:

                    cpf_usr = input('CPF do usuário: ')
                    vendedor_caixa = input('Nome do funcionário: ').upper()

                    itens_vendidos = input('Nome do produto: ').upper()
                    quant = input('Quantidade vendida: ')
                    quant = int(quant)
                    valor_passado = input('Valor total do comprador: ')
                    valor_passado = int(valor_passado)

                    VendasController.caixa_controller(
                        comprador=cpf_usr,
                        itens_vendidos=itens_vendidos,
                        vendedor=vendedor_caixa,
                        quantidade_vendida=quant,
                        valor_total=valor_passado,
                    )

                elif decisao_user6 == 2:
                    continue

                else:
                    print('Desculpe... Não consegui concluir sua solicitação')
                    continue

            case 7:

                decisao_user7 = input(
                    '[V]Relatório total de vendas'
                    + '\n'
                    + '[D]Relatório  de vendas por data'
                    + '\n'
                ).lower()

                # DESENVOLVIMENTO
                if decisao_user7 == 'v':
                    RelatoriosProdController.relatoria_produtos()

                elif decisao_user7 == 'd':
                    
                    data_inicial = input('Digite a data de inicio: ')
                    data_final = input('Digite a data final: ')

                    try:
                        RelatorioData.relatorio_data(
                                data_inicio=data_inicial,
                                data_termino=data_final
                        )
                    except:
                        print('Obrigatório o uso de /')


    except:
        print('Caractere inválido..')
        continue
