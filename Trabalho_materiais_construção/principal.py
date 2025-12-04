from registros import *
from modulos import *
from getpass import getpass
from time import sleep

#/////////////////////////// Função de login //////////////////////////////////
def login():
    # Cabeçalho de inicialização do código:
    print('-'*20)
    print(''*5,'Casa do Prego')
    print('-'*20)
    print('-')

    while True:
        # Gerenciamento do acesso do funcionário:
        print('Escolha:\n 1 - Cadastrar Funcionário \n 2 - Fazer Login \n 3 - Sair')
        escolha = int(input('...').strip())

        match escolha:
            case 1:#cadastro de 1 funcionário
                addFuncionario()
    
            case 2:#Login
                print('-'*20)
                print('Faça seu login:')
                codigo = int(input('Código: ').strip())
                nome = input('Nome: ').strip().title()
                senha = getpass('Senha: ')

                if checarFuncionario(codigo,nome,senha):#Verificando se o funcionário está cadastrado
                    return codigo
                else:
                    print('\033[31mFuncionário não cadastrado!\033[m')

            case 3:#Sair
                print('Saindo...')
                sleep(3)
                return 3
                
            case _:#Informa que a opção escolhida é inválida
                print('\033[31mOpção inválida!\033[m')

#/////////////////////////// Main code //////////////////////////////////

#Daqui pra baixo os prints são apenas placeholders para as funcionalidades que vão ser implementadas
while True:
    escolha2 = login()
    if escolha2 == 3:
        break
    match escolha2:
        case 100:
            while True:
                print('Registrar compras:')
                print('-'*20)

        case 200:
            while True:
                print('-'*20)
                print('Gerenciar estoque:')
                print('-'*20)
                print('1 - Adicionar mercadoria')
                print('2 - Remover mercadoria')
                print('3 - Sair')

                escolha3 = int(input('...').strip())

                match escolha3:
                    case 1:
                        addMercadoria()
                    case 2:
                        removeMercadoria()
                    case 3:
                        break
                    case _:
                        print('\033[31mOpção inválida!\033[m')

        case 300:
            while True:
                print('Relatório de vendas')
                print('Relatório de estoque')
                print('Relatório de produtos descartados')
                print('Mudar descrição de produto')
                print('Nodar descrição de funcionário')
                print('Excluir produto')
                print('Excluir funcionário')
        case _:
            print('\033[31mOpção inválida!\033[m')


