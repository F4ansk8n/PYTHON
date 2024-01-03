"""
Questão 08

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. peça três frutas para o usuario e calcule o total da compra dele
02. informe o qual fruta tem o menor valor
03. faça uma promoção e diminua o preco de duas frutas paara metade
04. insira duas novas frutas e seus preços

"""

frutas = ["abacaxi", "uva", "maçã", "abacate", "tangerina"]
precos = [3.50, 4.99, 6.49, 9.10, 4.99]

frutas_precos = {
    'abacaxi':3.50,
    'uva': 4.99,
    'maçã':6.49,
    'abacate':9.10,
    'tangerina': 4.99,
}

print(frutas_precos)

#fruta_1 = input('Qual fruta você quer comprar: ')
#fruta_2 = input('Qual fruta você quer comprar: ')
#fruta_3 = input('Qual fruta você quer comprar: ')

#if fruta_1 in frutas_precos and fruta_2 in frutas_precos and fruta_3 in frutas_precos:
#    total_compra = frutas_precos[fruta_1] + frutas_precos[fruta_2] + frutas_precos[fruta_3]
#print(f'O valor total da compra foi de:{total_compra}')

print()
menor_valor = min(frutas_precos)
print(f'A fruta com o menor valor é: {menor_valor}')

print()
# Tem que adcionar as duas promoção na lista
promocao_1 = precos[2] / 2
promocao_2 = precos[3] / 2
print(f'A promoção da {frutas[2]} é de 50 % o novo valor dela é {promocao_1:.2f}')
print(f'A promoção da {frutas[3]} é de 50 % o novo valor dela é {promocao_2:.2f}')

print()
print(frutas_precos)
frutas_precos['morango'] = 9.99
frutas_precos['alho'] = 13.99
print(frutas_precos)
