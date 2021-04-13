#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
n = int (input('Quantos termos: '))
c = 2
x = 0
y = 1
print('{} -> {} '.format(x, y), end='')
while c != n:
    c += 1
    z = x + y
    print('-> {}'.format(z), end=' ')
    x = y
    y = z
print('-> FIM')
