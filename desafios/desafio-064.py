#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''c = 0
n = 0
total = 0
while n != 999:
    n = int (input('Digite o número [999 para parar]: '))
    total += n 
    c += 1
total -= 999
print('Você digitou {} números e a soma entre eles foi de {}'.format(c, total))'''

#TEACHER
c = 0
n = 0
total = 0
n = int (input('Digite o número [999 para parar]: '))
while n != 999:
    total += n 
    c += 1
    n = int (input('Digite o número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi de {}'.format(c, total))