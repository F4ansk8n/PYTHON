"""
Questão 04

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. crie uma função que faça a troca de caracteres de acordo com a escolha do usuario. Imprima em uma nova string.
02. utilizando um FOR troque os espaços em branco por -.

"""
texto = "Neste curso, os alunos(as) terão capacidades para trabalharem com toda a estrutura de dados que roda por trás de aplicações web. Compreendendo as necessidades de geração, captura e armazenamento de dados de uma aplicação web e a desenvolve, levando sempre em consideração a agilidade, segurança e confiabilidade nos dados que serão gerados e, por vezes, integrados a outros sistemas de gestão estratégica."


def troca(troca_caractere,novo_caractere):
    texto_modificado = texto.replace(troca_caractere, novo_caractere) 
    return texto_modificado

troca_caractere = input('Digite um caractere que deseja se trocado: ')
novo_caractere = input('Qual caractere quer usar para fazer a troca: ')

print()
resultado_da_troca = troca(troca_caractere, novo_caractere)
print(resultado_da_troca)

print()
for i in texto:
    texto = texto.replace(' ', '-')
print(texto)