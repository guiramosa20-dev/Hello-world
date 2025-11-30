from registros import *

#Cadastro de funcionário novo:
def addFuncionario():#Onde: efetivo = funcionarios
    
        print('Novo funcionário:')
        efetivo = FUNCIONARIO()
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
    for j in range(i):
        if  code == efetivo[j].codigo and name == efetivo[j].nome and passe == efetivo[j].senha:
             achou = True
    return achou