"""
Leia uma temperatura em graus celsius, faça a conversão para
graus fahrenheit e exiba na tela.
"""

c = float(input('Digite uma temperatura em graus celsius [°C]: '))
f = c * (9.0 / 5.0) + 32

print(f'A temperatura de {c}°C convertida para fahrenheit é de {f:.1f}°F.')
