#estudos 1 - Exibindo texto na tela
print('Exercicios 1') # O argumento 'end' impede a quebra de linha no final do print
print('Bom dia', end='') # "end=''" faz com que o próximo print continue na mesma linha
print(' Boa Noite')  # Será impresso na mesma linha do "Bom dia"
print(' ') # Apenas imprime um espaço em branco

#estudos 2 - Formatando saída com %s e %d
print('Exercicios 2')
x = 'Vic' # string
y = 19 # Inteiro

# Uso do %s (para strings) e %d (para inteiros) na formatação de saída
print('%s tem %d anos' % (x,y))  # Esse método é um estilo antigo de formatação
print(' ')

#estudos 3 - Imprimindo variáveis inteiras
print('Exercicios 3')

x: int; y: int # Indica que x e y devem ser um números inteiros
x = 10 # Atribuindo um valor inteiro a x
y = 20 # Atribuindo um valor inteiro a y

print(x) # Exibe o valor de x
print(y) # Exibe o valor de y
print(' ')

#estudos 4 - Formatando números decimais (float)
print('Exercicios 4')

x: float # Número decimal (float)
x = 3.155125 # Atribuindo valor

# "{:.2f}".format(x) exibe o número com 2 casas decimais
print("{:.2f}".format(x)) # Saída: 3.16 (arredondado)
print(' ')

#estudos 5 - Usando f-strings e format() para formatar saída
idade: int    # Variável do tipo inteiro
salario: float  # Variável do tipo float (número com casas decimais)
nome: str    # Variável do tipo string (texto)
sexo: str    # Variável do tipo string

# Atribuindo valores às variáveis
idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

# f-string: uma forma moderna de formatar strings
print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")

# Método format(): outra maneira de formatar saída
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))
