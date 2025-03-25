# Solicita três números inteiros ao usuário
primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))

# Determina o maior número
maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

# Determina o menor número
menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

# Exibe os resultados
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
