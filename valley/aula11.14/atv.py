# 1. faça um código que cria uma lista de 5 números inteiros imprime a lista , remove o numero do meio e imprime a lista atualizada.
lista= [1,2,3,4,5]
print(lista)
del lista[2]
print(lista)

# 2. faça um código que cria uma lista de 10 números reais e imprima só os pares e depois só os impares
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[0::2])
print(lista[1::2])

# 3. faça um código que pede 3 notas de quatro alunos, calcula a media e printa as medias em uma lista.
nota1 = float(input('Digite a sua nota:'))
nota2 = float(input('Digite a sua nota:'))
nota3 = float(input('Digite a sua nota:'))

nota4 = float(input('Digite a sua nota:'))
nota5 = float(input('Digite a sua nota:'))
nota6 = float(input('Digite a sua nota:'))

nota7 = float(input('Digite a sua nota:'))
nota8 = float(input('Digite a sua nota:'))
nota9 = float(input('Digite a sua nota:'))

nota10 = float(input('Digite a sua nota:'))
nota11 = float(input('Digite a sua nota:'))
nota12 = float(input('Digite a sua nota:'))

media1 = (nota1 + nota2 + nota3) /3
media2 = (nota4 + nota5 + nota6) /3
media3 = (nota7 + nota8 + nota9) /3
media4 = (nota10 + nota11 + nota12) /3
lista_nota = [media1, media2, media3, media4]
print(lista_nota)

# 4. faça um código que pede 5 letras e quando for consoante ele avisa "É uma consoante", imprima uma lista com as consolantes encontradas
l1 = str(input('digite uma letra: '))
l2 = str(input('digite uma letra: '))
l3 = str(input('digite uma letra: '))
l4 = str(input('digite uma letra: '))
l5 = str(input('digite uma letra: '))
lista_consoante = []
if l1 != 'a' and l1 != 'e' and l1 != 'i' and l1 != 'o' and l1 != 'u':
    print('É uma consoante')
    lista_consoante = [l1]
if l2 != 'a' and l2 != 'e' and l2 != 'i' and l2 != 'o' and l2 != 'u':
    print('É uma consoante')
    lista_consoante.append(l2)
if l3 != 'a' and l3 != 'e' and l3 != 'i' and l3 != 'o' and l3 != 'u':
    print('É uma consoante')
    lista_consoante.append(l3)
if l4 != 'a' and l4 != 'e' and l4 != 'i' and l4 != 'o' and l4 != 'u':
    print('É uma consoante')
    lista_consoante.append(l4)
if l5 != 'a' and l5 != 'e' and l5 != 'i' and l5 != 'o' and l5 != 'u':
    print('É uma consoante')
    lista_consoante.append(l5)
print(lista_consoante)

# 5. faça um código que crie uma lista com 20 números inteiros e armazene os números pares na lista pares e os números impares na lista impar, imprima as duas listas.
lista_numerico = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_impares = []
lista_pares = []
lista_impares=(lista_numerico[0::2])
lista_pares=(lista_numerico[1::2])
print(lista_impares)
print(lista_pares)