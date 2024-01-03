# 1. faça um programa que peça 10 numeros interos, calcule e mostre a quantidade de numeros pares e a quantidade de numeros impares.
contador_par = 0
contador_impar = 0

for i in range(1, 11):
    numero = int(input(f'Informeo o {i}° numero: '))
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print(f'A quntidade de numeros pares é: {contador_par}')
print(f'A quntidade de numeros impares é: {contador_impar}')

# 2. faça um programa que, dado um conjunto de N numeros determine o menor valor, o maior valor é a soma dos valores.
maior = 0
menor = None

while True:
    saida = input('Digite "S" para sair: ')
    if saida == 's' or saida == 'S':
        print('Volte sempre!')
        break

    numero = int(input('Informe um numero inteiro: '))

    if numero > maior:
        maior = numero

    if menor == None or numero < menor:
        menor = numero

print(f'Soma de {maior} + {menor} = {maior+menor}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

# 3. faça um programa que peça um numero inteiro e determine se ele é ou não é primo. obs.: Um numero primo é aquele que é divisibel somente por ele mesmo e por 1.
numero = int(input('Informe um numero inteiro: '))
intervalo = range(1,numero + 1)
contador = 0

for i in intervalo:
    if numero % i == 0:
        print(f'foi divissivel por {i}')

if contador == 2 or contador == 1:
    print(f'O numero {numero} e primo')

# 4. faça um programa que peça para 10 pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 a 60 e maior que 60; e então, dizer se a turma é jovem ou adulta ou idosa, conforme a  média calculada
soma = 0

for i in range(10):
    idade = int(input('Digite sua idade: '))
    soma += idade

media = soma / 10

if media >= 0 and media <= 25:
    print("A turma é jovem.")
elif media >= 26 and media <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")

# 5. supondo que a população de um país A seja de 80000 habitantes com uma taxa anual de crescimento de 3% Faça um programa que calcule e escreva o número de anos necessários para que a população do país A chegar a 120000 habitantes.
atual = 80000
crescimento = 3
anos = 0 
alvo = 120000

while atual < alvo:
        atual *= 1 + 3 / 100
        anos += 1
        
print(f'Levou {anos} anos até atingir os 120000 habitantes. ')

# 6. o Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas em graus celsius, e informe ao final a menor e a maior temperaturas informadas.Para sair do programa deve digitar "SAIR"
maior = None
menor = None

while True:
    sair = input("Digir [SAIR] para sair do programa: ")
    if sair == "SAIR" or sair == "sair":
        print("Você saiu do programa com sucesso.")
        break
    
    temperatura = float(input('Digite a temperatura desejada: '))

    if maior == None or temperatura > maior:
        maior =  temperatura
    if menor == None or temperatura < menor:
        menor = temperatura

print(f'A menor temperatura é de {menor} graus celsius, a maior temperatura é de {maior} graus celsius.')