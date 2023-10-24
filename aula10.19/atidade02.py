# Receba a altura(h) de uma pessoa, crie um código que calcule seu peso ideal, utilizando as fórmulas abaixo:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 

sexo = input('Digite seu sexo: (1)Para homem (2)Para mulher: ') 
if sexo == 1:
     altura_homem = float(input('Digite sua altura: '))
     peso = float(72.7 * altura_homem)
     ideal = float (peso - 58)
else :
     altura_mulher = float(input('Digite sua altura: ')) 
     peso = float(62.1 * altura_mulher) 
     ideal = float(peso - 44.7)
print ('Seu peso ideal é ',ideal, "quilos")