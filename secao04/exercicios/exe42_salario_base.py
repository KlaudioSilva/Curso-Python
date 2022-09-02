"""
Receba o salário-base de um funcionário. Calcule e imprima
o salário a receber, sabendo-se que esse funcionário tem uma
gratificação de 5% sobre o salário-base. Além disso, ele paga
7% de imposto sobre o salário-base.
"""

sal_base = float(input('Qual é o salário-base do funcionário: R$'))
grat = (sal_base * 5) / 100
impost = (sal_base * 7) / 100

print(f'Já adicionado os 5% da gratificação e descontado os 7% do imposto')
print(f'o salário líquido a receber do funcionário é R${sal_base + grat - impost:.2f}')
print()
