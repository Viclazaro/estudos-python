#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar 
#em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

num = int(input('Deseja ver qual tabuada? '))
start = int(input('Deseja começar em: '))
finish = int(input('A tabuada deve finalizar em: '))

if(start < finish):
    for i in range(start, finish+1):
        conta = num * i
        print(f'{num} x {i} = {conta}')
else:
    print('Valor inválido')