# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

digito = int(input('Escreva um número:\n'))

if digito == 1:
    print('Domingo')
elif digito == 2:
    print('Segunda')
elif digito == 3:
    print('Terça')
elif digito == 4:
    print('Quarta')
elif digito == 5:
    print('Quinta')
elif digito == 6:
    print('Sexta')
elif digito == 7:
    print('Sábado')
else:
    print('Inválido')
