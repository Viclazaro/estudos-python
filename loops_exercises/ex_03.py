# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

x = int(input('Digite uma nota entre zero e dez: '))
    

while (x < 0) or (x > 10):
    print('Invalido')
    x = int(input('Digite novamente um valor válido: '))

print('Valor válido!')
