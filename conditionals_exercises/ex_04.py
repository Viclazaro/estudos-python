# Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

num1 = int(input('Digite um numero:\n'))
num2 = int(input('Digite outro numero:\n'))


num0 = num1
num1 = num2
num2 = num0
print('Invertendo...')

print(num1, num2)