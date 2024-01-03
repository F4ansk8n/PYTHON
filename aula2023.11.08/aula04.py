# Outra forma de INTERPOLAR

nome = 'Francisco'
salario = 1320

print(nome,"ganha um salário de R$",salario)
print(f'O salário de {nome} é R$ {salario}')

# forma FORMAT de imprimir
    # s - string
    # d e t - int
    # f - float
    # x e X - hexadecimais
print('Salario de %s e de R$ %.2f' % (nome, salario))
print('Quem ganha um salário de R$ %.2f é o %s' % (salario, nome))