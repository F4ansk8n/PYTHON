class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.comida = 100

    # get
    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso
    
    def get_fome(self):
        return self.fome
    

    
    # set
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_peso(self, novo_peso):
        self.peso = novo_peso
    
    def set_fome(self, nova_fome):
        self.fome += nova_fome
        if self.fome >= 99:
            print(f'Alimente a/o {self.nome}')
            nova_comida = input('Quanto de comida você quer dar para seu Pet? ')
            self.comida = nova_comida
            self.comida -= nova_comida
            self.fome -= nova_comida
    

    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'Estou pesando {self.peso} kg')
        print(f'Minha fome está em {self.fome}')


caozinho = Pet('Bodo', 10)

caozinho.set_fome(20)
caozinho.imprimir()

caozinho.set_fome(50)
caozinho.imprimir()


