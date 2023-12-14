"""
Questão 02

• Escreva um programa que, recebe uma palavra e uma frase, crie uma função que verifique se as letras da palavra aparecem na frase, e quantas vezes aparecem. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: você deve validar se a frase tem pelo menos 25 caracteres

Exemplos do resultado:
    palavra = "pato" 
    frase = "a capa do livro velho"
    P aparece 1 vez
    A aparece 3 vezes
    T não aparece
    O aparece três vezes
"""


def validacao(palavra, frase):
    if len(palavra) < 3: 
        print("ERRO!!! A palavra precisa ter 3 ou mais letras.") 
        return
        
    if len(frase) < 25:
        print("ERRO!!! A frase precisa ter 25 ou mais caracteres.")
        return
        
    for letra in palavra: 
        if letra in palavra and letra in frase: 
            indice_frase = frase.count(letra) 
            print(f'A {letra} aparece {indice_frase} vezes')
        else:
            print(f'A {letra} não aparece')

palavra = input('Digite uma palavra: ').lower() 
frase = input('Digite uma frase: ').lower()

validacao(palavra, frase)