# Solicita a idade do usuário e converte para um número inteiro
idade = int(input("Digite sua idade: "))  # input() retorna uma string, então usamos int() para converter

# Estrutura condicional para verificar a faixa etária
if idade >= 18:  # Se a idade for 18 ou mais
    print("Você é maior de idade.")  # Executa esta linha se a condição for verdadeira

elif idade >= 12:  # Se a idade for menor que 18, mas 12 ou maior
    print("Você é um adolescente.")  # Executa esta linha se a condição for verdadeira

else:  # Se nenhuma das condições acima for atendida (idade < 12)
    print("Você é uma criança.")  # Executa esta linha
