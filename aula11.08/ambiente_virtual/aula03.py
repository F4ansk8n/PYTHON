# Operadores IN e NOT IN
nome = "Francisco"
print ('is' in nome)

print('='*20)

seu_nome = input('Informe seu nome ')
buscar = input('informe o valor a ser encontrado: ')

if ( buscar in nome ):
    print(f'{ buscar } entá contido em { seu_nome }')
else:
    print(f'{ buscar } NÃO está contindo em { seu_nome }')

print('='*20)

nao_nome = "Joãozinho"
print('au' not in nao_nome)