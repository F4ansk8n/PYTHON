# criar um codigo que imprime todos os dias da semana na tela
# dias_semanas = ['domigo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
# for dia in dias_semanas:
#    print(dia)

# escreva um codigo que imprima os numeros de 1 até 1000 e avise quando chegar nos multiplos de 100
for n in range(1, 1001):
    if n % 100 == 0:
        print(f'{n} e multiplo de 100')
    else:
        print(n)