import json
from dataclasses import asdict
from registros import *

#salvamento de dados em .json:
def salvarDados(ARQUIVO,registro):
    try:
        with open(ARQUIVO,'w', encoding='utf-8') as arquivo:
            json.dump([asdict(p) for p in registro], arquivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'\033[31mErro ao salvar arquivo: {e}\033[m')

#Cadastro de funcionário novo:
def addFuncionario():#Onde: a variávelefetivo = FUNCIONÁRIOS()
    
    i = int(input('Número de funcionários a serem cadastrados: ').strip())
    efetivo = []
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
    with open('estoque.json','r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    while True:
        somaPreco = 0.0
        achou = False

        try:
            codigo = int(input('Código da mercadoria: ').strip())
        except ValueError:
            codigo = 10

        if codigo == 0:
            break
        for i in range(len(dados)):
            if dados[i]['codigo'] == codigo:
                achou = True

        if achou:
            quantidade = int(input('Quantidade comprada: ').strip())
            if quantidade <= dados[i]['quantidade']:
                somaPreco += dados[i]['preco'] * quantidade
                dados[i]['quantidade'] -= quantidade
                print(f'\033[32mCompra registrada! Total: R$ {somaPreco:.2f}\033[m')

                # salvamento dos dados atualizados no estoque
                salvarDados('estoque.json',dados)
            else:
                print('\033[31mQuantidade indisponível em estoque!\033[m')
        else:
            print('\033[31mMercadoria não encontrada!\033[m')

#adiciona mercadoria ao estoque
def addMercadoria():#Onde a variávelestoque = MERCADORIA()
    '''
    try:
        with open('estoque.json','r', encoding='utf-8') as arquivo:
            existe = json.load(arquivo)
    except FileNotFoundError:
        pass
    '''
    estoque = []
    try:
        i = int(input('Quantidade de mercadorias a serem cadastradas: ').strip())
    except ValueError:
        i = 1
    
    for _ in range(i):
        novo = PRODUTO() #estoque deve se tornar uma lista e PRODUTO() deve ser adicionado à ela
        novo.codigo = int(input(f'Código da {_+1}ª mercadoria: ').strip())
        novo.nome = input(f'Nome da {_+1}ª mercadoria: ').strip().title()
        novo.descricao = input(f'Descrição da {_+1}ª mercadoria: ').strip()
        novo.quantidade = int(input(f'Quantidade da {_+1}ª mercadoria: ').strip())
        novo.preco = float(input(f'Preço da {_+1}ª mercadoria: ').strip())
        estoque.append(novo)

    salvarDados('estoque.json',estoque)
    print('\033[32mMercadoria(s) cadastrada(s) com sucesso!\033[m')

#excluir mercadoria do estoque
def removeMercadoria():
    with open('estoque.json','r', encoding='utf-8') as arquivo:
        data = json.load(arquivo) #dados carregados na memória RAM
        try:
            codigo = int(input('Código da mercadoria a ser descartada: ').strip())
        except ValueError:
            codigo = 0
        for i in range(len(data)):
            if data[i]['codigo'] == codigo:
                del data[i]
                print('\033[32mMercadoria removida com sucesso!\033[m')
                break
        else:
            print('\033[31mMercadoria não encontrada!\033[m')

