"""
Crie um programa que receba os valores 'a' e 'b' e calcule
o valor da hipotenusa.
"""

cat_a = int(input('Digite o comprimento do cateto Maior: '))
cat_b = int(input('Digite o comprimento do cateto Menor: '))

# x recebe a soma dos quadrados dos catetos
x = (cat_a ** 2) + (cat_b ** 2)

# formula para descobrir a raiz quadrada
hip = x ** (1/2)

print(f'A hipotenusa dos catetos {cat_a} e {cat_b} é {hip}.')
print()
