# for trabalha com iteraveis!!!
# tem que possuir uma variavel de controle
# iter()
# next()

# nome = 'Paulo'
# letra = iter(nome)
# print(next(letra))
# print(next(letra))
# print(next(letra))
# print(next(letra))
# print(next(letra))

# for letra in nome:
#     print(letra)

#enumerate() é um iterador de indices e valores

# lista_nomes = [ 'João', 'Pedro', 'Mateus', 'Judas', 'Tiago' ]

# lista_enumerada = enumerate(lista_nomes)

# print(lista_nomes)
# print(list(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

# for indice_lista, item_lista in enumerate(lista_nomes):
#     print(f'{ item_lista } é o { indice_lista } da lista')


# Crie um codigo que imprime todos os dias da semana na tela

dias_semana = [ 'domigo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado' ]

for dia in dias_semana:
    print(dia)

# escreva um codigo que imprima os numeros de 1 até 1000 e avise quando chegar nos multiplos de 100
for n in range(1, 1001):
    if n % 100 == 0:
        print(f'{n} e multiplo de 100')
    else:
        print(n)