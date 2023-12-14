"""
Questão 06 

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. crie uma nova lista só com os numeros pares. 
02. crie uma nova lista só com os numeros impares. 
03. crie uma nova lista só com os multiplos de 2. 
04. some todos os itens da "lista"  
05. informe quais valores se repetem 

"""

lista = [10,11,20,22,30,33,40,11,50,55,60,66,70,22,80,88,90,99]


lista_pares = []
for numer in lista:
    if numer % 2 == 0:
        lista_pares.append(numer)
print(f'Lista de numeros pares {lista_pares}')

print()
lista_impares = []
for numer in lista:
    if numer % 2 != 0:
        lista_impares.append(numer)
print(f'Lista de numeros impares {lista_impares}')

print()
lista_multiplos_2 = []
for numer in lista:
    if numer % 2 == 0:
        lista_multiplos_2.append(numer)
print(f'Lista de numeros multiplos de 2 {lista_multiplos_2}')

print()
soma = 0
for numer in range(len(lista)):
    soma += lista[numer]
#soma = sum(lista)
print(f'A soma de todos os itens da lista ficou no total de {soma}')

print()
repetem = set([numer for numer in lista if lista.count(numer) > 1])
print(f'Os numeros {repetem} se repetem')
