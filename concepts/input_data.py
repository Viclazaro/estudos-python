# O input() permite que o usuário digite um valor e o armazena em uma variável

nome = input("Qual é o seu nome? ")  # Sempre retorna uma string (texto)

idade = input("Qual é a sua idade? ")  # Também retorna uma string, mesmo que o usuário digite um número + requer declaração de variavel

# Exibe o nome e a idade informados pelo usuário
print(nome, idade)  # O print() exibe os valores separados por um espaço

#estudos 2

input() # utilizado para entrada de dados
input("mensagem") # input reconhece dados como str

x = int(input("Digite um numero: ")) # caso eu queria receber um numero é necessario declarar o tipo de variavel
x = float(input("Digite um numero: ")) # outro exemplo

# exemplo 1

salario1: float; salario2: float  # Define que salario1 e salario2 são do tipo float
nome1: str; nome2: str  # Define que nome1 e nome2 são do tipo string
idade: int  # Define que idade é do tipo inteiro
sexo: str  # Define que sexo é do tipo string

# Coleta as entradas do usuário
nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input("Salario da primeira pessoa: "))
nome2 = input("Nome da segunda pessoa: ")
salario2 = float(input("Salario da segunda pessoa: "))
idade = int(input("Digite uma idade: "))
sexo = input("Digite um sexo (F/M): ")

# Imprime as informações coletadas com formatação
print(f"Nome 1: {nome1}")
print(f"Salario 1: {salario1:.2f}")
print(f"Nome 2: {nome2}")
print(f"Salario 2: {salario2:.2f}")
print(f"Idade: {idade}")

