"""
Leia um valor de volume em metros cúbicos e converta para litros.
"""

m = int(input('Digite um valor de volume em metros cúbicos [m³]: '))
l = m * 1000

print(f'O volume de {m}m³ convertido para litros é {l:.1f}ls.')
