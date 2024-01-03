"""
Questão 08 

• Escreva uma função que calcule o tempo de viagem de uma pessoa lembre de imprimir todos os resultados:

01. peça a distancia e a velocidade media ok
02. a formula é: distância / velocidade média(hora) ok
03. não esqueça de limitar a respota em apenas duas casas decimais ok

"""
def tempo_viagem():
    distancia = float(input('Digite a distância: '))
    velocidade_media = float(input('Digite a velocidade: '))
    
    tempo = distancia / velocidade_media
    
    print('Distância: %.2f km'% (distancia))
    print('Velocidade média: %.2f km/h'% (velocidade_media))
    print('O tempo de viagem foi %.2f horas'% (tempo))

tempo_viagem()