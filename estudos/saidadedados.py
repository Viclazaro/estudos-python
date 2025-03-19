#estudos 1
print('Exercicios 1')
print('Bom dia', end='') #sem quebra de linha 
print(' Boa Noite')
print(' ')

#estudos 2
print('Exercicios 2')
x = 'Vic'
y = 19

print('%s tem %d anos' % (x,y))
print(' ')

#estudos 3
print('Exercicios 3')
x: int; y: int
x = 10 
y = 20
print(x)
print(y)
print(' ')

#estudos 4
print('Exercicios 4')
x: int
x = 3.155125
print("{:.2f}".format(x)) 
print(' ')

#estudos 5
idade: int
salario: float
nome: str
sexo: str
idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))
