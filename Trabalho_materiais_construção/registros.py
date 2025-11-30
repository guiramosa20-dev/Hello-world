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
    vedas: int = ''
    quantidade = ''