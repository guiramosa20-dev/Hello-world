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
    for _ in range(i):
        novato = FUNCIONARIO()
        efetivo.append(novato)
        codigo = int(input(f'Código do {_+1}º novato:\n100 - Caixa\n200 - Conferente\n200 - Administrativo\n...').strip())
        #Verifica se o código é válido:
        if codigo != 100 and codigo != 200 and codigo != 300:
            print('\033[31m Código inválido!\033[m')
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

#adiciona mercadoria ao estoque
def addMercadoria():#Onde a variávelestoque = MERCADORIA()
    estoque = []

    i = int(input('Número de mercadorias a serem cadastradas: ').strip())
    
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
        data = json.load(arquivo)
        codigo = int(input('Código da mercadoria a ser removida: ').strip())
        for i in range(len(data)):
            if data[i]['codigo'] == codigo:
                del data[i]
                print('\033[32mMercadoria removida com sucesso!\033[m')
                break
        else:
            print('\033[31mMercadoria não encontrada!\033[m')

