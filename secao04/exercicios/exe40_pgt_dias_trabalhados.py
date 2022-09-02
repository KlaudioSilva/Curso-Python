"""
Uma empresa contrata um encanador a R$30,00 por dia. Faça um
programa que solicite o número de dias trabalhados pelo encanador
e exiba a quantia líquida que deverá ser paga, sabendo-se que
são descontados 8% para imposto de renda.
"""
dias = int(input('Quantos dias o encanador trabalhou neste mês: '))
tot = dias * 30
liq = tot - (tot * 8) / 100

print(f'Tendo trabalhado por {dias}, o valor bruto é de R${tot:.2f},\nmas com o desconto do imposto de 8%, o valor líquido é R${liq:.2f}')
print()
