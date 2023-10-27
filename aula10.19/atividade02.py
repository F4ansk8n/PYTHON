# Receba a altura(h) de uma pessoa, crie um código que calcule seu peso ideal, utilizando as fórmulas abaixo:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 

sexo1 = "homem"
sexo2 = "mulher"
peso_homem = float
peso_mulher = float
input("informe seu sexo: (1)para homem e (2)para mulher ")
if sexo1 == "(1)para homem":
     altura_homem = float(input("Informe sua altura: "))
     peso_homem = (72.7 * altura_homem) - 58
     print("Seu peso ideal é ",peso_homem, "quilos")

elif sexo2:
     altura_mulher = float(input("Informe sua altura: "))
     peso_mulher = (62.1 * altura_mulher) - 44.7
     print("Seu peso ideal é ",peso_mulher, "quilos")
else:
     print("seu peso ideal é ",peso_mulher, "quilos")