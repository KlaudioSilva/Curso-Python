"""
Escopo de Variáveis.
O que é escopo de variáveis?
Escopo é a propriedade que determina onde uma variável pode
ser utilizada como um identificador em um programa.

1º Variáveis Globais:
São reconhecidas, ou seja, seu escopo compreende, todo o prorama.

2º Variáveis Locais:
São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
está limitado ao bloco onde foi declarada ex:
Uma variável declarada em uma função é do tipo local.

Em Python, para declarar variáveis fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declarar
uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma:

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

Exemplo em Python:
numero = 42
"""

numero = 42  # Este é um exemplo de variável global
print(numero)
print(type(numero))

numero2 = 'Geek'
print(numero2)
print(type(numero2))

nao_existo = 'Oi'
print(nao_existo)

numero = 51
if numero > 10:
    novo = numero + 10  # Este é um exemplo de variável local
    print(novo)

# print(novo)
