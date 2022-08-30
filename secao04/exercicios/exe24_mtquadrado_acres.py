"""
Leia uma área em metros quadrados e faça a conversão para acres.
"""

a = int(input('Digite o tamanho de uma área em metros quadrados [m²]: '))
acre = a / 4047

print(f'A área de {a}m² convertida em acres é {acre:.5f}.')
