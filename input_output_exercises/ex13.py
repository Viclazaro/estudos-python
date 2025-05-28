# 13) Faça um algoritmo que guarde em um variáveis o peso e a altura de uma pessoa. O algoritmo deve 
#retornar o nome e o IMC (Índice de Massa Corporal) dessa pessoa. Para obter o IMC, basta dividir o 
#seu peso (em quilos) pela altura (em metros) elevada ao quadrado (altura x altura)

nome = input("Digite o nome da pessoa: ")
peso = float(input("Digite o peso da pessoa (em kg): "))
altura = float(input("Digite a altura da pessoa (em metros): "))

imc = peso / (altura ** 2)

print(f"{nome}, seu IMC é: {imc:.2f}")