# 10) Uma variável que guarde o salário fixo de um vendedor, outra o total ($) de vendas por ele efetuadas e 
#outra o percentual de comissão que ele ganha sobre o total vendido. O algoritmo deve imprimir a 
#comissão do vendedor e o seu salário final.

salario_fixo = float(input('Digite seu salario fixo:\n')) 

total_vendas = float(input('Digite o total de vendas:\n')) 

comissao_percentual = float(input("Digite o percentual de comissão do vendedor (em %): "))

comissao = (comissao_percentual / 100) * total_vendas

salario_final = salario_fixo + comissao

print(f'Comissao: {comissao}')
print(f'Salario: {salario_final}')