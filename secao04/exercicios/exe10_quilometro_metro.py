"""
Leia uma velocidade em km/h (quilômetro por hora) e apresente-a
convertida em m/s (metros por segundo).
"""

q = int(input('Digite uma velocidade em quilômetros por hora [km/h]: '))
m = q / 3.6

print(f'A velocidade de {q}km/h, convertida para metros por segundo é {m:.2f}m/s.')
