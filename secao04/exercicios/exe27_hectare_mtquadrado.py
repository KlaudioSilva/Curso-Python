"""
Leia uma área em hectares e converta para metros quadrados.
"""

ha = int(input('Digite o tamanho da área em hectares [ha]: '))
m = ha * 10000

print(f'A área de {ha}ha convertida para metros quadrados é {m:.1f}m².')
print()
