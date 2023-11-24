# faça um codigo que peça uma nota, entre 0 e 10. Mostre uma mensagem caso a nota seja invalida e continue pedindo até que o usuario informe uma nota valida.
while True:
    nota = int(input('Informe sua nota: '))
    if nota > 0 and nota > 10:
        print(f'Nota {nota} é invalida')
    if nota < 0 and nota < 10:
        print(f'Nota {nota} é invalida')

# faça uma codigo que leia um nome de usuário é a sua senha e não aceite a senha igual ao nome do usuario, mostrando uma mensagem de erro e pedindo as informaçoes novamente.
while True:
    usuario = input('Informe seu nome: ')
    senha = input('DIgite sua senha: ')
    if usuario == senha:
        print('ERRO, senha igual ao nome. TENTE NOVAMENTE')
    else:
        print('Entrou com sucesso')
    break

# faça um codigo que leia 5 numeros e informe o maior numero
contador = 1
numero = 0
while contador <= 5:
    numero = input('Informe um numero: ')