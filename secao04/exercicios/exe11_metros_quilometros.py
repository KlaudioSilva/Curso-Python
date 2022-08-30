"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a
convertida para km/h (quilômetros por hora).
"""

m = int(input('Digite uma velocidade em metros por segundo [m/s]: '))
q = m * 3.6

print(f'A velocidade de {m}m/s convertida para quilômetros por hora é {q:.1f}')
