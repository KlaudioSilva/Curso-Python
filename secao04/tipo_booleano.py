"""
Tipo Booleano
Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso
True -> verdadeiro
False -> falso

Obs: Sempre com a inicial em maiúscula.
Certo:
    False, True
Errado:
    false, true
"""
ativo = False
print(ativo)

"""
Operações básicas

-> Negação (not):
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
Se for falso o resultado será verdadeiro. Ou seja, sempre será o contrário.
>>> not True
False
>>> not False
True
"""
print(not ativo)
logado = False

"""
-> Ou (or):
É uma operação binária, ou seja, depende de dois valores. Um ou outro deve ser verdadeiro.
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
"""
print(ativo or logado)

"""
-> E (and):
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem
ser verdadeiros.
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False

>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
"""