# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = 0

inicio = min(num1, num2) #menor valor
fim = max(num1, num2) #maior valor

for i in range(inicio+1, fim):
    print('Numero no intervalo: ', i)
    soma += i #acumular valores

print('Soma dos números no intervalo:', soma)