# Tipo Numérico:
"""
>>> 44
44

-> a variavel num recebe o valor 42:
>>> num = 42
>>> num
42
>>> print(num)
42
>>> 5 + 4
9
>>> 7 - 2
5

-> realizando operações com variáveis
>>> a = 3
>>> b = 5
>>> c = a + b
>>> c
8
>>> print(c)
8

>>> 3 * 5
15

>>> 5 / 2
2.5

-> divisão inteira
>>> int(5 / 2)
2
>>> 5 // 2
2

-> resto da divisão
>>> 4 % 2
0
>>> 5 % 2
1

-> exponenciação
>>> 3 ** 3
27
>>> 2 ** 8
256

-> Podemos usar a função 'type' para saber qual é o tipo do dado
>>> num = 34
>>> type(num) -> tipo inteiro
<class 'int'>
>>> num2 = 34.5
>>> type(num2)
<class 'float'> -> tipo flutuante
>>> num3 = '34'
>>> type(num3)
<class 'str'> -> tipo texto
>>> num4 = True
>>> type(num4)
<class 'bool'> -> tipo booleano

"""

# OBS: ao trabalhar com números muito grandes pode-se usar '_' para facilitar a leitura:
num = 1_000_000_000
print(num)