nome = "Victoria"  # String (texto)
idade = 19       # Inteiro (int)
altura = 1.71    # Float (número decimal)
tem_pet = True   # Booleano (True ou False)

print(nome, idade, altura, tem_pet)

#continuação

# Definição de tipos de variáveis (anotação de tipo, não obrigatória)
idade: int  # Apenas números inteiros
salario: float  # Números com casas decimais (ponto flutuante)
altura: float  # Aceita números com decimais
genero: str  # Representa um caractere ou texto
nome: str  # Conjunto de caracteres que formam um texto

# Atribuição de valores às variáveis
idade = 20  # Número inteiro
salario = 1200  # Número decimal (float, mas sem casas decimais visíveis)
altura = 1.71  # Número decimal (float)
genero = 'F'  # Letra representando o gênero (string)
nome = 'Victoria'  # Nome como string (texto)

# Exibindo as variáveis usando f-strings para formatação moderna
print(f'idade = {idade}')  # Exibe a idade normalmente

# Exibe o salário com duas casas decimais
print(f'salario = {salario:.2f}')  # {:.2f} força duas casas decimais

# Exibe a altura com duas casas decimais
print(f'altura = {altura:.2f}')  # {:.2f} força duas casas decimais

# Exibe o gênero e o nome normalmente
print(f'genero = {genero}')
print(f'nome = {nome}')
