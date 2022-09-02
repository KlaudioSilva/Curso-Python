"""
Leia o salário de um funcionário. Calcule e exiba o valor do
novo salário, depois que ele recebeu um aumento de 25%.
"""

sal_atual = float(input('Qual é o seu salário atual R$'))
aumento = (sal_atual * 25) / 100

print(f'Após um aumento de 25% o seu salário passa a ser de R${sal_atual + aumento:.2f}')
print()
