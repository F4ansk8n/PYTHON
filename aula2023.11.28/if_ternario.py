# tradicional
salario = float(input('Informe o valor do seu salario: '))

if salario >= 2500.00:
    print('IR será cobrado')
else:
    print('IR não será cobrado')

# condicao ternaria acontece em formato de linha
variavel_controle = 'IR será cobrado' if salario >= 2500.00 else 'IR não será cobrado'
print(variavel_controle)

print('*' * 20)

# condicao ternaria acontece em formato de linha com if, elif, else
vr_controle = 'OK 1' if True else 'OK 2' if True else 'Fim'
print(vr_controle)

if True:
    print('OK 1')
elif True:
    print('OK 2')
else:
    print('Fim')