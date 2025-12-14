import json
from dataclasses import asdict, replace
from registros import *
from getpass import getpass
from time import sleep

#/////////////////////////// Funções de manipulação de dados ///////////////////////////////
#salvamento de dados em .json:
def salvarDados(ARQUIVO,registro):
    try:
        with open(ARQUIVO,'w', encoding='utf-8') as arquivo:
            json.dump([asdict(p) for p in registro], arquivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'\033[31mErro ao salvar arquivo: {e}\033[m')

#carregamento de dados de .json:
def carregarDados(ARQUIVO):
    try:
        with open(ARQUIVO,'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        if ARQUIVO == 'funcionarios.json':
            return [FUNCIONARIO(**item) for item in dados]
        elif ARQUIVO == 'estoque.json':
            return [PRODUTO(**item) for item in dados]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

#alteração de dados em registros: off to see the wizard
def alteraDados(ARQUIVO,index,registro,novoValor):
    original = carregarDados(ARQUIVO)
    
    if ARQUIVO == 'funcionarios.json':
        for i in range(len(original)):
            if i == index:
                try:
                    original[i] = replace(original[i], **{registro: novoValor})
                except TypeError:
                    return
    
    else:
        for i in range(len(original)):
            if i == index:
                try:
                    original[i] = replace(original[i], **{registro: float(novoValor) if registro == 'preco' else int(novoValor) if registro == 'quantidade' else novoValor})
                except TypeError:
                    return
    
    salvarDados(ARQUIVO,original)

#//////////////////////////// Funções específicas do sistema ///////////////////////////////
   
#Cadastro de funcionário novo:
def addFuncionario():#Onde: a variávelefetivo = FUNCIONÁRIOS()
    
    i = int(input('Número de funcionários a serem cadastrados: ').strip())
    efetivo = carregarDados('funcionarios.json')
    reconta = 0
    for _ in range(i):
        _ += reconta
        novato = FUNCIONARIO()
        efetivo.append(novato)

        try:
            codigo = int(input(f'Código do {_+1}º novato:\n100 - Caixa\n200 - Conferente\n200 - Administrativo\n...').strip())
        except ValueError:
            codigo = 0
            
        #Verifica se o código é válido:
        if codigo != 100 and codigo != 200 and codigo != 300:
            print('\033[31m Código inválido!\033[m')
            reconta += _ -1
            continue
        #Adiciona funcionário ao registro:
        else:
            novato.codigo = codigo
            novato.nome = input(f'Nome do {_+1}º novato: ').title().strip()
            novato.senha = input(f'Senha do {_+1}º novato: ').strip()
        
    salvarDados('funcionarios.json',efetivo)
    print('\033[32mFuncionário(s) cadastrado(s) com sucesso!\033[m')

#checa se o funcionário está cadastrado:
def checarFuncionario(code,name,passe):#Onde: code = codigo, name = nome e passe = senha, efetivo = funcionários
    achou = False

    with open('funcionarios.json','r', encoding='utf-8') as efetivo:
        data = json.load(efetivo)
        for i in range(len(data)):
            if data[i]['codigo'] == code and data[i]['nome'] == name and data[i]['senha'] == passe:
                achou = True
                break
    return achou

#registro de vendas:
def venda():
    try:
        with open('estoque.json','r', encoding='utf-8') as arquivo:
            estoque= json.load(arquivo)
    except FileNotFoundError:
        estoque = []
    except json.JSONDecodeError:
        estoque = []

    somaPreco = 0.0
    while True:

        achou = False

        try:
            codigo = int(input('Código da mercadoria: ').strip())
        except ValueError:
            codigo = 10

        if codigo == 0:
            break
        for i in range(len(estoque)):
            if estoque[i]['codigo'] == codigo:
                achou = True
                break

        if achou:
            quantidade = int(input('Quantidade comprada: ').strip())
            if quantidade <= estoque[i]['quantidade']:
                somaPreco += estoque[i]['preco'] * quantidade
                estoque[i]['quantidade'] -= quantidade
                estoque[i]['vendas'] += 1

                #se algo der errado, provavelmente é aqui
                alteraDados('estoque.json',i,'vendas',estoque[i]['vendas'])
                alteraDados('estoque.json',i,'quantidade',estoque[i]['quantidade'])

            else:
                print('\033[31mQuantidade indisponível em estoque!\033[m')
        else:
            print('\033[31mMercadoria não encontrada!\033[m')

    print(f'\033[32mCompra registrada! Total: R$ {somaPreco:.2f}\033[m')

#adiciona mercadoria ao estoque
def addMercadoria():#Onde a variávelestoque = MERCADORIA()
    estoque = carregarDados('estoque.json')
    try:
        i = int(input('Quantidade de mercadorias a serem cadastradas: ').strip())
    except ValueError:
        i = 1
    
    reconta = 0
    for _ in range(i):
        _ += reconta
        
        novo = PRODUTO()
        
        #validar e cadastrar código
        num = int(input(f'Código da {_+1}ª mercadoria: ').strip())
        
        if type(num) != int:
            print('\033[31mCódigo inválido!\033[m')
            reconta += _ -1
            continue
        elif any(novo.codigo == num for novo in estoque):
            print('\033[31mCódigo já cadastrado!\033[m')
            reconta += _ -1
            continue
        else:
            novo.codigo = num
        novo.nome = input(f'Nome da {_+1}ª mercadoria: ').strip().title()
        novo.descricao = input(f'Descrição da {_+1}ª mercadoria: ').strip()

        #validar e cadastrar quantidade
        qtd = input(f'Quantidade da {_+1}ª mercadoria: ').strip()
        if type(qtd) != int:
            print('\033[31mQuantidade inválida!\033[m')
            reconta += _ -1
            continue
        else:
            novo.quantidade = qtd
        
        #criar keyword vendas e inicializá-la em 0:
        novo.vendas = 0
        
        #validar e cadastrar preço
        price = input(f'Preço da {_+1}ª mercadoria: ').strip()

        if type(price) != float:
            print('\033[31mPreço inválido!\033[m')
            reconta += _ -1
            continue
        else:
           novo.preco = price
    
        estoque.append(novo)

    salvarDados('estoque.json',estoque)
    print('\033[32mMercadoria(s) cadastrada(s) com sucesso!\033[m')

#excluir mercadoria do estoque
def removeMercadoria():
    data = carregarDados('estoque.json')
    try:
        codigo = int(input('Código da mercadoria a ser descartada: ').strip())
    except ValueError:
        codigo = 0
    for i in range(len(data)):
        if data[i].codigo == codigo:
            del data[i]
            salvarDados('estoque.json',data)
            print('\033[32mMercadoria removida com sucesso!\033[m')
            break
        else:
            print('\033[31mMercadoria não encontrada!\033[m')

def relatorioVendas():
    try:
        with open('estoque.json','r', encoding='utf-8') as arquivo:
            estoque= json.load(arquivo)
    except FileNotFoundError:
        estoque = []
    except json.JSONDecodeError:
        estoque = []

    estoque.sort(key=lambda x: x['vendas'], reverse=True)
    print('-'*40)
    print(f'{"Relatório de Vendas":^40}')
    print('-'*40)
    print(f'{"Código":<10}{"Nome":<15}{"Vendas":>15}')
    print('-'*40)
    for i in range(len(estoque)):
        print(f'{estoque[i]["codigo"]:<10}{estoque[i]["nome"]:<15}{estoque[i]["vendas"]:>15}')
    print('-'*40)

def relatorioEstoque():
    try:
        with open('estoque.json','r', encoding='utf-8') as arquivo:
            estoque= json.load(arquivo)
    except FileNotFoundError:
        estoque = []
    except json.JSONDecodeError:
        estoque = []

    print('-'*80)
    print(f'{"Relatório de Estoque":^80}')
    print('-'*80)
    print(f'{"Código":<10}{"Nome":<20}{"Descricao":<20}{"Quantidade":<15}{"Preço (R$)":>15}')
    print('-'*80)
    for i in range(len(estoque)):
        print(f'{estoque[i]["codigo"]:<10}{estoque[i]["nome"]:<20}{estoque[i]["descricao"]:<20}{estoque[i]["quantidade"]:<15}{estoque[i]["preco"]:>15.2f}')
    print('-'*80)

def alteraProduto():
    try:
        with open('estoque.json','r', encoding='utf-8') as arquivo:
            estoque= json.load(arquivo)
    except FileNotFoundError:
        estoque = []
    except json.JSONDecodeError:
        estoque = []

    codigo = int(input('Código do produto a ter a descrição alterada: ').strip())
    print()
    print('-'*20)
    print('Dados atuais do produto:')
    print('-'*20)
    for i in range (len(estoque)):
        if estoque[i]['codigo'] == codigo:
            print(f'Código: {estoque[i]["codigo"]}')
            print(f'Nome: {estoque[i]["nome"]}')
            print(f'Descrição: {estoque[i]["descricao"]}')
            print(f'Quantidade: {estoque[i]["quantidade"]}')
            print(f'Preço: R$ {estoque[i]["preco"]:.2f}')
            print('-'*20)

            chave = ''
            print('qual dado deseja alterar?\n1 - Nome\n2 - Descrição\n3 - Quantidade\n4 - Preço\n5 - Cancelar')

            data = int(input('...').strip())

            match data:
                case 1:
                    chave = 'nome'
                case 2:
                    chave = 'descricao'
                case 3:
                    chave = 'quantidade'
                case 4:
                    chave = 'preco'
                case 5:
                    return
                case _:
                    print('\033[31mOpção inválida!\033[m')

            novaDescricao = input('Nova descrição: ').strip()
            alteraDados('estoque.json',i,chave,novaDescricao)
            print('\033[32mDescrição alterada com sucesso!\033[m')
            break
    else:
        print('\033[31mProduto não encontrado!\033[m')
    
def alteraFuncionario():
    try:
        with open('funcionarios.json','r', encoding='utf-8') as arquivo:
            efetivo= json.load(arquivo)
    except FileNotFoundError:
        efetivo = []
    except json.JSONDecodeError:
        efetivo = []

    nome = input('Nome do funcionário a ter a descrição alterada: ').strip().title()
    print()
    print('-'*20)
    print('Dados atuais do funcionário:')
    print('-'*20)
    for i in range (len(efetivo)):
        if efetivo[i]['nome'] == nome:
            print(f'Código: {efetivo[i]["codigo"]}')
            print(f'Nome: {efetivo[i]["nome"]}')
            print(f'Senha: {efetivo[i]["senha"]}')
            print('-'*20)

            print('qual dado deseja alterar?\n1 - Código\n2 - Nome\n3 - Senha\n4 - Cancelar')
            data = int(input('...').strip())

            match data:
                case 1:
                    chave = 'codigo'
                case 2:
                    chave = 'nome'
                case 3:
                    chave = 'senha'
                case 4:
                    return
                case _:
                    print('\033[31mOpção inválida!\033[m')

            novaDescricao = input('Nova descrição: ').strip()
            alteraDados('funcionarios.json',i,chave,novaDescricao)
            print('\033[32mDescrição alterada com sucesso!\033[m')
            break
    else:
        print('\033[31mFuncionário não encontrado!\033[m')
    
def removeFuncionario():
    data = carregarDados('funcionarios.json')
        
    try:
        nome = input('Nome do funcionário a ser removido: ').strip().title()
    except ValueError:
        nome = ''
    for i in range(len(data)):
        if data[i].nome == nome:
            del data[i]
            salvarDados('funcionarios.json',data)
            print('\033[32mFuncionário removido com sucesso!\033[m')
            break
    else:
        print('\033[31mFuncionário não encontrado!\033[m')

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
