#Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo 
#salário com reajuste de 35% 

salario_atual = float(input('Qual é seu salário?\n'))

salario_novo = salario_atual * 0.35
salario_novo = salario_atual + salario_novo

print(f'Seu novo salário é: {salario_novo:.2f}')