"""
Crie um programa que leia o valor de um produto e imprima
o valor com desconto, tendo em vista que o desconto foi de 12%.
"""

val = float(input('Qual é o valor desse produto: R$'))
desc = val - (val * 12) / 100

print(f'O valor final do produto, já com o desconto de 12% é de R${desc:.2f}')
print()
