"""
Leia uma distância em milhas e apresente-a convertida em
quilômetros.
"""
m = int(input('Digite uma distância em milhas: '))
k = 1.61 * m

print(f'A distância de {m} milhas convertida para quilômetros é {k:.1f}')
