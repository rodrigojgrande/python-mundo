#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

print('='*15, '\033[1;33mJO KEN PO\033[m', '='*15, )

print('\033[1;33mSUAS OPÇÕES\033[m')
print('[ \033[1;33m1\033[m ] PEDRA')
print('[ \033[1;33m2\033[m ] PAPEL')
print('[ \033[1;33m3\033[m ] TESOURA')

player = int(input('Qual é a sua jogada? '))

from random import randint
machine = randint(1, 3)

from time import sleep
print('\033[1;31mJO!\033[m')
sleep(1)
print('\033[1;33mKEN!!\033[m')
sleep(1)
print('\033[1;32mPO!!!\033[m')
sleep(1)

if player != 1 and player != 2 and player != 3:
    print('\033[1;31opsss! Algo de inesperado aconteceu!\033[m')
else:
    if player == 1:
        player = 'Pedra'
        if machine == 1:
            machine = 'Pedra'
            resultado = '\033[1;33mEmpate!\033[m'
        elif machine == 2: 
            machine = 'Papel'
            resultado = '\033[1;31mMáquina Vence!\033[m'
        else:
            machine = 'Tesoura'
            resultado = '\033[1;32mJogador Vence!\033[m'
    if player == 2:
        player = 'Papel'
        if machine == 1:
            machine = 'Pedra'
            resultado = '\033[1;32mJogador Vence!\033[m'
        elif machine == 2: 
            machine = 'Papel'
            resultado = '\033[1;33mEmpate!\033[m'
        else:
            machine = 'Tesoura'
            resultado = '\033[1;31mMáquina Vence!\033[m'
    if player == 3:
        player = 'Tesoura'
        if machine == 1:
            machine = 'Pedra'
            resultado = '\033[1;31mMáquina Vence!\033[m'
        elif machine == 2: 
            machine = 'Papel'
            resultado = '\033[1;32mJogador Vence!\033[m'
        else:
            machine = 'Tesoura'
            resultado = '\033[1;33mEmpate!\033[m'




print('\033[1;33m-=\033[m'*10)
print('Computador jogou \033[1;35m{}\033[m'.format(machine))
print('Jogador jogou \033[1;34m{}\033[m'.format(player))
print('\033[1;33m-=\033[m'*10)
print(resultado)


