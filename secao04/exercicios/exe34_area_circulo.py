"""
Leia o comprimento do raio de um círculo, calcule e imprima a
área do círculo correspondente
"""

raio = int(input('Qual é o comprimento do raio desse círculo [cm]: '))
area =  3.14 * (raio ** 2)

print(f'A área de um círculo com um raio de {raio}cm é igual a {area:.2f}cm².')
print()
