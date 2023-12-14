"""
Questão 07

• Crie uma função que gere uma lista com tuplas em seus elementos, nas tuplas devem conter dois valores nome e idade 

Ex.: [('paulo', 28), ('Jose', 23), ('Roberto', 17)] 

Ainda deve fazer:
• excluir o ultimo valor
• adicionar uma nova tupla no inicio da lista
• Crie uma cópia da lista para não utilizar o mesmo endereço de memoria

"""

def lista_tupla():
    lista_nomes = []
    lista_nomes = [('Kelly', 20), ('Raquely', 22), ('Rian', 18)]    
    lista_nomes.pop()
    print(lista_nomes)
    lista_nomes.insert(0,('Iris',19))
    print(lista_nomes)
    lista_1 = lista_nomes.copy()
    print(lista_1)

lista_tupla()