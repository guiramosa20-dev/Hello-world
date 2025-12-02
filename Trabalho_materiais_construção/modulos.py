from registros import *

#Cadastro de funcionário novo:
def addFuncionario():#Onde: a variávelefetivo = FUNCIONÁRIOS()
    
        print('Novo funcionário:')
        efetivo = FUNCIONARIO() #efetivo deve se tornar uma lista e FUNCIONARIO() deve ser inserido dentro dela
        codigo = int(input('Código do novato:\n100 - Caixa\n200 - Conferente\n200 - Administrativo\n...').strip())
        #Verifica se o código é válido:
        if codigo != 100 and codigo != 200 and codigo != 300:
            print('\033[31m Código inválido!\033[m')
        #Adiciona funcionário ao registro:
        else:
            efetivo.codigo = codigo
            efetivo.nome = input('Nome do novato: ').title().strip()
            efetivo.senha = input('senha do novato: ').strip()
        return efetivo

#checa se o funcionário está cadastrado:
def checarFuncionario(code,name,passe,efetivo):#Onde: code = codigo, name = nome e passe = senha, funcionários
    i = len(efetivo)
    achou = False
    for indiceEfetivo in range(i):
        if  code == efetivo[indiceEfetivo].codigo and name == efetivo[indiceEfetivo].nome and passe == efetivo[indiceEfetivo].senha:
             achou = True

    return achou

#adiciona mercadoria ao estoque
def addMercadoria():#Onde a variávelestoque = MERCADORIA()
    print('Nova mercadoria:')
    estoque = PRODUTO() #estoque deve se tornar uma lista e PRODUTO() deve ser adicionado à ela
    estoque.codigo = int(input('Código da mercadoria: ').strip())
    estoque.quantidade = int(input('Quantidade da mercadoria: ').strip())
    estoque.preco = float(input('Preço da mercadoria: ').strip())

    return estoque
