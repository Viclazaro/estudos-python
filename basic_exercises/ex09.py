# 9) Crie um algoritmo que guarde em variáveis o nome de uma pessoa e o ano de nascimento dela. O 
# algoritmo deve retornar o nome da pessoa e a sua idade.

nome = input('Digite seu nome:\n') # Receber dado e armazenar na variavel "nome"
data = int(input('Digite sua data de nascimento:\n')) # Receber dado e armazenar na variavel "data" declarando seu tipo

idade = 2025 - data

print(f'Seu nome é {nome}, possui {idade} anos de idade')

