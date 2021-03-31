#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)

machine = randint(0, 5)

player = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if player == machine:
    print('PARABÉNS! Você conseguiu vencer!')
else: 
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(machine, player))

#Tratar Número Errado
#if player == (0 or 1 or 2 or 3 or 4 or 5):
#else:  player = int(input('Número incorreto! Tente inserir um valor de 0 a 5:  '))

