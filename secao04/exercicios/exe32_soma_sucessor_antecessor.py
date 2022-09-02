"""
Leia um número inteiro e imprima a soma do sucessor de
seu triplo com o antecessor de seu dobro.
"""

num = int(input('Digite um número inteiro qualquer: '))
suc = (num * 3) + 1
ant = (num * 2) - 1

print(f'O sucessor do triplo de {num} é {suc}.')
print(f'O antecessor do dobro de {num} é {ant}.')
print(f'A soma entre {suc} e {ant} é igual a {suc + ant}.')
