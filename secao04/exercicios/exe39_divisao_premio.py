"""
A importância de R$780.000,00 será dividida entre três ganhadores
de um concurso. Sendo que da quantia total:
→ O primeiro ganhador receberá 46%;
→ O segundo ganhador receberá 32%;
→ O terceiro ganhador receberá o restante;
Calcule e exiba a quantia ganha por cada um dos ganhadores.
"""

print('\033[31m-\033[m' * 25)
print('DIVIDINDO O PRÊMIO'.center(25))
print('\033[31m-\033[m' * 25)
print()

print('Vamos dividir um prêmio de R$780 mil entre 3 ganhadores:')
print(f'O primeiro ganhador vai receber 46% do prêmio: R${(780000 * 46) / 100:.2f}')
print(f'O segundo ganhador vai receber 32% do prêmio: R${(780000 * 32) / 100:.2f}')
print(f'O terceiro ganhador vai receber o valor restante: R${(780000 * 22) / 100:.2f}')
print()
