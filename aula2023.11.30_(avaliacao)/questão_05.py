"""
Questão 05

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. monte um conjunto(SET) com o nome "meu_conjunto1", nele você deve colocar os indices impares da "minha_lista"
02. transforme a "minha_lista" em uma string separada por /
03. monte uma lista iversa da "minha_lista"
04. informe quanntos elementos estão contidos em "minha_lista" e quantos estão contidos em "meu_conjunto"

"""

minha_lista = ["com", "um", "notebook", "e", "internet", "de", "banda", "larga", "qualquer", "jovem", "capacitado", "poderá", "trabalhar", "ou", "empreender", "do", "Ceará", "para", "o", "Brasil", "e", "o", "mundo", "e", "consequentemente", "transformando", "a", "sua", "vida", "e", "aquecendo", "a", "economia", "local"]


meu_conjunto1 = minha_lista[1::2]
print(meu_conjunto1)

print()
minha_lista = '/'.join(minha_lista)
print(minha_lista)

print()
lista_inversa = minha_lista[::-1] 
print(lista_inversa)

print()
print(len(set(minha_lista)))

print()
print(len(set(meu_conjunto1)))