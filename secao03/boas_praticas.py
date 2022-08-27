"""
PEP8 - Python Enhancement Proporsal
São propostas de melhorias para a linguagem Python

O Zen de Python, de Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor do que complicado.
Plano é melhor do que aninhado.
Esparso é melhor do que denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que explicitamente silenciado.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Embora essa maneira possa não ser óbvia no início, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja melhor do que *agora*.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Namespaces são uma ótima ideia -- vamos fazer mais desses!
-------------------------------------------------------------------------------------

A ideia da PEP8 é que possamos escrever códigos Python de forma 'Pythonica'.
"""
# -----------------------------------------------------------------------------------
# [1] - Use Camel Case para nomes de classes:
# nomes de classes devem sempre iniciar com maiúsculas
class Calculadora:
    pass
# se o nome é formado por duas palavras, não use 'underline'. Escreva as inicias em maiúsculas.
class CalculadoraCientifica:
    pass

# -----------------------------------------------------------------------------------
# [2] - Use nomes em minúsculas, separadas por 'underlines' para funções ou variáveis:
def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

# -----------------------------------------------------------------------------------
# [3] - Use quatro espaços para identação!
if 'a' in 'banana':
    print('tem')  # identação com quatro espaços

# -----------------------------------------------------------------------------------
# [4] - Linhas em branco
# - Separar funções e definições de classe com duas linhas em branco.
# - Métodos dentro de uma classe devem ser separados com uma única linha em branco.

# -----------------------------------------------------------------------------------
# [5] - Imports
""" Imports deve ser sempre feitos em linhas separadas:

-> Certo:
import sys
import os

-> Errado:
import sys, os

-> Não há problemas em usar:
from types import StringType, ListType

-> Caso tenha muitos imports de um mesmo pacote, recomenda-se:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

-> Imports deve sem colocados no topo do arquivo, logo depois de quaisquer comentários
ou docstrings e antes de constantes ou variávies globais.
"""

# -----------------------------------------------------------------------------------
# [6] - Espaços em expressões e instruções:
""" 
-> Não faça:
funcao( algo[ 1 ], { outro: 2 } )

-> Faça:
funcao(algo[1], {outro: 2})

-> Não faça:
algo (1)

-> Faça:
algo(1)

-> Não faça:
dict ['chave'] = lista [indice]

-> Faça:
dict['chave'] = lista[indice]

-> Não faça:
x              = 1
y              = 2
variavel_longa = 5

-> Faça:
x = 1
y = 2
variavel_longa = 5
"""

# -----------------------------------------------------------------------------------
# [7] - Sempre termine uma instrução com uma nova linha.
# print('Hello World!')  -> ao finalizar a instrução, insira mais uma linha:
