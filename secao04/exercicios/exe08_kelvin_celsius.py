"""
Leia uma temperatura em graus kelvin, faça a conversão para
graus celsius e exiba na tela.
"""

k = float(input('Digite uma temperatura em graus kelvin [°K]: '))
c = k - 273.15

print(f'A temperatura de {k}°K, convertida para celsius é de {c:.1f}°C.')
