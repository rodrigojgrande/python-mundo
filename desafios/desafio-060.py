#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

from math import sqrt fatorial
f = factorial(x)

x = int(input('\033[1;34mDigite um número para calcular seu Fatorial:\033[m '))
print('Calculando {}! = '.format(x), end='')
total = x
while x > 1:
    print('{} x '.format(x), end='')
    x -= 1
    total = total * x
print('1 = {}'.format(total))

