"""
Questão 01

• Faça a abstração da superclasse Veículo. Você deve ter pelo menos duas subclasses, nove atributos e 12 metodos.

Obs: você deve fazer o str de cada uma delas

------------------
|    Veiculos    |
------------------

"""

class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def get_tipo(self):
        return self.tipo
    
    def get_chassi(self):
        return self.chassi
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_anoo(self):
        return self.ano

    @property
    def ano(self):
        return self._ano

    @_ano.setter
    def _ano(self, valor: int):
        self._ano = valor

    
class Carro(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, consumo, kilometragem, capacidade_tanque):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.__consumo = consumo                      # km/litro
        self.__kilometragem = kilometragem            # Km atual do carro
        self.__capacidade_tanque = capacidade_tanque  # definir quantidade de combustível que cabe no tanque
        self.__combustivel_no_tanque = 0              # carro começa com tanque sem combustível

    def __verifica_tanque(self, valor):
        if ((self.__combustivel_no_tanque + valor) <= self.__capacidade_tanque): # verifica se o combustível vai caber no tanque
            return valor
        else:   #se não couber, vai completar o tanque
            return (self.__capacidade_tanque - self.__combustivel_no_tanque) #retorna o que ainda cabe no tanque

    def abastecer(self, volume):   # abastecer o carro com valor solicitado ou completar a capacidade
        abastecer = self.__verifica_tanque(volume)
        self.__combustivel_no_tanque += abastecer
        print("Tanque abastecido com {} litros de combustível. Seu tanque agora tem {} litros".format(abastecer, self.__combustivel_no_tanque))

    def __pode_andar(self, kilometragem):  # verifica se a quantidade de combustível no tanque é suficiente para rodar os Km solicitados
        consumo = (kilometragem / self.__consumo) # litros que serão gastos na quilometragem percorrida
        return (self.__capacidade_tanque >= consumo)

    def andar(self, km): #Roda os km e adiciona no odometro do carro / reduz o combustível do tanque
        if (self.__pode_andar(km)):
            self.__kilometragem += km
            self.__combustivel_no_tanque -= (km / self.__consumo)
        else:
            print("Combustível insuficiente para andar {}Km".format(km))

    def tanque(self): #imprime a quantidade de litros que tem no tanque
        print("Restam {} litros no tanque de combustível".format(self.__combustivel_no_tanque))

    #propriedades da Classe Carro
    @property
    def consumo(self):
        return self.__consumo

    @property
    def capacidade_tanque(self):
        return self.__capacidade_tanque

    @property
    def kilometragem(self):
        return self.__kilometragem

    @property
    def combustiven_no_tanque(self):
        return self.__combustivel_no_tanque
    

class Motorbike(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano,  potencia):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.potencia = potencia

    def começar(self):
        if self._verificar_gasolina:
            print("Partida da moto!")
        print("Sem gasolina")

    def parar(self):
        print("Parando a moto")

    def _verificar_gasolina(self):
        return False
