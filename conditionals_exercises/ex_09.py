#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
#  A atribuição de conceitos obedece à tabela abaixo:

#      Média de Aproveitamento  Conceito
#      Entre 9.0 e 10.0                      A
#      Entre 7.5 e 9.0                       B
#      Entre 6.0 e 7.5                       C
#      Entre 4.0 e 6.0                       D
#      Entre 4.0 e zero                      E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
# ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))

media = (nota1 + nota2)/2 

if 9.0 <= media <= 10.0:
    print(f'Notas: {nota1} e {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: A')
    print('Aprovado')


elif 7.5 <= media < 9.0:
    print(f'Notas: {nota1} e {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: B')
    print('Aprovado')

elif 6.0 <= media < 7.5:
    print(f'Notas: {nota1} e {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: C')
    print('Aprovado')

elif 4.0 <= media < 6.0:
    print(f'Notas: {nota1} e {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: D')
    print('Reprovado')

else: 
    print(f'Notas: {nota1} e {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: E')
    print('Reprovado')