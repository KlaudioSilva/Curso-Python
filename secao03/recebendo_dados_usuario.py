""" Recebendo dados do usuário
ATENÇÃO: tudo que é recebido via 'input' é do tipo string
Strings são dados que estão entre aspas simples, aspas duplas
aspas simples triplas, aspas duplas triplas...
exemplos:
Aspas simples - 'José'
Aspas duplas - "José"
Aspas simples triplas - '''José'''
"""

# entrada de dados, na antiga versão 2x do Python
print('Qual é o seu nome: ')
nome = input()
print('Qual a sua idade: ')
idade = input()

# saída no terminal, na antiga versão 2x do Python
print('Seja bem-vindo(a) %s' %nome)
print('%s tem %s anos' %(nome, idade))

#---------------------------------------------------------------
# entrada de dados, usando 'format' do Python 3x
nome2 = input('Qual é o seu nome: ')
idade2 = input('Qual é a sua idade: ')

# saída
print('Seja bem-vindo(a) {0}'.format(nome2))
print('{0} tem {1} anos'.format(nome2, idade2))

#---------------------------------------------------------------
# entrada de dados, a partir da versão 3.7 do Python, podemos fazer assim:
nome3 = input('Qual é o seu nome: ')
idade3 = input('Qual é a usa idade: ')

# saída
print(f'Seja bem-vindo(a) {nome3}')
print(f'{nome3} tem {idade3} anos.')

# fazendo um cast:
# Cast é a 'conversão' de um tipo de dado para outro.
print(f'{nome3} nasceu em {2022 - int(idade)}')

# definindo o tipo de dado no input
idade4 = int(input('Qual é a sua idade: '))
print(f'{nome3} nasceu em {2022 - idade4}')
