# Faça um programa que receba dois números inteiros e gere 
# os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

inicio = min(num1, num2) #menor valor
fim = max(num1, num2) #maior valor

for i in range(inicio+1, fim):
    print('Numero no intervalo: ', i)

    