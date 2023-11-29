# estruturas condicionais
variavel = 4
if variavel < 5:
    print('Menor que 5')
elif variavel == 10:
    print('Igual a 10')
elif variavel > 10 and variavel < 20:
    print('Esta no intervaalo entre 11 e 19')
else:
    print('Qualquer outra coisa')

# estruturas de repetiçao
#   "for" e "while"
for i in range(5):
    print(f'O printe do numero {i}')

print('*' * 20)

contador = 5
while contador > 0:
    print(f'Esse é o print do numer {contador}')
    contador -= 1

# join - unir strings
lista = ['Joao', 'Paulo', 'II']
nome = ' ' .join(lista)
print(nome)