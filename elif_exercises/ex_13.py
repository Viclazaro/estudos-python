#Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

x = input(str('Escolha:\n F - Feminino\n M - Masculino\n'))

if x == 'F':
     print('Feminino')

elif x == 'M':
      print('Masculino')

else:
    print('inválido')

