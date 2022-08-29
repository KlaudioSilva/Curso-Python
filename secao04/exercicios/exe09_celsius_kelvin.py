"""
Leia uma temperatura em graus celsius, faça a conversão
para graus kelvin e exiba na tela.
"""

c = float(input('Digite uma temperatura em graus celsius [°C]: '))
k = c + 273.15

print(f'A temperatura de {c}°C, convertida para kelvin é de {k:.1f}°K.')
