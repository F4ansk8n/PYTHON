'''
Faca um sistema de controle de estoque que atenda as seguintes regras

1. cadrastro de produtos
2. controle de validade
3. controle de quantidade

'''
from datetime import datetime

class ControleEstoque:
    def __init__(self, produto, validade, quantidade):
        self.produto = produto
        self.validade = validade
        self.quantidade = quantidade
        self.dia = '01/02/2024'

    #  GETS
    def get_produto(self):
        return self.produto

    def get_validade(self):
        dia_coverter = datetime.strptime(self.dia, '%m/%d/%Y') 
        validade_coverter = datetime.strptime(self.validade, '%m/%d/%Y') 
        dias = (validade_coverter - dia_coverter).days
        
        if dias < 10:
            print(f'precisa repot o produto')
        else:
            print(f'produto ok')

    # SETS
    def set_produto(self, novo_produto):
        self.produto = novo_produto
        return novo_produto
    
    def set_validade(self, novo_dia):
        self.validade = novo_dia
        return novo_dia

    def __str__(self):
        return f'{self.produto},{self.validade},{self.quantidade}'

    
a = ControleEstoque('arroz','01/20/2024','3')
# print(a)
a.get_validade()