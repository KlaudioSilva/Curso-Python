"""
Leia um valor em real e a cotação do dolar. Em seguida,
exiba o valor correspondente em dólares.
"""
print('Dolar hoje: R$5.16')
real = float(input('Digite um valor em reais para a fazermos a cotação: R$'))
dolar = real / 5.16

print(f'O valor de R${real} pode comprar na cotação atual U${dolar:.2f}')
print()
