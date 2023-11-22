# for -> trabalha com interaveis!!
#   tem que possuir uma variavel de controle
# metodos:
# > iter() -> transforma um objento em interavel
# > next() -> função par imprimir os iteraveis de uma "lista"

# nome = 'Paulo'      #
# texto = iter(nome)  # 
# print(texto)        # funcionamento do for atras dos "panos"
# print(next(texto))  # 
# print(next(texto))  # 

# print('='*20)

# for letra in nome:
#     print(letra)

# enumerate () -> é uma iterador de indices e valores
lista_nome = ['joão', 'pedro', 'mateus', 'judas', 'tiago']
lista_enumerada = enumerate(lista_nome)
print(lista_nome)
print(list(lista_enumerada))

for item in lista_enumerada:
    print(item)

for indice_lista, item_lista in enumerate(lista_nome):
    print(f'{item_lista} e o {indice_lista} da lista')