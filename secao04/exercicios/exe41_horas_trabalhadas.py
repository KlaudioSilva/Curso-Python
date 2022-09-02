"""
Faça um programa que leia o valor da hora de trabalho (em reais) e
o número de horas trabalhadas no mês. Imprima o valor a ser pagao
ao funcionário, adicionando 10% sobre o valor calculado.
"""
val_hora = float(input('Diga o valor da hora trabalhada: R$'))
tot_hora = int(input('Quantas horas foram trabalhadas neste mês: '))
bruto = val_hora * tot_hora
liquido = bruto + (bruto * 10) / 100
print()

print('~' * 65)
print(f'Num mês com {tot_hora} horas trabalhadas o pintor vai receber R${liquido:.2f}')
print()
