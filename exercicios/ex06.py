#Crie uma variável de atribua a ela o valor de uma hora inteira. O algoritmo deve processar a conversão 
#dessa hora em minutos e segundos e imprimir na tela essas conversões.

horas = int(input('Digite a hora:\n'))

minutos = horas * 60
segundos = horas * 3600

print(f'Minutos: {minutos}')
print(f'Segundos: {segundos}')
