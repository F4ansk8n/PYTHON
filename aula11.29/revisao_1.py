# variavel e um espaçao na memoria do computado que armazena um valor
variavel = 1
print(variavel)

variavel = 'Paulo'
print(variavel)

# regra do fatiamento [inicio, fim, step]
print(variavel[2:4])

# utllizando fatiamento e repetição imprima uma lista de "a" ate "e" removendo uma lentra de cada vez
lista = ['a','b','c','d','e']
for i in range(5):
    print(lista[:5-i], type(lista))