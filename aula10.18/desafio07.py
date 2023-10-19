# Faça um progama que peça 3 numeros inteiro e calcule:
# -> o produto do dobro do primeiro com a metade do segundo somado com o terceiro
# -> a soma do triplo do primeiro com o terceiro e multiplicado pelo o segundo

n1 = int(input('1º número inteiro: '))
n2 = int(input('2º número inteiro: '))
n3 = int(input('3º número inteiro: '))
print ('resultado:',int(2*n1) * int(n2/2) + n3)
print ('resultado:',(3*n1) + n3 * n2)