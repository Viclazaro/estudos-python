#Um motorista deseja colocar no seu tanque X reais de gasolina. Crie uma variável que guarde o preço 
#do litro da gasolina e o valor que o motorista possui para colocar a gasolina. Imprima quantos litros de 
#gasolina o motorista conseguiu colocar no tanque.

#declarando variaveis
valor_litro = float(input('Digite o valor da gasolina:\n'))
valor_motorista = float(input('Digite o valor disponível\n'))

#calculando quantidade de litros
litros = valor_motorista / valor_litro

#exibindo resultado
print(f'Poderá colocar {litros:.2}L no tanque.')

