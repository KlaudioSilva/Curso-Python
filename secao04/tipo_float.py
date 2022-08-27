# Tipo Float
""" 
Também chamado de Tipo Real ou Decimal.
Casas decimais:
Obs: na programação, a separação das casas decimais é feita usando
o ponto e não a vírgula.
"""

# Errado para Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo para o Float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um Float para um Int
# fazendo essa conversão temos perda da precisão.
res = int(valor)
print(res)
print(type(res))

# exemplo de perda:
"""
>>> salario = 2.56
>>> salario2 = 3.67
>>> total = salario + salario2
>>> total
6.23
>>> total2 = int(salario) + int(salario2)
>>> total2
5.0

Tivemos uma perda de 1.23 no salario
"""

# Números complexos
# geralmente números complexos são representados pelo valor seguido da letra 'j'
"""
>>> 5j
5j
>>> type(5j)
<class 'complex'>
>>> variavel = 5j
>>> type(variavel)
<class 'complex'>
>>> variavel ** 2
(-25+0j)

"""