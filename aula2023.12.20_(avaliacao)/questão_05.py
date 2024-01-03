"""
Questão 05

• Faça a abstração de superclasse Formas Geométricas.

Obs: você deve fazer o cálculo da área e do perímetro das formas
Obs: você deve fazer quantos str forem necessarios para sua abstração

----------------------------
|    FormasGeometricas    |
----------------------------

"""
class FormasGeometricas:
    def __init__(self, figura_geometrica):
        self.figura_geometrica = figura_geometrica
    
    def get_figura_geometrica(self):
        return self.figura_geometrica

class Retangulo(FormasGeometricas):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        area = self.largura * self.comprimento  
        return area                    

    def calcular_perimetro(self):
        perimetro = 2*self.largura + 2*self.comprimento
        return perimetro

    def __str__(self):
        return f'Comprimento: {self.comprimento}cm, Lagura: {self.largura}cm, Area: {self.calcular_area()}m, Perimento: {self.calcular_perimetro()}m'

r = Retangulo(4,10)
print(r) 