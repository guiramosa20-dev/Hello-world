from registros import *
from modulos import *
from getpass import getpass

def login():
    # Cabeçalho de inicialização do código:
    print('-'*20)
    print(''*5,'Casa do Prego')
    print('-'*20)
    print('-')
    funcionarios = []

    while True:
        # Gerenciamento do acesso do funcionário:
        print('Escolha:\n 1 - Cadastrar Funcionário \n 2 - Fazer Login')
        escolha = int(input('...').strip())

        match escolha:
            case 1:#cadastro de 1 funcionário
                funcionarios.append(addFuncionario())
    
            case 2:#Login
                codigo = int(input('Código: ').strip())
                nome = input('Nome: ').strip()
                senha = getpass('Senha: ')

                if checarFuncionario(codigo,nome,senha,funcionarios):#Verificando se o funcionário está cadastrado
                    return codigo
                else:
                    print('\033[31mFuncionário não cadastrado!\033[m')

            case _:#Informa que a opção escolhida é inválida
                print('\033[31mOpção inválida!\033[m')
    
# Main
escolha2 = login()

#Daqui pra baixo os prints são apenas placeholders para as funcionalidades que vão ser implementadas
match escolha2:
    case 100:
        while True:
            print('Registrar compras:')
            print('-'*20)

    case 200:
        while True:
            #print('Registro de Entrega de Mercadoria:')
            print()
            print('Entrega de Mercadoria:')
            print('-'*20)
            #addMercadoria()
    case 300:
        while True:
            print('Relatório de vendas')
            print('Relatório de estoque')
            print('Relatório de produtos descartados')
            print('Mudar descrição de produto')
            print('Nodar descrição de funcionário')
            print('Excluir produto')
            print('Excluir funcionário')

