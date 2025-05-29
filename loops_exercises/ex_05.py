#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input("Qual seu nome [mínimo 4 caracteres]: ")
while len(nome) <= 3:
    print('Nome deve conter mais de 3 caracteres.')
    nome = input("Qual seu nome [mínimo 4 caracteres]: ")

idade = int(input("Sua idade: "))
while idade < 0 or idade > 150:
    print("Você deve ter entre 0 e 150 anos.")
    idade = int(input("Sua idade: "))

salario = float(input("Salário: "))
while salario <= 0:
    print("Salário deve ser maior que zero.")
    salario = float(input("Salário: "))

sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
while sexo != 'f' and sexo != 'm':
    print("Sexo inválido. Digite 'f' para feminino ou 'm' para masculino.")
    sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")

civil = input("Estado civil (s, c, v ou d): ")
while civil not in ['s', 'c', 'v', 'd']:
    print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
    civil = input("Estado civil (s, c, v ou d): ")