# 11) O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que 
#receba em uma variável o peso (em gramas) do prato montado pelo cliente. O algoritmo deve imprimir 
#o valor que o cliente deve pagar pela comida. Assuma que a balança já desconte o peso do prato. 

peso_gramas = float(input('Digite o peso do prato montado pelo cliente (em gramas):\n'))

peso_quilos = peso_gramas / 1000

valor_pago = peso_quilos * 12

print(f'Valor total: R${valor_pago:.2f}')