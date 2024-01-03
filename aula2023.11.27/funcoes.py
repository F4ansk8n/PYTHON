# funções são blocos de codigos que são executados somente quandos são chamados
# paramentro: def
# as funçOes devem ter prioridade no codigo

def media(nota1, nota2, nota3):
    media=(nota1 + nota2 + nota3) /3
    return media

nota01 = int(input('Informe a primeira nota: '))
nota02 = int(input('Informe a segunda nota: '))
nota03 = int(input('Informe a terçeira nota: '))

print(media(nota01, nota02, nota03))


print('*' * 20)


def calcula_horas_extras(quantidade_horas, valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_recebe = (horas - 40) * taxa

    return valor_recebe

quantidade_horas = float(input('Ifnforme o total de horas trabalhadas: '))
valor_da_hora = float(input('Informe o valor da taxa do colaborador: '))

print(calcula_horas_extras(quantidade_horas, valor_da_hora))

print('*' * 20)

salario = 1400.00
print(salario + calcula_horas_extras(quantidade_horas, valor_da_hora))

print('*' * 20)

# 1. faça um progama, com um função que necessita de um argumento. A função retorna o valor de caracterere "P", se seu argumento for positivo, e "N", se seu argumento for zero ou negativo.
def valor_argumento(n):
    if n > 0:
        valor = "P"
    else:
        valor = "N"
    return valor

numero = int(input('Digite um numero inteiro aleatorio: '))
print(valor_argumento(numero))