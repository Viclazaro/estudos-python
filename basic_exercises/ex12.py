# 12) Escreva um algoritmo para guarde em 4 variáveis o número total de eleitores de um município, o 
#número de votos brancos, nulos e válidos. Calcular e imprimir o percentual que cada um representa em 
#relação ao total de eleitores. 

total_eleitores = int(input('Numero de eleitores:\n'))
brancos =  int(input('Numero de votos brancos:\n'))
nulos = int(input('Numero de votos nulos:\n'))
validos = int(input('Numero de votos validos:\n'))

brancos_percentual = (brancos*100)/total_eleitores
nulos_percentual = (nulos*100)/total_eleitores
validos_percentual = (validos*100)/total_eleitores

print(f"Percentual de votos brancos: {brancos_percentual:.2f}%")
print(f"Percentual de votos nulos: {nulos_percentual:.2f}%")
print(f"Percentual de votos válidos: {validos_percentual:.2f}%")