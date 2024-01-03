"""
Questão 03 

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. imprima quantas vezes aparece a letra "a" no "texto".
02. imprima qual a posição do primeiro "z".
03. leve o "texto" para uma nova variavel e trocando "aprendizado compartilhado" por "vivencia profissional".

"""
texto = "Somos uma escola de tecnologia de informação que cria pontes entre pessoas, conhecimento e empresas. Ambiente que proporciona conexão, troca de conhecimentos e aprendizado compartilhado entre participantes, instrutores e empresas parceiras."

print(f'A letra "a" aparece {texto.count("a")} vezes no texto')

print()
print(f'A letra "z" aparece no indece {texto.find("z")}')

print()
print(texto)

print()
nova_frase = texto.replace("aprendizado compartilhado", "vivencia profissional")
print(nova_frase)