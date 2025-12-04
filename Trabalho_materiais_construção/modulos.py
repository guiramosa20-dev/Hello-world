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
        codigo = int(input(f'Código do novato{_+1}º:\n100 - Caixa\n200 - Conferente\n200 - Administrativo\n...').strip())
        #Verifica se o código é válido:
        if codigo != 100 and codigo != 200 and codigo != 300:
            print('\033[31m Código inválido!\033[m')
        #Adiciona funcionário ao registro:
        else:
            novato.codigo = codigo
            novato.nome = input(f'Nome do novato{_+1}º: ').title().strip()
            novato.senha = input(f'senha do novato{_+1}º: ').strip()
        
    salvarDados('funcionarios.json',efetivo)
    print('\033[32mFuncionário(s) cadastrado(s) com sucesso!\033[m')

#checa se o funcionário está cadastrado:
def checarFuncionario(code,name,passe):#Onde: code = codigo, name = nome e passe = senha, efetivo = funcionários
    with open('funcionarios.json','r', encoding='utf-8') as efetivo:
        data = json.load(efetivo)
        for i in range(len(data)):
            if data[i]['codigo'] == code and data[i]['nome'] == name and data[i]['senha'] == passe:
                achou = True
                break
    return achou

#adiciona mercadoria ao estoque
def addMercadoria():#Onde a variávelestoque = MERCADORIA()
    print('Nova mercadoria:')
    estoque = PRODUTO() #estoque deve se tornar uma lista e PRODUTO() deve ser adicionado à ela
    estoque.codigo = int(input('Código da mercadoria: ').strip())
    estoque.quantidade = int(input('Quantidade da mercadoria: ').strip())
    estoque.preco = float(input('Preço da mercadoria: ').strip())

    return estoque

