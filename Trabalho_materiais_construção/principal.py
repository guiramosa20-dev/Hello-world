from unittest import case
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
        print('Escolha:\n 1 - Fazer Login \n 2 - Cadastrar funcionário \n 3 - Sair')
        try:
            escolha = int(input('...').strip())
        except ValueError:
            escolha = 0

        match escolha:
            case 1:#cadastro de 1 funcionário
                print('-'*20)
                print('Faça seu login:')
                try:
                    codigo = int(input('Código: ').strip())
                except ValueError:
                    print('\033[31mPor favor, insira um número válido para o código.\033[m')
                    continue
                nome = input('Nome: ').strip().title()
                senha = getpass('Senha: ')

                if checarFuncionario(codigo,nome,senha):#Verificando se o funcionário está cadastrado
                    return codigo
                else:
                    print('\033[31mFuncionário não cadastrado!\033[m')
    
            case 2:#Login
               addFuncionario()

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
    match escolha2:#vendas
        case 100:
            while True:
                print('-'*20)
                print('1 - Registrar compras:')
                print('2 - Sair')
                print('-'*20)
                try:
                    escolha2 = int(input('...').strip())
                except ValueError:
                    escolha2 = 0

                match escolha2:
                    case 1:
                        venda()
                    case 2:
                        break
                    case _:
                        print('\033[31mOpção inválida!\033[m')
                        
        case 200:#estoque
            while True:
                print('-'*20)
                print('Gerenciar estoque:')
                print('-'*20)
                print('1 - Adicionar mercadoria')
                print('2 - Remover mercadoria')
                print('3 - Sair')
                try:
                    escolha2 = int(input('...').strip())
                except ValueError:
                    escolha2 = 0

                match escolha2:#adição de mercadoria
                    case 1:
                        addMercadoria()
                    case 2:# remoção de mercadoria
                        removeMercadoria()
                    case 3:
                        break
                    case _:
                        print('\033[31mOpção inválida!\033[m')

        case 300:#Gerenciamento administrativo
            while True:
                print('Relatório de vendas')
                print('Relatório de estoque')
                print('Mudar descrição de produto')
                print('Nodar descrição de funcionário')
                print('Excluir produto')
                print('Excluir funcionário')
        case _:
            print('\033[31mOpção inválida!\033[m')


