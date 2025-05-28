#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa 
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

respostas_positivas = 0

print('Responda com 1 para "Sim" ou 2 para "Não"')
resposta1 = int(input('Telefonou para a vítima? '))
resposta2 = int(input('Esteve no local do crime? '))
resposta3 = int(input('Mora perto da vítima? '))
resposta4 = int(input('Devia para a vítima? '))
resposta5 = int(input('Já trabalhou com a vítima? '))

# Contagem de respostas positivas
if resposta1 == 1:
    respostas_positivas += 1
if resposta2 == 1:
    respostas_positivas += 1
if resposta3 == 1:
    respostas_positivas += 1
if resposta4 == 1:
    respostas_positivas += 1
if resposta5 == 1:
    respostas_positivas += 1

if respostas_positivas == 2:
    classificado = 'Suspeito(a)'
elif respostas_positivas == 3 or respostas_positivas == 4:
    classificado = 'Cúmplice'
elif respostas_positivas == 5:
    classificado = 'Assassino'
else:
    classificado = 'Inocente'

print(f'O resultado é: {classificado}')





