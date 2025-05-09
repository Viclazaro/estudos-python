#Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo


num1 = float(input('Digite um número: '))

if num1 > 0:
    print('O valor é positivo')
elif num1 < 0:
    print('O valor é negativo')
else: 
    print('O valor é zero')