#ESTUDO 1

x:int  # Define que x será do tipo inteiro
y:int  # Define que y será do tipo inteiro

x = 5  # Atribui o valor 5 à variável x
y = 2 * x  # Atribui à variável y o valor de 2 vezes x, ou seja, 2 * 5 = 10

print(x)  # Imprime o valor de x, que é 5
print(y)  # Imprime o valor de y, que é 10

#ESTUDO 2

x: int  # Define que x será do tipo inteiro
y: float  # Define que y será do tipo ponto flutuante (decimal)

x = 5  # Atribui o valor 5 à variável x
y = 2 * x  # Atribui à variável y o valor de 2 vezes x, ou seja, 2 * 5 = 10

print(x)  # Imprime o valor de x, que é 5
print(f"{y:.1f}")  # Imprime y com uma casa decimal

#ESTUDO 3

b1: float; b2: float; h: float; area: float # Define os tipos das variáveis

b1 = 6.0  # Atribui o valor 6.0 à base b1
b2 = 8.0  # Atribui o valor 8.0 à base b2
h = 5.0   # Atribui o valor 5.0 à altura h

area = (b1 + b2) / 2.0 * h # aplicando formula

print(area) # imprimindo resultado

#ESTUDO 4

a: int; b: int; resultado: int  # Define os tipos das variáveis
a = 5  # Atribui o valor 5 à variável a
b = 2  # Atribui o valor 2 à variável b
resultado = a // b  # Realiza uma divisão inteira entre a e b
print(resultado)  # Imprime o resultado da divisão inteira

#ESTUDO 5
a: float  # Define a variável a como float
b: int    # Define a variável b como int
a = 5.0   # Atribui o valor 5.0 (float) à variável a
b = int(a)  # Converte o valor de a (float) para int e atribui a b
print(b)   # Imprime o valor de b
