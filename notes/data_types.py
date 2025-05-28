# Definição de variáveis e tipos de dados em Python

# 📌 Variáveis simples sem anotação de tipo
nome = "Victoria"  # String (texto)
idade = 19         # Inteiro (int)
altura = 1.71      # Float (número decimal)
tem_pet = True     # Booleano (True ou False)

# Exibindo as variáveis
print(nome, idade, altura, tem_pet)


# 📌 Definição de tipos de variáveis (anotação de tipo, não obrigatória)
idade: int  # Apenas números inteiros
salario: float  # Números com casas decimais
altura: float  # Aceita números decimais
genero: str  # Representa um caractere ou texto
nome: str  # Conjunto de caracteres que formam um texto

# Atribuição de valores às variáveis
idade = 20  
salario = 1200  
altura = 1.71  
genero = 'F'  
nome = 'Victoria'  

# Exibindo as variáveis com f-strings para melhor formatação
print(f'Idade = {idade}')  
print(f'Salário = {salario:.2f}')  # Mostra duas casas decimais
print(f'Altura = {altura:.2f}')  # Mostra duas casas decimais
print(f'Gênero = {genero}')
print(f'Nome = {nome}')
