"""
Leia um temperatura em graus fahrenheit, faça a conversão para
graus celsius e exiba na tela.
"""

f = float(input('Digite a temperatura em graus fahrenheit [°F]: '))
c = 5.0 * (f - 32) / 9

print(f'A temperatura de {f}°F, convertida para celsius é de {c:.1f}°C.')
