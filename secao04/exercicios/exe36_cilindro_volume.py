"""
Leia a altura e o raio de um cilindro circular e exiba o volume do cilindro.
"""

h = int(input('Digite a altura do cilindro [cm]: '))
r = int(input('Qual é tamanho do raio desse cilindro [cm]: '))
vol = 3.14 * (r ** 2) * h

print(f'O volume de um cilindo com {h}cm de altura e um raio de {r}cm é igual a {vol:.2f}.')
print()
