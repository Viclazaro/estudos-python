# Fazer um programa que lê um valor inteiro N e depois N números 
# inteiros. Ao final, mostra a soma dos N números lidos.

num = int(input('Quantos números serão digitados? ')) 
soma = 0

for n in range(0, num):
    x = int(input('Digite um numero: '))
    soma = soma + x
   
print('Soma: ', soma)