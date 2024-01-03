# 1. Crie uma lista de alunos com nomes e nota final de cada aluno e coloque em um dicionario, depois imprima
lista_de_alunos = ['pedro',6],['tiago', 7]
dic = {}
dic.update(lista_de_alunos)
print(dic)

# 2. ainda sobre a questão 1. inserir mais 4 alunos e notas no seu dicionario
dic.update({'jose': 4})
dic.update({'joao': 3})
dic.update({'maria': 7})
dic.update({'lucia': 7})
print(dic)

# 3. faça um codigo que pede a marca e o modelo do cliente insere ele em uma lista e depois transforma em um dicionario
marca = input('informe a MARCA do seu carro: ')
modelo = input('indorme o MODELO do seu carro: ')

lista_de_carros = []
lista_de_carros.append(marca)
lista_de_carros.append(modelo)

dic_carros= {}
dic_carros.update([lista_de_carros])

print(lista_de_carros)
print(dic_carros)

# 4. crie um cadastro de clietes recebendos nome, idade, data de aniversario e endereço complento (rua, numero de residencia e bairro). Adicionr todos as informacoes em um dicionario. Imprima ao final
nome = input('qual o seu nome: ')
idade = int(input('Informe sua idade: '))
data_aniverario = input('Informe sua data de aniversario DIA/MÊS/ANO: ')
endereco_rua = input('Informe sua rua: ')
endereco_num = input('Informe o seu numero de endereço: ')
endereco_bairro = input('Informe o seu bairro: ')

cadastro = {
    'nome':nome,
    'idade':idade,
    'Data de Aniversario':data_aniverario,
    'Rua':endereco_rua,
    'Número': endereco_num,
    'Bairro':endereco_bairro,
}

print(cadastro)

# 5. Vamos criar um sistemas de login e senhas. Crie um dicionario contendo os acessos dos colaboradosres com nome de usuario e senha. Em seguinda peça as informações e valide o login do usuario.
dic_acesso = {
    'paulo':'1234',
    'joão':'3222',
}

usuario_senha = {}
usuario = input('informe o nome de USUARIO: ')
senha = input('informe sua SENHA: ')

usuario_senha[usuario] = senha

for chave in dic_acesso.keys():
    if chave == usuario:
        if dic_acesso[chave] == senha:
            print('acesso liberado!')
            break
        else:
            print(f'senha icorrenta para o usuario {usuario}')
            break
else:
    print(f'o usuario {usuario} incorrento!')

# 6. faca um quiz utilizado um dicionario com as seguintes chaves: pergunta, opcoes e resposta. Faça a validação da opção escolhida com a resposta e imprima.
perguntas =[
    {'Pergunta': 'Quanto é 5 x 5?',
     'Opções': [12, 16, 20, 25],
     'Resposta': 25,},

    {'Pergunta': 'Quanto é 12 / 4?',
     'Opções': [6, 13, 3, 2],
     'Resposta': 3,},

    {'Pergunta': 'Quanto é 15 + 15?',
     'Opções': [14, 15, 30, 25],
     'Resposta': 30,},
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})', opcao)
    print()

    escolha = int(input('Escolha sua opção: '))
    acertou = False

    if escolha == int(pergunta['Resposta']):
        acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou 😔')

    print()

print(f'Você acertou { qtd_acertos } de { len(perguntas) }')