"""
Leia um valor de comprimento em polegadas e converta para centímetros.
"""

p = int(input('Digite um comprimento em polegadas [in]: '))
c = p * 2.54

print(f'O comprimento de {p}in convertido para centímetros é {c:.1f}cm.')
