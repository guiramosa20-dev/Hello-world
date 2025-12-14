import json
from dataclasses import asdict, replace
from registros import *

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
                original[i] = replace(original[i], **{registro: novoValor})
    
    else:
        for i in range(len(original)):
            if i == index:
                original[i] = replace(original[i], **{registro: novoValor})
    
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

