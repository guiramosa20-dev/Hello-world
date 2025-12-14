from unittest import case
from registros import *
from modulos import *

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
                print('-'*40)
                print('Gerenciamento administrativo:')
                print('-'*40)
                print('1 - Relatório de vendas')
                print('2 - Relatório de estoque')
                print('3 - Mudar dados de um produto')
                print('4 - Mudar dados de um funcionário')
                print('5 - Excluir produto')
                print('6 - Excluir funcionário')
                print('7 - Sair')
                try:
                    escolha2 = int(input('...').strip())
                except ValueError:
                    escolha2 = 0
                
                match escolha2:
                    case 1:
                        relatorioVendas()
                    case 2:
                        relatorioEstoque()
                    case 3:
                        alteraProduto()
                    case 4:
                        alteraFuncionario()
                    case 5:
                        removeMercadoria()
                    case 6:
                        removeFuncionario()
                    case 7:
                        break
                    case _:
                        print('\033[31mOpção inválida!\033[m')

        case _:
            print('\033[31mOpção inválida!\033[m')


