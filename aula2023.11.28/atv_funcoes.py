# 1. Faça uma função que retorne o reverso de um numero inteiro informado. Por exemplo: 127 -> 721
def numero_reverso(numero):
    reverso = 0

    while numero > 0:
        # pegar o ultimo valor do numero
        ultimo_valor = numero % 10
         
         # add ultimo valor
        reverso = (reverso * 10) + ultimo_valor

        # tira o ultimo numero
        numero = numero // 10
    # retona o reveeso
    return reverso

numero = int(input('Digite um numero: '))
resultado = numero_reverso(numero)
print(f'O numero informado foi {numero} e o reverso dele é {resultado}')

print('*' * 20)

def numero_reverso(numero):
    reverso = numero[::-1]
    return int(reverso)

numero = input('Digite um numero: ')
print(f'O numero informado foi {numero} e o reverso dele é {numero_reverso(numero)}')

# 2. Faça um função que informe a quantidade de digitos de um detrminado numero interio.
def quantidade_digitos(numero):
    digitos = len(numero)
    return digitos

numero = input('Informe um numero: ')
resultado = quantidade_digitos(numero)
print(f'O numero {numero} e a quantidade de digitos foi de {resultado}')

# 3. Escreva uma funçao chamada gorjeta, que recebe o valor de conta de um restaurante, calcule e exiba a gorjeta do garçom, considerabdo 12% do valor da conta.