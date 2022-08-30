"""
Leia um valor de volume em litros e converta para metros cúbicos.
"""

l = int(input('Digite um volume em litros [ls]: '))
m = l / 1000

print(f'O volume de {l}ls convertido para metros cúbicos é {m:.1f}m³.')
