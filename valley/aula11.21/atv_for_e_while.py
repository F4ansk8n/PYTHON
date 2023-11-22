# 1) faça um programa que peça 10 numeros interos, calcule e mostre a quantidade de numeros pares e a quantidade de numeros impares.
#contador_par = 0
#contador_impar = 0

#for i in range(1, 11):
#    numero = int(input(f'Informeo o {i}° numero: '))
#    if numero % 2 == 0:
#        contador_par += 1
#    else:
#        contador_impar += 1

#print(f'A quntidade de numeros pares é: {contador_par}')
#print(f'A quntidade de numeros impares é: {contador_impar}')

# 2) faça um programa que, dado um conjunto de N numeros determine o menor valor, o maior valor é a soma dos valores.
#maior = 0
#menor = None

#while True:
#    saida = input('Digite "S" para sair: ')
#    if saida == 's' or saida == 'S':
#        print('Volte sempre!')
#        break

#    numero = int(input('Informe um numero inteiro: '))

#    if numero > maior:
#        maior = numero

#    if menor == None or numero < menor:
#        menor = numero

#print(f'Soma de {maior} + {menor} = {maior+menor}')
#print(f'O maior valor é: {maior}')
#print(f'O menor valor é: {menor}')

# 3) faça um programa que peça um numero inteiro e determine se ele é ou não é primo. obs.: Um numero primo é aquele que é divisibel somente por ele mesmo e por 1.
#numero = int(input('Informe um numero inteiro: '))
#intervalo = range(1,numero + 1)
#contador = 0

#for i in intervalo:
#    if numero % i == 0:
#        print(f'foi divissivel por {i}')

#if contador == 2 or contador == 1:
#    print(f'O numero {numero} e primo')