'''
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_valor_lado(self, novoValor):
        self.lado = novoValor

    def retornar_valor_lado(self):
        print(self.lado)

    def calcular_area(self):
        area = self.lado**2
        print(area)

Q1 = Quadrado(3)

print(Q1.__dict__)
Q1.retornar_valor_lado()
Q1.calcular_area()

Q1.mudar_valor_lado(4)      #atributo lado alterado para 4
print(Q1.__dict__)
Q1.retornar_valor_lado()
Q1.calcular_area()