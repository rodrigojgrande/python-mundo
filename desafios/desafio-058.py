#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

tentativas = 0

print('-=-' * 20)
print('\033[1;33mVou pensar em um número entre 0 e 100\033[m ')
print('-=-' * 20)

machine = randint(0, 100)

print('\033[34mSerá que você consegue adivinhar qual foi?\033[m')
player = int(input('\033[1;34mQual o seu palpite?\033[m '))

while player != machine:
    if player > machine:
        print('\033[1;33mPROCESSANDO...\033[m')
        sleep(1)
        player = int(input('\033[1;31mMenos... Tente mais uma vez.\033[m '))
        tentativas += 1
    elif player < machine:
        print('\033[1;33mPROCESSANDO...\033[m')
        sleep(1)
        player = int(input('\033[1;31mMais... Tente mais uma vez.\033[m '))
        tentativas += 1
sleep(1)
tentativas += 1
print('\033[1;32mAcertou com {} tentativas! Parabéns!\033[m'.format(tentativas))
