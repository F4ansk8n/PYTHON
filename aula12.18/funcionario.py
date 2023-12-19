# crie abstracao para uma super classe funcionario com duas subclasses. imprima todos os dados
class Funcionarios:
    def __init__(self, nome):
        self.nome = nome
    
    #get
    def get_nome(self):
        return self.nome 
    
    #set
    def set_nome(self):
        return self.nome
    

class Contratados(Funcionarios):
    pass

class Estagiario(Funcionarios):
    pass


