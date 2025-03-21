#Crie 3 variáveis para guardar três notas informadas por um aluno e exiba a sua média aritmética.

nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a  segunda nota:\n'))
nota3 = float(input('Digite a terceira nota:\n'))

media = (nota1 + nota2 + nota3) / 3

print(f'A media corresponde a: {media}')