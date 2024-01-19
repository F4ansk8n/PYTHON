"""
Questão 04

• Faça a abstração de superclasse Bichinho Virtual. Você deve ter os atributos: nome, energia, brincar e dormir

Regras: ao brincar o bichinho gasta energia e se a energia atingir um nivel imposto por você ele deve dormir para recarregar.

Obs: você deve ter um str mostrando o status completo do seu bichinho virtual

-------------------------
|    BichinhoVirtual    |
-------------------------

"""

print("\n\n\n CLASSE BICHINHO VIRTUAL \n\n\n")

class BichinhoVirtual:
	def __init__(self, nome, idade):
		self.__nome = nome
		self.__idade = idade
		self.__fome = 100
		self.__saude = 100

	def get_nome(self):
		return self.__nome

	def set_nome(self, novo_nome):
		self.__nome = novo_nome

	def get_idade(self):
		return self.__idade

	def set_idade(self, nova_idade):
		self.__idade = nova_idade

	def get_fome(self):
		return self.__fome

	def set_fome(self, nova_fome):
		self.__fome = nova_fome

	def get_saude(self):
		return self.__saude

	def set_saude(self, nova_saude):
		self.__saude = nova_saude

	def get_humor(self):
		if self.get_fome() >= 70 and self.get_saude() >= 70:
			return "Estou feliz!"

		elif self.get_fome() >= 50 and self.get_saude() >= 50:
			return "Não sou tão bom!"

		elif self.get_fome() >= 30 and self.get_saude() >= 30:
			return "Estou com muita raiva!"

		else:
			return "Estou tão fraco que não consigo responder!"

bichinho = BichinhoVirtual("Bolinha", 2)

print( bichinho.get_nome() )
print( bichinho.get_idade() )
print( bichinho.get_humor() )

bichinho.set_saude(30)
bichinho.set_fome(70)

print( bichinho.get_humor() )
