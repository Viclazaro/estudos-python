#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_colaborador = float(input('Digite seu salario:\n'))

if salario_colaborador <= 280:
    percentual = 20 

elif 280 < salario_colaborador <= 700:
    percentual = 15
 
elif 700 < salario_colaborador <= 1500:
    percentual = 10 

else:
    percentual = 5 
    
aumento = (percentual/100) * salario_colaborador
novo_salario = aumento + salario_colaborador

print(f'Salário original: {salario_colaborador:.2f}')
print(f'Percentual de aumento aplicado: {percentual}%')
print(f'Valor do aumento: {aumento:.2f}')
print(f'Novo salario: {novo_salario:.2f}')
