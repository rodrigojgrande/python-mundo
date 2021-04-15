#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

#MY WAY
#a = randint(0, 9)
#b = randint(0, 9)
#c = randint(0, 9)
#d = randint(0, 9)
#e = randint(0, 9)

#tupla = (a, b, c, d, e)

#print(f'Os valores sorteados foram: {tupla[0:5]}')
#print(f'O maior valor sorteado foi: {max(tupla)}')
#print(f'O menor valor sorteado foi: {min(tupla)}')

#TEACHER WAY
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')