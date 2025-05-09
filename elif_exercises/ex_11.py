#Faça um programa que peça dois números e imprima o maior deles.

print('Digite dois números')
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))

if num1 > num2:
    print(f'O número {num1:.2f} é maior.')
elif num1 < num2:
    print(f'O número {num2:.2f} é maior.')
else: 
    print('Os números são iguais.')