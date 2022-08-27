"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'string', '234', 'K', 'True', '33.1'
- Estiver entre aspas duplas -> "string", "234", "K", "True", "33.1"
- Estiver entre aspas simples triplas -> '''string''', '''234''', '''K''', '''True''', '''33.1'''
"""
# Estiver entre aspas duplas triplas -> """string""", """234""", """K""", """True""", """33.1"""

from cgitb import text


nome = 'Klaudio Silva'
print(nome)
print(type(nome))

nome2 = "José"
print(nome2)
print(type(nome2))

nome3 = "Gina's Bar"
print(nome3)
print(type(nome3))

# Se eu precisar inserir uma quebra de linha, posso fazer:
# usando um -> \n
nome4 = 'Klaudio \nSilva'
print(nome4)
print(type(nome4))

# usando aspas duplas simples também é possível:
nome5 = """Klaudio
Silva"""
print(nome5)
print(type(nome5))

print(nome.lower())
print(nome.upper())

# usando um fatiamento de string, também chamado de split
print(nome.split())  # fatia a string e cria uma lista com as duas palavras da string:

print(nome.split()[1])  # vai exibir na tela apenas o 'Silva'
# no exemplo acima foi usado o indice da lista onde 0-> Klaudio e 1-> Silva

"""
Para fazer uma inversão da string podemos fazer:
: para dizer que é pra começar do primeiro elemento da string
: para dizer que é para ir até o final da string
-1 para dizer que é para ler do último para o primeiro
print(nome[::-1])
"""
print(nome[::-1])

# como o comando 'replace' podemos fazer subtituições na string:
print(nome.replace('K', 'C'))

# podemos fazer algumas brincadeiras com as palavras -> PALINDROMO
texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])
# um palindromo é uma frase ou palavra que pode ser lida da mesma 
# forma de trás para frente