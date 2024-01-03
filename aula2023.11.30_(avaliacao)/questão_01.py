"""
Questão 01

• Escreva um programa que, recebe uma palavra, crie uma função que verifica na lista "alfabeto" a que indice pertence cada letra da palavra. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: letras repetidas devem ser verificadas somente uma vez

Exemplos do resultado:
    palavra = "cidade" 
    C está no indice 2
    I está no indice 8
    D está no indice 3
    A está no indice 0
    E está no indice 4
"""

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z' ]


def indece(palavra, alfabeto):
    if len(palavra) < 3:
        print('ERRO!!! A palavra precisa ter 3 ou mais letras')

    else:
        for i in set(palavra):
            if i and alfabeto:
                indece = alfabeto.index(i)
                print(f'A letra "{i}" esta no indece "{indece}"')
    return

palavra = input('Digite alguma palavra: ').lower()

indece(palavra, alfabeto)