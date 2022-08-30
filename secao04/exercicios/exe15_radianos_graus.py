"""
Leia um ângulo em radianos e converta para graus.
"""

r = float(input('Digite um ângulo em radianos: '))
g = (r * 180) / 3.14

print(f'O ângulo de {r} radianos convertido para graus é {g:.1f}')
