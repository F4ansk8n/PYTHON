# CRUD - created, readed, updated, deleted

# created
dic = {'Nome':'Paulo'}
dic2 = dict(idade = 23)

#readed
dic['Nome']
reading = dic2.get('Idade')

#updated
dic.update(Sobrenome =  'Junior')
dic.update({'idade': 23})

tupla = ('Peso', 72.12), # para fazer um updated de uma tupla precisa colocar uma virgula no final da tupla
dic.update(tupla)

lista = ['Data', '13/04/1996'],['Numero', [1,2,3,4,5]] # updaated de uma lista precisa de uma virgula no final e adicionar duas listas
dic.update(lista)

print(dic)
print(dic2)

#deleted
dic.clear()
print(f'dados do dicionario {dic}')