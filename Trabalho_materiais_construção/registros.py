from dataclasses import dataclass

@dataclass

class FUNCIONARIO:
    codigo: int = 0
    nome: str = ''
    senha: str = ''

@dataclass

class PRODUTO:
    codigo: int = 0
    nome: str = ''
    senha: str = ''
    vendas: int = 0 #p/ possível implementação futura
    quantidade: int = 0
    preco: float = 0.0