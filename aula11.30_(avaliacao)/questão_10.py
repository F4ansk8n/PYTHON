"""
Questão 10 

• Escreva uma função que calcule o fatorial de um numero e lembre de imprmir todos os resultados:

01. o numero  deve ser solicitado ao usaurio. ok

"""
def fatorial():
    numero = int(input('Digite um numero: '))
    resultado = 1

    for n in range(1,numero + 1):
        resultado *= n
    print(f'O fatorial de {numero}! é: {resultado}')

    return resultado
    
fatorial()